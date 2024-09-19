from exceptions import PatientMissingError, StatusUpError


class Hospital:
    STATUSES = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

    def __init__(self, patients=None):
        if patients is None:
            patients = [1] * 200
        self.patients = patients

    def get_status(self, patient_id):
        inner_id = self._convert_patient_id_to_inner_id(patient_id)
        if self.patients[inner_id] is None:
            raise PatientMissingError
        return self.STATUSES[self.patients[inner_id]]

    def _convert_patient_id_to_inner_id(self, patient_id):
        inner_id = patient_id - 1
        if patient_id > len(self.patients) or self.patients[inner_id] is None:
            raise PatientMissingError
        return inner_id

    def status_up(self, patient_id):
        inner_id = self._convert_patient_id_to_inner_id(patient_id)
        if self.patients[inner_id] == max(self.STATUSES):
            raise StatusUpError
        self.patients[inner_id] += 1

    def can_status_up(self, patient_id):
        inner_id = self._convert_patient_id_to_inner_id(patient_id)
        return max(self.STATUSES) != self.patients[inner_id]

    def discharge(self, patient_id):
        inner_id = self._convert_patient_id_to_inner_id(patient_id)
        self.patients[inner_id] = None
