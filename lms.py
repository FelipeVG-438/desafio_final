from abc import ABC, abstractmethod
import bcrypt

users = {
    'admin': {'password': bcrypt.hashpw(b'admin123', bcrypt.gensalt()), 'role': 'admin'},
    'teacher': {'password': bcrypt.hashpw(b'teacher123', bcrypt.gensalt()), 'role': 'teacher'},
    'student': {'password': bcrypt.hashpw(b'student123', bcrypt.gensalt()), 'role': 'student'}
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
        users[username] = {'password' : bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()), 'role' : 'student'}
        
    def permitions(self):
        return "Student permissions"

class Teacher(Users):
    def __init__(self, username, password):
        super().__init__(username, password)
        users[username] = {'password' : bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()), 'role' : 'teacher'}
        
    def permitions(self):
        return "Teacher permissions"
    
class Admin(Users):
    def __init__(self, username, password):
        super().__init__(username, password)
        users[username] = {'password' : bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()), 'role' : 'admin'}
        
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
            raise ValueError('Rol no valido')

# Singleton
class LMS:
    _instance = None
    _tasks = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LMS, cls).__new__(cls)
        return cls._instance
    
    def add_task(self, task):
        self._tasks.append(task)
        
    def get_tasks(self):
        return self._tasks

user_factory = UserFactory()
admin = user_factory.create_user('Juan', 'admin_pass', 'admin')
teacher = user_factory.create_user('Pedro', 'teacher_pass', 'teacher')
student = user_factory.create_user('Luis', 'student_pass', 'user')

print(users)