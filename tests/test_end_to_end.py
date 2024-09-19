from dialog_with_user import DialogWithUser
from hospital import Hospital
from hospital_commands import HospitalCommands


def test_discharge():
    dialog_with_user = DialogWithUser()
    hospital = Hospital()
    hospital_commands = HospitalCommands(hospital, dialog_with_user)
    application = Application(hospital_commands)

