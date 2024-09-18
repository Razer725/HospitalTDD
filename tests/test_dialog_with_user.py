from unittest.mock import patch

import pytest

from dialog_with_user import DialogWithUser
from exceptions import PatientIDTypeError


def test_request_patient_id(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '1')
    dialog_with_user = DialogWithUser()
    assert dialog_with_user.request_patient_id() == 1


@pytest.mark.parametrize('user_input', ['0', '-1', 'два', '1.1'])
def test_request_patient_id_wit_invalid_type(monkeypatch, user_input):
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    dialog_with_user = DialogWithUser()
    with pytest.raises(PatientIDTypeError):
        dialog_with_user.request_patient_id()


@pytest.mark.parametrize('user_input', ['да', 'yes'])
def test_request_discharge_confirmation(monkeypatch, user_input):
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    dialog_with_user = DialogWithUser()
    assert dialog_with_user.request_discharge_confirmation()
