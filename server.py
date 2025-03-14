from flask import Flask, request, jsonify, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from lms import LMS, UserFactory, users_data

# Rutas necesarias
# home GET, login, register, teachers

app = Flask(__name__)
lms = LMS()

@app.route('/', methods=['GET'])
def index():
    # Mandar a /home cuando se accede a la raiz
    return redirect('/home')

@app.route('/platform/home', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/platform/teacher/<int:id>', methods=['GET'])
def teacher(id):
    teacher = users_data.get(id)
    if not teacher:
        return jsonify({'error': 'User not found'}), 404
    return render_template('teacher.html', id=id)

@app.route('/platform/student/<int:id>', methods=['GET'])
def student(id):
    student = users_data.get(id)
    if not student:
        return jsonify({'error': 'User not found'}), 404
    return render_template('student.html', id=id)

@app.route('/platform/admin/<int:id>', methods=['GET'])
def admin(id):
    admin = users_data.get(id)
    if not admin:
        return jsonify({'error': 'User not found'}), 404
    return render_template('admin.html', id=id)

@app.route('/platform/users', methods=['GET'])
def users():
    users = users_data.values()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)  # Cambiar a False en producción

