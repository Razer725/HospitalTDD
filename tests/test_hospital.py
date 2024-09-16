import pytest

from exceptions import PatientMissingError
from hospital import Hospital


def test_get_status():
    hospital = Hospital([1, 3])
    assert hospital.get_status(1) == "Болен"


@pytest.mark.parametrize('patient_id', [10, 2])
def test_get_status_when_patient_missing(patient_id):
    hospital = Hospital([0, None, 2])
    with pytest.raises(PatientMissingError):
        hospital.get_status(patient_id)
