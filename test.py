import unittest
from lms import Teacher, LMS

class TestTask_Teacher(unittest.TestCase):
    def setUp(self):
        self.lms = LMS()
        for user in self.lms.users_data:
            if user['name'] == 'teacher':
                self.teacher = user['name']
                break
        self.tasks = self.lms.get_tasks()

    def test_get_teacher_tasks(self):
        count = 0
        for task in self.tasks:
            if task['teacher'] == self.teacher:
                count += 1
                
        self.assertEqual(count, len(self.lms.get_teacher_tasks(self.teacher)))
            
if __name__ == '__main__':
    unittest.main()