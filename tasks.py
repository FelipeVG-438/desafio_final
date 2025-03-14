from abc import ABC, abstractmethod
import bcrypt
from lms import *

# Observer 

class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

class Subject(ABC):
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

#  Observador Concreto

class Notificator(Observer):
    def update(self, message):
        print(f"Notification: {message}")


class UserFactory(Subject):
    def __init__(self):
        super().__init__()

    def create_user(self, username, password, role):
        if role == 'admin':
            user = Admin(username, password)
        elif role == 'teacher':
            user = Teacher(username, password)
        elif role == 'user':
            user = Student(username, password)
        else:
            raise ValueError('Invalid role.')
        
        self.notify(f"A new user was created: {username} with rol {role}")
        return user

# Singleton LMS extendido con Observer

class LMS(Subject):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LMS, cls).__new__(cls)
            cls._instance._tasks = []
            cls._instance._observers = []  # importante para Subject
        return cls._instance
    
    def add_task(self, task):
        self._tasks.append(task)
        self.notify(f"A new task was added: {task}")
        
    def get_tasks(self):
        return self._tasks

# Crear notificador
notificator = Notificator()

# Crear UserFactory y LMS con observadores
user_factory = UserFactory()
user_factory.attach(notificator)

lms = LMS()
lms.attach(notificator)

# Agregar tareas
lms.add_task(f"Submit assignment 1 for {student.username}")
lms.add_task(f"Read chapter 5 of History book for {teacher.username}")

