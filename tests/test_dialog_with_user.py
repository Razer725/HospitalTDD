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
def test_request_discharge_confirmation_when_answer_positive(monkeypatch, user_input):
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    dialog_with_user = DialogWithUser()
    assert dialog_with_user.request_discharge_confirmation()


@pytest.mark.parametrize('user_input', ['нет', 'no'])
def test_request_discharge_confirmation_when_answer_negative(monkeypatch, user_input):
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    dialog_with_user = DialogWithUser()
    assert not dialog_with_user.request_discharge_confirmation()


def test_send_message(capfd):
    dialog_with_user = DialogWithUser()
    dialog_with_user.send_message('Статус пациента: "Болен"')
    assert capfd.readouterr().out == 'Статус пациента: "Болен"\n'


def test_send_status(capfd):
    dialog_with_user = DialogWithUser()
    dialog_with_user.send_status("Болен")
    assert capfd.readouterr().out == 'Статус пациента: "Болен"\n'
