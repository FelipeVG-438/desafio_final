'''
File containing the testing script for LMS system
Checks what is supposedly the amount of tasks assigned to a teacher
and compares it with the amount of tasks returned by the get_teacher_tasks method
'''

import unittest
from lms import LMS

class TestTask_Teacher(unittest.TestCase):
    def setUp(self): # Initialize the LMS and get the teacher name
        self.lms = LMS()
        for user in self.lms._users.values():
            if user['role'] == 'teacher':
                self.teacher = user['name']
                break
        self.tasks = self.lms.get_tasks()

    def test_get_teacher_tasks(self): #Test class
        count = count = sum(1 for task in self.tasks.values() if task['teacher'] == self.teacher) #Count the amount of tasks assigned to the teacher
        self.assertEqual(count, len(self.lms.get_teacher_tasks(self.teacher))) #Compare the amount of tasks assigned to the teacher with the amount of tasks returned by the get_teacher_tasks method
            
if __name__ == '__main__':
    unittest.main()