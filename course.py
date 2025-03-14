from gradingStrategy import Grading_manager, TypeAStrategy
from lms import LMS

class Course:
    def __init__(self, name, teacher, grading_strategy=TypeAStrategy()):
        self.lms = LMS()
        self.name = name
        self.teacher = teacher
        self.students = []
        self.grading_manager = Grading_manager(grading_strategy)
        
    def add_student(self, student):
        student = [user for user in self.lms._users.values() if user['name'] == student]
        if student is None:
            raise ValueError("Student not found")
        self.students.append(student)
        print(f'Student {student[0]['name']} added to course {self.name}')

    def set_grading_strategy(self, grading_strategy):
        self.grading_manager.set_grading_strategy(grading_strategy)
        
    def grade_student(self, student, projects, homework, attendance, exam):
        pass
        
course = Course("Math", "Mr. Smith")
# Example usage:
course.add_student("student")
# grade = course.grade_student("student", 90, 85, 0, 95)