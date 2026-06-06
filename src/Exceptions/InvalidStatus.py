class InvalidStatus(Exception):
    def __init__(self, status: int):
        self.status = status

    
    def __str__(self):
        return f"Недопустимый значение: {self.status}.\n Допустимые значения статуса: 0 (NotStarted), 1 (InWork), 2 (Finished)"