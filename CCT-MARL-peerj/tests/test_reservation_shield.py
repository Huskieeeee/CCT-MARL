from cct_marl.shield.reservation_shield import ReservationShield

def test_same_target_conflict_intervention():
    shield = ReservationShield((5,5))
    result = shield.apply([(0,0),(0,2)], ["Right", "Left"])
    assert len(result["actions"]) == 2
    assert result["interventions"] >= 1
