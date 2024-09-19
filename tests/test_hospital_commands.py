from unittest.mock import MagicMock

import pytest

from exceptions import PatientIDTypeError
from hospital_commands import HospitalCommands
from hospital import Hospital


def test_get_status():
    dialog_with_user = MagicMock()
    hospital = Hospital([1, 3])
    hospital_commands = HospitalCommands(hospital, dialog_with_user)
    dialog_with_user.request_patient_id = MagicMock(return_value=1)

    hospital_commands.get_status()
    dialog_with_user.send_status.assert_called_once_with("Болен")


def test_get_status_when_id_type_invalid():
    dialog_with_user = MagicMock()
    hospital = Hospital([1, 3])
    hospital_commands = HospitalCommands(hospital, dialog_with_user)
    dialog_with_user.request_patient_id = MagicMock(side_effect=PatientIDTypeError)

    hospital_commands.get_status()
    dialog_with_user.send_message.assert_called_once_with(
        "Ошибка. ID пациента должно быть числом (целым, положительным)")


def test_get_status_when_patient_missing():
    dialog_with_user = MagicMock()
    hospital = Hospital([1, 3])
    hospital_commands = HospitalCommands(hospital, dialog_with_user)
    dialog_with_user.request_patient_id = MagicMock(return_value=10)

    hospital_commands.get_status()
    dialog_with_user.send_message.assert_called_once_with("Ошибка. В больнице нет пациента с таким ID")


def test_status_up():
    dialog_with_user = MagicMock()
    hospital = Hospital([1, 3])
    hospital_commands = HospitalCommands(hospital, dialog_with_user)
    dialog_with_user.request_patient_id = MagicMock(return_value=1)

    hospital_commands.status_up()
    assert hospital.patients == [2, 3]
    dialog_with_user.send_new_status.assert_called_once_with("Слегка болен")


def test_status_up_with_max_status_when_discharge_confirmed():
    dialog_with_user = MagicMock()
    hospital = Hospital([1, 3])
    hospital_commands = HospitalCommands(hospital, dialog_with_user)
    dialog_with_user.request_patient_id = MagicMock(return_value=2)
    dialog_with_user.request_discharge_confirmation = MagicMock(return_value=True)

    hospital_commands.status_up()
    assert hospital.patients == [1, None]
    dialog_with_user.send_discharged.assert_called_once()


def test_status_up_with_max_status_when_discharge_declined():
    dialog_with_user = MagicMock()
    hospital = Hospital([1, 3])
    hospital_commands = HospitalCommands(hospital, dialog_with_user)
    dialog_with_user.request_patient_id = MagicMock(return_value=2)
    dialog_with_user.request_discharge_confirmation = MagicMock(return_value=False)

    hospital_commands.status_up()
    assert hospital.patients == [1, 3]
    dialog_with_user.send_status_not_changed.assert_called_once()


def test_status_up_when_id_type_invalid():
    dialog_with_user = MagicMock()
    hospital = Hospital([1, 3])
    hospital_commands = HospitalCommands(hospital, dialog_with_user)
    dialog_with_user.request_patient_id = MagicMock(side_effect=PatientIDTypeError)

    hospital_commands.status_up()
    assert hospital.patients == [1, 3]
    dialog_with_user.send_message.assert_called_once_with(
        "Ошибка. ID пациента должно быть числом (целым, положительным)")


def test_status_up_when_patient_missing():
    dialog_with_user = MagicMock()
    hospital = Hospital([1, 3])
    hospital_commands = HospitalCommands(hospital, dialog_with_user)
    dialog_with_user.request_patient_id = MagicMock(return_value=10)

    hospital_commands.status_up()
    assert hospital.patients == [1, 3]
    dialog_with_user.send_message.assert_called_once_with("Ошибка. В больнице нет пациента с таким ID")


def test_discharge():
    dialog_with_user = MagicMock()
    hospital = Hospital([1, 3])
    hospital_commands = HospitalCommands(hospital, dialog_with_user)
    dialog_with_user.request_patient_id = MagicMock(return_value=1)

    hospital_commands.discharge()
    assert hospital.patients == [None, 3]
    dialog_with_user.send_discharged.assert_called_once()


def test_discharge_when_patient_missing():
    dialog_with_user = MagicMock()
    hospital = Hospital([1, 3])
    hospital_commands = HospitalCommands(hospital, dialog_with_user)
    dialog_with_user.request_patient_id = MagicMock(return_value=10)

    hospital_commands.discharge()
    assert hospital.patients == [1, 3]
    dialog_with_user.send_message.assert_called_once_with("Ошибка. В больнице нет пациента с таким ID")


def test_discharge_when_id_type_invalid():
    dialog_with_user = MagicMock()
    hospital = Hospital([1, 3])
    hospital_commands = HospitalCommands(hospital, dialog_with_user)
    dialog_with_user.request_patient_id = MagicMock(side_effect=PatientIDTypeError)

    hospital_commands.discharge()
    assert hospital.patients == [1, 3]
    dialog_with_user.send_message.assert_called_once_with("Ошибка. ID пациента должно быть числом (целым, положительным)")