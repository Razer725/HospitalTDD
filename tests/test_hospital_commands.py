from unittest.mock import MagicMock

import pytest

from exceptions import PatientIDTypeError
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

    with pytest.raises(PatientIDTypeError):
        hospital_commands.get_status()
