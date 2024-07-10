# Reinforcement Learning Project

<img src="https://github.com/adavidho/racing-rl-project/blob/main/artifacts/animation/td3_car_racer.gif" width="300" />


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
