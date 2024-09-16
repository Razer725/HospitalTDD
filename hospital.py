from exceptions import PatientMissingError


class Hospital:
    STATUSES = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

    def __init__(self, patients=None):
        if patients is None:
            patients = [1] * 200
        self.patients = patients

    def get_status(self, patient_id):
        inner_id = self._convert_patient_id_to_inner_id(patient_id)
        return self.STATUSES[self.patients[inner_id]]

    def _convert_patient_id_to_inner_id(self, patient_id):
        if patient_id > len(self.patients):
            raise PatientMissingError
        return patient_id - 1
