from unittest.mock import patch

from dialog_with_user import DialogWithUser


@patch('builtins.input', return_value='1')
def test_request_patient_id(mock_input):
    dialog_with_user = DialogWithUser()
    assert dialog_with_user.request_patient_id() == 1
