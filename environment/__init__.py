from gymnasium.envs.registration import register

register(
    id="hilo_single_player",
    entry_point="environment.hilo_env:EnvHiLoSinglePlayer"
)
