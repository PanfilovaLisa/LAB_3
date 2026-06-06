from src.Exceptions import InvalidPriorityLevel

class PriorityDescriptor:
    def __init__(self, min: int, max: int):
        self.min = min
        self.max = max

    
    def __set_name__(self, owner, name):
        self._name=f"_{name}"


    
    def __get__(self, instance, owner: type = None):
        if not instance:
            return self
        
        return getattr(instance, self._name)

        

    def __set__(self, instance, value: int):
        if not isinstance(value, int):
            raise TypeError(f"Ожидался int, получен: {type(value)}")
        
        if self.min <= value <= self.max:
            setattr(instance, self._name, value)
            return 
        
        raise InvalidPriorityLevel(value, self.min, self.max)