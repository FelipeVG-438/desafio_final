from gradingStrategy import Grading_manager, TypeAStrategy
from lms import LMS

class Course:
    def __init__(self, name, teacher, grading_strategy=TypeAStrategy()):
        # Use the singleton instance of LMS
        self.lms = LMS()
        # Initialize course attributes
        self.name = name
        self.teacher = teacher
        self.students = []
        # Initialize grading manager with the default grading strategy
        self.grading_manager = Grading_manager(grading_strategy)
        
    # Add a student to the course
    def add_student(self, student):
        # Check if the student exists in the LMS
        student = [user for user in self.lms._users.values() if user['name'] == student]
        if student is None:
            raise ValueError("Student not found") # Error message
        # Add the student to the course
        self.students.append(student[0]['name'])
        print(f'Student {student[0]['name']} added to course {self.name}')

    # Set a new grading strategy
    def set_grading_strategy(self, grading_strategy):
        # Set the new grading strategy in the grading manager
        self.grading_manager.set_grading_strategy(grading_strategy)
    
    # Grade a student based on the grading strategy
    def grade_student(self, student, projects, homework, attendance, exam):
        # Check if the student is enrolled in the course
        if student in self.students:
            # Return the grade using the grading manager
            return self.grading_manager.grade(projects, homework, attendance, exam)
        else:
            raise ValueError("Student not enrolled in this course") # Message error
        
# Example usage:
if __name__ == '__main__':    
    course = Course("Math", "Mr. Smith")
    course.add_student("student")
    print(course.students)
    print(course.grade_student("student", 90, 85, 0, 95))