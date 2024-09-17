from unittest.mock import MagicMock

import pytest

from exceptions import PatientIDTypeError, PatientMissingError
from hospital_commands import HospitalCommands
from hospital import Hospital


def test_get_status():
    dialog_with_user = MagicMock()
    hospital =  Hospital([1, 3])
    hospital_commands = HospitalCommands(hospital, dialog_with_user)
    dialog_with_user.request_patient_id = MagicMock(return_value=1)

    hospital_commands.get_status()
    dialog_with_user.send_message.assert_called_once_with("Болен")

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
    dialog_with_user.request_patient_id = MagicMock(side_effect=PatientMissingError)

    hospital_commands.get_status()
    dialog_with_user.send_message.assert_called_once_with("Ошибка. В больнице нет пациента с таким ID")

def test_status_up():
    dialog_with_user = MagicMock()
    hospital = Hospital([1, 3])
    hospital_commands = HospitalCommands(hospital, dialog_with_user)
    dialog_with_user.request_patient_id = MagicMock(return_value=1)

    hospital_commands.status_up()
    assert hospital.patients == [2, 3]
    dialog_with_user.send_message.assert_called_once_with('Новый статус пациента: "Слегка болен"')

def test_status_up_with_max_status_when_discharge_confirmed():
    dialog_with_user = MagicMock()
    hospital = Hospital([1, 3])
    hospital_commands = HospitalCommands(hospital, dialog_with_user)
    dialog_with_user.request_patient_id = MagicMock(return_value=2)
    dialog_with_user.request_discharge_confirmation = MagicMock(return_value=True)

    hospital_commands.status_up()
    assert hospital.patients == [1, None]
    dialog_with_user.send_message.assert_called_once_with('Пациент выписан из больницы')

def test_status_up_with_max_status_when_discharge_declined():
    dialog_with_user = MagicMock()
    hospital = Hospital([1, 3])
    hospital_commands = HospitalCommands(hospital, dialog_with_user)
    dialog_with_user.request_patient_id = MagicMock(return_value=2)
    dialog_with_user.request_discharge_confirmation = MagicMock(return_value=False)

    hospital_commands.status_up()
    assert hospital.patients == [1, 3]
    dialog_with_user.send_message.assert_called_once_with('Пациент остался в статусе "Готов к выписке"')

def test_status_up_when_id_type_invalid():
    dialog_with_user = MagicMock()
    hospital = Hospital([1, 3])
    hospital_commands = HospitalCommands(hospital, dialog_with_user)
    dialog_with_user.request_patient_id = MagicMock(side_effect=PatientIDTypeError)

    hospital_commands.status_up()
    dialog_with_user.send_message.assert_called_once_with(
        "Ошибка. ID пациента должно быть числом (целым, положительным)")
