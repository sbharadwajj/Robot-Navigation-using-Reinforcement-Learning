import sys
import time
import Adafruit_PCA9685
import numpy as np
import keras
import random
import os
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.models import model_from_json
from quadpod import quadpod 
import paho.mqtt.client as paho
broker="127.0.0.1"

np.random.seed(7)
rcvflag = 0

#Creating the environment
env = quadpod()

#Parameters
y = 0.90 #0.90
eps = 0.5 #Prev Valu = 0.5
decay_factor = 0.99
mes = "0 0"

def on_message(client, userdata, message):
    global rcvflag
    global mes
    mes = str(message.payload.decode("utf-8")) 
    rcvflag = 1

def getReward():
    global rcvflag
    rcvflag = 0 
    client.publish("ack","rr")
    print("waiting")
    while rcvflag == 0:
        pass
    print("Receievd")
    print(mes)
    [a,b] = mes.split()
    done = int(a)
    rew = int(b)
    rcvflag = 0
    print(env.state)
    print(env.oldstate)
    if rew == 0:
        rew = 10
    else:
        rew = 10*rew
    if done == 0:
        if env.state == env.oldstate:
            rew = -100
        return False,rew
    else:
        return True,rew

client= paho.Client("client-001") 
client.on_message=on_message
client.connect(broker)
client.loop_start()
client.subscribe("outTopic")


def model_ann():
    model = Sequential()
    # model.add(InputLayer(batch_input_shape=(1, 8)))
    model.add(Dense(8, input_shape=(8,), activation='relu'))
    model.add(Dense(32, activation='relu'))
    #model.add(Dense(32, activation='relu'))   #might overfit, add if needed
    model.add(Dense(24, activation='linear'))
    model.compile(loss='mse', optimizer=Adam(lr=0.1))
    return model

model = model_ann()



currentState = env.reset()
#print(state)
eps *= decay_factor
#r_sum = 0
done = False
while not done:
    #print(np.array(state).shape)
    outputNeuralNet = np.argmax(model.predict(np.array([currentState]),batch_size=None))
    #print(outputNeuralNet)
    new_state = env.step(outputNeuralNet)
    done, r = getReward()
    target = r + y * np.max(model.predict(np.array([new_state])))
    target_vec = model.predict(np.array([currentState]))[0]
    #print(target)
    target_vec[outputNeuralNet] = target
    model.fit(np.array([currentState]), target_vec.reshape(-1, 24), epochs=1, verbose=0)
    currentState = new_state
    print(done)
    print(r)
    time.sleep(0.03)

model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")
