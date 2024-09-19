from application import Application
from dialog_with_user import DialogWithUser
from hospital import Hospital
from hospital_commands import HospitalCommands
from mock_console import MockConsole


def test_discharge():
    console = MockConsole()
    dialog_with_user = DialogWithUser(console)
    hospital = Hospital([0, 3])
    hospital_commands = HospitalCommands(hospital, dialog_with_user)
    application = Application(hospital_commands, dialog_with_user)

    console.add_expected_request_and_response('Введите команду: ', 'discharge')
    console.add_expected_request_and_response('Введите ID пациента: ', '1')
    console.add_expected_output_message('Пациент выписан из больницы')

    console.add_expected_request_and_response('Введите команду: ', 'discharge')
    console.add_expected_request_and_response('Введите ID пациента: ', '1')
    console.add_expected_output_message('Ошибка. В больнице нет пациента с таким ID')

    console.add_expected_request_and_response('Введите команду: ', 'стоп')
    console.add_expected_output_message('Сеанс завершён.')

    application.run()

    console.verify_all_calls_have_been_made()
    assert hospital.patients == [None, 3]

