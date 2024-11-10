import gymnasium as gym


def main():
    env_name = "environment:hilo_single_player"
    env = gym.make(env_name)

    state, _ = env.reset()


if __name__ == "__main__":
    main()
