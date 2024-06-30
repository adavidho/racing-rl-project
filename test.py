import gymnasium as gym
import imageio
import numpy as np

env = gym.make("CarRacing-v2", continuous=False, render_mode="rgb_array") # human for display window.
env.reset()

frames = []
for i in range(100):
    frame = env.render()
    frames.append(frame)
    s, r, terminated, truncated, info = env.step(3)  # 0-th action is no_op action

env.close()

# Save rendering as GIF.
output_file = "test_eval.gif"
# imageio.mimsave(output_file, frames, fps=30)
