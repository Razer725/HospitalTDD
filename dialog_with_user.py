from exceptions import PatientIDTypeError


class DialogWithUser:
    def request_patient_id(self):
        patient_id = input("Введите ID пациента: ")
        if not patient_id.isdigit() or int(patient_id) == 0:
            raise PatientIDTypeError

        return int(patient_id)

    def request_discharge_confirmation(self):
        user_answer = input("Желаете этого клиента выписать? (да/нет): ")
        return user_answer in ('yes', 'да')

    def send_message(self, message):
        print(message)

    def send_status(self, status):
        self.send_message(f'Статус пациента: "{status}"')
