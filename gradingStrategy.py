'''
This file contains the necessary classes and methods to impement different grading options for teachers
Teachers can change the grading criteria used when getting a student's grade
Used strategy design pattern
'''

from abc import ABC, abstractmethod

class GradingStrategy(ABC): #Main abstract class
    @abstractmethod
    def grade(self, projects, homework, attendance, exam):
        pass

class TypeAStrategy(GradingStrategy): #Type A grading criteria
    def grade(self, projects, homework, attendance, exam):
        return {
            'projects' : projects,
            'homework' : homework,
            'exam' : exam,
            'project-criteria' : 0.3,
            'homework-criteria' : 0.3,
            'attendance-criteria' : 0,
            'exam-criteria' : 0.4,
            'grade' : 0.3*projects + 0.3*homework + 0.4*exam
        }

class TypeBStrategy(GradingStrategy): #Type B grading criteria
    def grade(self, projects, homework, attendance, exam):
        return {
            'projects' : projects,
            'homework' : homework,
            'exam' : exam,
            'project-criteria' : 0.2,
            'homework-criteria' : 0.3,
            'attendance-criteria' : 0,
            'exam-criteria' : 0.5,
            'grade' : 0.2*projects + 0.3*homework + 0.5*exam
        }

class TypeCStrategy(GradingStrategy): #Type C grading criteria
    def grade(self, projects, homework, attendance, exam):
        return {
            'projects' : projects,
            'homework' : homework,
            'exam' : exam,
            'project-criteria' : 0.4,
            'homework-criteria' : 0.3,
            'attendance-criteria' : 0,
            'exam-criteria' : 0.3,
            'grade' : 0.4*projects + 0.3*homework + 0.3*exam
        }

class TypeDStrategy(GradingStrategy): #Type D grading criteria
    def grade(self, projects, homework, attendance, exam):
        return {
            'projects' : projects,
            'homework' : homework,
            'exam' : exam,
            'project-criteria' : 0.3,
            'homework-criteria' : 0.4,
            'attendance-criteria' : 0.1,
            'exam-criteria' : 0.3,
            'grade' : 0.3*projects + 0.4*homework + 0.1*attendance + 0.3*exam
        }

class Grading_manager: #Grading manager class to change the current strategy and call the grade method
    def __init__(self, grading_strategy):
        self.grading_strategy = grading_strategy
        
    def set_grading_strategy(self, grading_strategy):
        self.grading_strategy = grading_strategy

    def grade(self, projects, homework, attendance, exam):
        return self.grading_strategy.grade(projects, homework, attendance, exam)
    
if __name__ == '__main__': #Test cases
    grading_manager = Grading_manager(TypeAStrategy())
    print(grading_manager.grade(80, 90, 100, 70))
    grading_manager.set_grading_strategy(TypeBStrategy())
    print(grading_manager.grade(80, 90, 100, 70))
    grading_manager.set_grading_strategy(TypeCStrategy())
    print(grading_manager.grade(80, 90, 100, 70))
    grading_manager.set_grading_strategy(TypeDStrategy())
    print(grading_manager.grade(80, 90, 100, 70))