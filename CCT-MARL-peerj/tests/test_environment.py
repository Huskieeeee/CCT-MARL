from cct_marl.envs.construction_env import ConstructionCoordinationEnv

def test_environment_step():
    env = ConstructionCoordinationEnv()
    obs = env.reset()
    assert "positions" in obs
    obs, reward, done, info = env.step(["Wait", "Wait", "Wait"])
    assert "waiting" in info
