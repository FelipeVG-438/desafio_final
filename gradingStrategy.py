from abc import ABC, abstractmethod

class GradingStrategy(ABC):
    @abstractmethod
    def grade(self, projects, homework, attendance, exam):
        pass

class TypeAStrategy(GradingStrategy):
    def grade(self, projects, homework, attendance, exam):
        return {
            'projects' : 0.3,
            'homework' : 0.3,
            'exam' : 0.4, 
            'grade' : 0.3*projects + 0.3*homework + 0.4*exam
        }

class TypeBGradingStrategy(GradingStrategy):
    def grade(self, projects, homework, attendance, exam):
        return {
            'projects' : 0.2,
            'homework' : 0.3,
            'exam' : 0.5,
            'grade' : 0.2*projects + 0.3*homework + 0.5*exam
        }

class TypeCStrategy(GradingStrategy):
    def grade(self, projects, homework, attendance, exam):
        return {
            'projects' : 0.4,
            'homework' : 0.3,
            'exam' : 0.3,
            'grade' : 0.4*projects + 0.3*homework + 0.3*exam
        }

class TypeDStrategy(GradingStrategy):
    def grade(self, projects, homework, attendance, exam):
        return {
            'projects' : 0.3,
            'homework' : 0.4,
            'exam' : 0.3,
            'grade' : 0.3*projects + 0.4*homework + 0.3*exam
        }

class Grading_manager:
    def __init__(self, grading_strategy):
        self.grading_strategy = grading_strategy
        
    def set_grading_strategy(self, grading_strategy):
        self.grading_strategy = grading_strategy

    def grade(self, projects, homework, attendance, exam):
        return self.grading_strategy.grade(projects, homework, attendance, exam)


if __name__ == "__main__":
    course1 = Grading_manager("Math", StandardGradingStrategy())
    course2 = Grading_manager("Art", ProjectHeavyGradingStrategy())
    course3 = Grading_manager("Science", ExamHeavyGradingStrategy())

    print(f"Math final grade: {course1.calculate_final_grade(85, 90, 95, 80)}")
    print(f"Art final grade: {course2.calculate_final_grade(85, 90, 95, 80)}")
    print(f"Science final grade: {course3.calculate_final_grade(85, 90, 95, 80)}")