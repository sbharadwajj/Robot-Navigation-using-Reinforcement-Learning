# Robotic Navigation using Reinforcement Learning

This is an artificially intelligent robot which learns its own navigation pattern with the help of reinforcement learning.The robot learns to navigate from a certain point A to B i.e from a given initial point to a destination point. The interpreter identifies the robot with the help of a marker which is a part of the design of the robot. We implemented our own unique marker system which identifies the robot in an environment and gives the centroid of the robot. The communication between the robot and the interpreter is done using MQTT protocol. We designed our reinforcement algorithm using Q - learning approach with e-greedy exploration strategy. The architecture has a fully connected dense artificial neural network.

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
