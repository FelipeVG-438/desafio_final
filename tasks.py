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

class Notificator(Observer):
    def update(self, message):
        print(f"Notification: {message}")



# Factory + Observer 
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

        self.notify(f"New user created: {username} with role {role}")
        return user

# LMS Singleton + Observer
class LMS(Subject):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LMS, cls).__new__(cls)
            cls._instance._tasks = {}
            cls._instance._observers = []
        return cls._instance

    def add_task(self, name, description='', teacher='', due_date=''):
        task_id = len(self._tasks) + 1
        self._tasks[task_id] = {
            'name': name,
            'description': description,
            'teacher': teacher,
            'due_date': due_date
        }
        self.notify(f"New task added: '{name}' assigned by {teacher}")

    def get_tasks(self):
        return self._tasks

    def get_teacher_tasks(self, teacher):
        teacher_tasks = [task for task in self._tasks.values() if task['teacher'] == teacher]
        if not teacher_tasks:
            return {'error': 'No tasks found for this teacher'}
        return teacher_tasks

# Uso del sistema 
notificator = Notificator()

user_factory = UserFactory()
user_factory.attach(notificator)

lms = LMS()
lms.attach(notificator)

# Crear usuarios
admin = user_factory.create_user('Juan', 'admin_pass', 'admin')
teacher = user_factory.create_user('Pedro', 'teacher_pass', 'teacher')
student = user_factory.create_user('Luis', 'student_pass', 'user')

# Agregar tareas
lms.add_task('Task 1', 'Description of task 1', 'Pedro', '2023-12-31')
lms.add_task('Task 2', 'Description of task 2', 'Juan', '2023-12-31')

# Mostrar tareas y usuarios
print("\nAll tasks:")
print(lms.get_tasks())

print("\nAll users:")
print(users_data)
