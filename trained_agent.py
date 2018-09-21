import numpy as np
import keras
import random
import os
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.models import model_from_json
from quadpod import quadpod 
import time

#np.random.seed(7)

env = quadpod()

#load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")
loaded_model.compile(loss='mse', optimizer=Adam(lr=0.1))

# Reset State
state = env.reset()
prev_op = 0

for q in range(0,10000):
    # Predict action based on loaded weights and state
    ann_opp = np.argmax(loaded_model.predict(np.array([state]),batch_size=None))
    
    # Perform Action -> Get new state
    if ann_opp == prev_op:
        print("#################STUCK#####################")
        choice = random.randint(0,23)
        new_s = env.step(choice)
        prev_op=choice
    else:
        new_s = env.step(ann_opp)
        prev_op = ann_opp
    #prev = new_s.copy()
    # done, r = getReward()
    # target = r + y * np.max(loaded_model.predict(np.array([new_s])))
    # target_vec = model.predict(np.array([state]))[0]
    # print(target)
    # target_vec[ann_opp] = target
    # loaded_model.fit(np.array([state]), target_vec.reshape(-1, 24), epochs=1, verbose=0)

    # Replace state with new state
    state = new_s
    time.sleep(0.03)

