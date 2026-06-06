from typing import Iterator, Any

class TaskQueue:
    def __init__(self) -> None:
        self._queue = []


    def __iter__(self) -> Iterator:
        for task in self._queue:
            yield task 


    def __getitem__(self, index: int) -> Any:
        return self._queue[index]
    

    def __len__(self):
        return len(self._queue)


    def add(self, item: any) -> None:
        self._queue.append(item)


    def filter(self, condition) -> Iterator:
        for task in self._queue:
            if condition(task):
                yield task