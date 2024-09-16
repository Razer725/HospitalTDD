def test_get_status():
    hospital = Hospital()
    assert hospital.get_status() == "Болен"