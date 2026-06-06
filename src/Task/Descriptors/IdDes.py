class TaskIdDescription:
    def __set_name__(self, owner, name):
        self._name=f"_{name}"


    def __get__(self, instance, owner):
        if not instance:
            return self 
        return getattr(instance, self._name)