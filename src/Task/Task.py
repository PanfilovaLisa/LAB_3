import time
from .Descriptors import *
from src.Exceptions import *

class Task:
    """
    Класс задачи. Содержит атрибуты:
        id: int - автоматически возрастает с каждой задачей;
        payload: src - описание задачи;
        priority: int - приоритет задачи. Принимает значение от 1 (самый низкий приоритет) до 3 (самый высокий приоритет)
        status: int - статус выполнения задачи. Принимает значения  0 (NotStarted), 1 (InWork), 2 (Finished).
            При создании задачи, статус принимает значение 0.
        make_time: float - время созддания задачи;
        make_time_local: str - время создания задачи в локальном виде и строчной записи.
        properties: 
            start_time: float - время, когда было начато выполнение задачи. Вычислится автоматически, при изменении статуса задачи с NotStarted на InWork.
            end_time: float - время выполнения задачи. Вычисляется автоматически, при изменениия статуса задачи с InWork на Finished.
            duration - продолжительность выполнения задачи. Вычисляемое значение
    Связь status с start_time, end_time:
        value - некоторое значение времени

        status=0 (NotStarted):
            start_time=0
            end_time=0
        status=1 (InWork):
            start_time = value
            end_time = 0
        status=2 (Finished):
            start_time = value
            end_time = value

    """
    id_count = 0
    states=["NotStarted", "InWork", "Finished"]
    priority_min = 1
    priority_max = 3
    
    id=TaskIdDescription()
    priority = PriorityDescriptor(min=priority_min, max=priority_max)

    def __init__(self, payload: any, priority_level: int):
        Task.id_count+=1
        self._id = Task.id_count
        self.payload = payload

        self.priority = priority_level
        self._status = 0 #Атрибут приватный, чтобы проще отслеживать вводимые значения статуса
        self.__make_time = time.time() #Приватный, потому изменить его нельзя, назначится автоматом 

        self.__start_time = 0
        self.__end_time = 0


    @property
    def status(self) -> str:
        return self.states[self._status]
    

    @status.setter
    def status(self, new_status) -> None:
        """
        Изменнение статуса выполнения задачи.
        Изменение статуса вдияет на атрибуты Task.start_time и Task.end_time
        """
        # Check new_status is int
        try:
            new_status=int(new_status)
        except:
            note = f"Было передано значение типа {type(new_status)}. Необходимо: int."
            exception = TypeError()
            exception.add_note(note)
            raise exception

        if new_status==self._status:
            return

        match new_status:
            # Change status to "InWork"
            case 1:
                match self._status:
                    # From "NotStarted" to "InWork"
                    case 0:
                        self.__start_time=time.time()
                    # From "Finished" to "InWork"
                    case 2:
                        self.__end_time=0
            # Change status to "Finished"
            case 2:
                self.__end_time=time.time()
                # From "Not started" to "Finished"
                if self._status==0:
                    self.__start_time=self.__end_time
            # Change to "NotStarted"
            case 0:
                self.__start_time=0 
                self.__end_time=0
            case _:
                raise InvalidStatus(new_status)
        self._status=new_status
        return
    

    @property 
    def start_time(self) -> str:
        if self.__start_time!=0:
            start_time_local = time.localtime(self.__start_time)
            return time.strftime("%a, %d %b %Y, %H:%M:%S", start_time_local)
        return 0 
    

    @property 
    def end_time(self) -> str:
        if self.__end_time!=0:
            end_time_local = time.localtime(self.__end_time)
            return time.strftime("%a, %d %b %Y, %H:%M:%S", end_time_local)
        return 0


    @property
    def make_time(self) -> str:
        make_time_local = time.localtime(self.__make_time)
        return time.strftime("%a, %d %b %Y, %H:%M:%S", make_time_local)
    

    @property 
    def duration(self) -> tuple:
        """
        Вычисление продолжительности выполнения задачи.
        Возвращает кортеж целых чисел:   (hours, minutes, seconds)
        """
        if self.__start_time==0 or self.__end_time==0:
            return 0
        
        duration_time = int(self.__end_time - self.__start_time)
        minutes = duration_time//60
        secs = duration_time%60
        hours = minutes//60 
        minutes%=60
        return (hours, minutes, secs)