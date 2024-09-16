from hospital import Hospital


def test_get_status():
    hospital = Hospital()
    assert hospital.get_status(1) == "Болен"