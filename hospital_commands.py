class HospitalCommands:
    def __init__(self, hospital, dialog_with_user):
        self.hospital = hospital
        self.dialog_with_user = dialog_with_user

    def get_status(self):
        patient_id = self.dialog_with_user.request_patient_id()
        status = self.hospital.get_status(patient_id)
        self.dialog_with_user.send_message(status)