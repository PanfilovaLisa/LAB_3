import unittest 
from src.Task import Task
from src.Exceptions import *

class TestTask(unittest.TestCase):
    def setUp(self):
        self.task = Task.Task("TestTask", 1)

    
    def test_status_type(self):
        with self.assertRaises(TypeError):
            self.task.status='e'

    
    def test_status_value(self):
        with self.assertRaises(InvalidStatus):
            self.task.status=10


    def test_priority_type(self):
        with self.assertRaises(TypeError):
            self.task.priority='max'


    def test_priority_value(self):
        with self.assertRaises(InvalidPriorityLevel):
            self.task.priority=10
            

    def test_status_changes(self):
        self.task.status=0
        # Проверяем, что значения начала выполнения и окончания выполнения = 0
        self.assertEqual(self.task.start_time, 0)
        self.assertEqual(self.task.end_time, 0)

        # Проверяем, что время старта изменилось, при принятии задачи в работу
        self.task.status=1
        self.assertNotEqual(self.task.start_time, 0)
        self.assertEqual(self.task.end_time, 0)


        self.task.status=2
        self.assertNotEqual(self.task.start_time, 0)
        self.assertNotEqual(self.task.end_time, 0)
        


