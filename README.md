# Reinforcement Learning Project

This project explores the application of the TD3 algorithm to the CarRacing-v2 environment using OpenAI's Gym. Originally, we considered the Trackmania environment but switched to CarRacing-v2 due to resource limitations. Our aim was to train an autonomous agent to navigate a randomly generated race track with continuous control inputs.

<img src="https://github.com/adavidho/racing-rl-project/blob/main/artifacts/animation/td3_car_racer.gif" width="300" />

The project underscores the importance of hyperparameter tuning and demonstrates the practical deployment of reinforcement learning algorithms for complex control tasks.

## Getting Started
Clone the repository:
```
git clone https://github.com/adavidho/racing-rl-project.git
cd ./racing-rl-project
```
Install the required packages. 
Note: We recommend using python version 3.10.14 for compatibility. 
```
pip install -r requirements.txt
```
To excecute the [`td3_car_racing.ipynb`](https://github.com/adavidho/racing-rl-project/blob/main/td3_car_racing.ipynb) notebook we recommend using a screen session with nbconvert as excecution time is high.
Note: On a p3.16xlarge EC2 instance c.a. 27 hours.
```
sceen -S rl
jupyter nbconvert --to notebook --execute  --inplace td3_car_racing.ipynb
```
Now you are ready to have some fun with reinforcement learning.
