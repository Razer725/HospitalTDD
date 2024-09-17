from unittest.mock import MagicMock

from hospital_commands import HospitalCommands
from hospital import Hospital


def test_get_status():
    dialog_with_user = MagicMock()
    hospital =  Hospital([1, 3])
    hospital_commands = HospitalCommands(hospital, dialog_with_user)
    dialog_with_user.request_patient_id = MagicMock(return_value=1)

    hospital_commands.get_status()
    dialog_with_user.send_message.assert_called_once_with("Болен")