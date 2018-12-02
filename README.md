# Robotic Navigation using Reinforcement Learning

We chose a 4 legged quadpod which has 3 servo motors per leg. We calibrated each servo motor and restricted its degree of freedom to a certain set threshold such that each leg has 2 states and our state/action space has 8 dimensions. Our objective was to make the robot traverse from a starting point to a destination point and learn the optimal policy for its navigation between two points. The main challenge we faced was to create a partially observable environment for the agent to perform its action in a real world scenario.  We accomplished this by setting up a camera whose field of view consisted of the current position of the robot, its initial and destination points. Instead of consuming the entire frame(which will be dimensionally expensive) as the observation from the environment, we used only the information of the current position of the agent wrt to its initial and destination coordinates. We used the ϵ-greedy Q-learning with delayed reward to test the exploration of the agent, the agent was rewarded as it moved forward closer to the destination and punished when it moved backward away from the destination. At each step(t), the agent received information of its state along with the respective reward signal and a neural network was used to predict the Q values for each action, given a state. To further improve the results we planned to simulate the environment and train the algorithm in a simulated space in the future

## Video Demonstration
[QuadPod Video Demonstration](https://www.youtube.com/watch?v=DdDxthpPoiM)

## Repository Contents
+ Model-test file
+ Pretrained model weights
+ [Custom Marker](https://github.com/AnilBattalahalli/marker-for-RL)
+ Caliberation of the quadpod

## Design of the algorithm

![](https://github.com/chichilicious/Robot-Navigation-using-Reinforcement-Learning/blob/master/RL%20Algorithm.jpg)

## Additional Information

We wrote our own environment which is not added to the contents of this repository yet.
