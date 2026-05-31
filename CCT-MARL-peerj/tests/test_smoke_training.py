from cct_marl.communication.mean_broadcast import MeanBroadcastAggregator
from cct_marl.experience.experience_manager import ExperienceManager

def test_mean_broadcast():
    agg = MeanBroadcastAggregator().aggregate([[1,2,3],[3,4,5]])
    assert agg.tolist() == [2.0, 3.0, 4.0]

def test_experience_update():
    manager = ExperienceManager(1)
    s = manager.update(0, positive=1.0)
    assert s.alpha > 1.0
