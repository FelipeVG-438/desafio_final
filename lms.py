from abc import ABC, abstractmethod
import bcrypt

users_data = {
    '1': {'name': 'admin', 'password': bcrypt.hashpw(b'admin123', bcrypt.gensalt()), 'role': 'admin'},
    '2': {'name': 'teacher', 'password': bcrypt.hashpw(b'teacher123', bcrypt.gensalt()), 'role': 'teacher'},
    '3': {'name': 'student', 'password': bcrypt.hashpw(b'student123', bcrypt.gensalt()), 'role': 'student'}
}

# Factory
class Users(ABC):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    @abstractmethod
    def permitions(self):
        pass

class Student(Users):
    def __init__(self, username, password):
        super().__init__(username, password)
        users_data[len(users_data) + 1] = {'name':username, 'password': bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()), 'role' : 'student'}
        
    def permitions(self):
        return "Student permissions"

class Teacher(Users):
    def __init__(self, username, password):
        super().__init__(username, password)
        users_data[len(users_data) + 1] = {'name':username, 'password': bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()), 'role' : 'teacher'}
        
    def permitions(self):
        return "Teacher permissions"
    
class Admin(Users):
    def __init__(self, username, password):
        super().__init__(username, password)
        users_data[len(users_data) + 1] = {'name':username, 'password': bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()), 'role' : 'admin'}
        
    def permitions(self):
        return "Admin permissions"
        
class UserFactory:
    valid_roles = ['admin', 'teacher', 'user']
    
    @staticmethod
    def create_user(username, password, role):
        if role == 'admin':
            return Admin(username, password)
        elif role == 'teacher':
            return Teacher(username, password)
        elif role == 'user':
            return Student(username, password)
        else:
            raise ValueError('Invalid role')

# Singleton
class LMS:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LMS, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, '_tasks'):
            self._tasks = {}
            self._users = users_data
        
    def add_task(self, name, description='', teacher='', due_date=''):
        task_id = len(self._tasks) + 1
        self._tasks[task_id] = {'name': name, 'description': description, 'teacher': teacher, 'due_date': due_date}
        
    def get_tasks(self):
        return self._tasks
    
    def get_teacher_tasks(self, teacher):
        teacher_tasks = [task for task in self._tasks.values() if task['teacher'] == teacher]
        if not teacher_tasks:
            return {'error': 'No tasks found for this teacher'}
        return teacher_tasks

# Pruebas
user_factory = UserFactory()
admin = user_factory.create_user('Juan', 'admin_pass', 'admin')
teacher = user_factory.create_user('Pedro', 'teacher_pass', 'teacher')
student = user_factory.create_user('Luis', 'student_pass', 'user')

lms = LMS()
lms.add_task('Task 1', 'Description of task 1', 'Pedro', '2023-12-31')

lms2 = LMS()
lms2.add_task('Task 2', 'Description of task 2', 'Juan', '2023-12-31')

print(lms.get_tasks())

print(users_data)