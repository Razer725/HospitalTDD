from console import Console
from exceptions import PatientIDTypeError


class DialogWithUser:
    def __init__(self, console=None):
        if console is None:
            console = Console()

        self.console = console

    def request_user_command(self):
        return self.console.input("Введите команду: ")

    def request_patient_id(self):
        patient_id = self.console.input("Введите ID пациента: ")
        if not patient_id.isdigit() or int(patient_id) == 0:
            raise PatientIDTypeError

        return int(patient_id)

    def request_discharge_confirmation(self):
        user_answer = self.console.input("Желаете этого клиента выписать? (да/нет): ")
        return user_answer in ('yes', 'да')

    def send_message(self, message):
        self.console.print(message)

    def send_status(self, status):
        self.console.print(f'Статус пациента: "{status}"')

    def send_discharged(self):
        self.console.print('Пациент выписан из больницы')
