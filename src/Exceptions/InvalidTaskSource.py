class InvalidTaskSource(Exception):
    def __init__(self, source):
        self.source = source

    def __str__(self):
        return f"Источник {self.source} не является доупстимым источником задач."