class Hospital:
    STATUSES = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

    def __init__(self, patients=None):
        if patients is None:
            patients = [1] * 200
        self.patients = patients
