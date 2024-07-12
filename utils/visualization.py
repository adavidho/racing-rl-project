import gymnasium as gym
import imageio
import logging


def render_example(
    model,
    env_id: str = "CarRacing-v2",
    continuous: bool = True,
    render_frames: bool = True,
    output_file: str = None,
) -> None:
    """
    If an output_file location is given, we save to that location.
    Otherwise we do not save any renderings.
    """

    frames = generate_frames(
        model=model,
        env_id=env_id,
        continuous=continuous,
        save_mode=output_file != None,
        render_frames=render_frames,
    )

    if frames:
        create_and_save_GIF(frames=frames, output_file=output_file)


def generate_frames(
    model,
    env_id: str = "CarRacing-v2",
    continuous: bool = True,
    save_mode: bool = True,
    render_frames: bool = True,
) -> None | list:
    """
    Generate the frames for either the GIF to be saved
    or for rendering it straight away.
    """

    if save_mode:
        env = gym.make(env_id, continuous=continuous, render_mode="rgb_array")
        env.reset()
        frames = []
        step_count = 0
        terminated = False
        while not terminated and step_count < 1000:
            frame = env.render()
            frames.append(frame)
            action, _states = model.predict(obs)
            state, reward, terminated, truncated, info = env.step(action)
            step_count += 1

        env.close()
        return frames

    if render_frames:
        env = gym.make(env_id, continuous=continuous, render_mode="human")
        obs = env.reset()
        step_count = 0
        terminated = False
        while not terminated and step_count < 1000:
            env.render()
            action, _states = model.predict(obs)
            state, reward, terminated, truncated, info = env.step(action)
            step_count += 1
        env.close()


def create_and_save_GIF(
    frames: list, output_file: str = "eval.gif", fps: int = 30
) -> None:
    "Generate and save GIF."

    imageio.mimsave(output_file, frames, fps=fps)
    logging.info(f"Saved evaluation GIF to {output_file}")
