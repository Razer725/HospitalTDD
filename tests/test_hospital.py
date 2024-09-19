import pytest

from exceptions import PatientMissingError, StatusUpError
from hospital import Hospital


def test_get_status():
    hospital = Hospital([1, 3])
    assert hospital.get_status(1) == "Болен"


def test_get_status_when_patient_missing():
    hospital = Hospital([0, 2])
    with pytest.raises(PatientMissingError):
        hospital.get_status(10)


def test_get_status_when_patient_discharged():
    hospital = Hospital([0, None, 2])
    with pytest.raises(PatientMissingError):
        hospital.get_status(2)


def test_status_up():
    hospital = Hospital([0, 2])
    hospital.status_up(1)
    assert hospital.patients == [1, 2]


def test_status_up_when_status_max():
    hospital = Hospital([3, 0])
    with pytest.raises(StatusUpError):
        hospital.status_up(1)


def test_discharge():
    hospital = Hospital([0, 2])
    hospital.discharge(1)
    assert hospital.patients == [None, 2]


def test_discharge_when_patient_missing():
    hospital = Hospital([0, 2])
    with pytest.raises(PatientMissingError):
        hospital.discharge(10)


def test_discharge_when_patient_already_discharged():
    hospital = Hospital([None, 2])
    with pytest.raises(PatientMissingError):
        hospital.discharge(1)
