class InvalidPriorityLevel(Exception):
    def __init__(self, level: int, min: int, max: int):
        self.level = level
        self.min = min
        self.max = max

    
    def __str__(self):
        return f"Недопустимый значение: {self.level}.\n Допустимый диапозон уровня приоритета: от {self.min} до {self.max}"