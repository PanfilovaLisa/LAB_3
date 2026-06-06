import unittest
from src import protocol, handler

class SourceWrong:
    def method(self):
        return 
    

class SourceRight:
    def get_tasks(self):
        return


class TestSource(unittest.TestCase):
    def setUp(self):
        self.sourceWrong = SourceWrong()
        self.sourceRight = SourceRight()


    def test_task_source_protocol(self):
        self.assertNotIsInstance(self.sourceWrong, protocol.TaskSource)
        self.assertIsInstance(self.sourceRight, protocol.TaskSource)


    def test_check_source_handler(self):
        self.assertFalse(handler.check_source(self.sourceWrong))
        self.assertTrue(handler.check_source(self.sourceRight))

