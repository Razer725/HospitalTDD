from exceptions import PatientIDTypeError, PatientMissingError


class HospitalCommands:
    def __init__(self, hospital, dialog_with_user):
        self.hospital = hospital
        self.dialog_with_user = dialog_with_user

    def get_status(self):
        try:
            patient_id = self.dialog_with_user.request_patient_id()
            status = self.hospital.get_status(patient_id)
            self.dialog_with_user.send_message(status)
        except PatientIDTypeError:
            self.dialog_with_user.send_message("Ошибка. ID пациента должно быть числом (целым, положительным)")
        except PatientMissingError:
            self.dialog_with_user.send_message("Ошибка. В больнице нет пациента с таким ID")

    def status_up(self):
        patient_id = self.dialog_with_user.request_patient_id()
        if self.hospital.can_status_up(patient_id):
            self.hospital.status_up(patient_id)
            new_status = self.hospital.get_status(patient_id)
            self.dialog_with_user.send_message(f'Новый статус пациента: "{new_status}"')
        else:
            if self.dialog_with_user.request_discharge_confirmation:
                self.hospital.discharge(patient_id)
                self.dialog_with_user.send_message('Пациент выписан из больницы')
