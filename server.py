from flask import Flask, request, jsonify, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from lms import LMS, UserFactory

# Rutas necesarias
# home GET, login, register, teachers

app = Flask(__name__)

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
    return render_template('teacher.html', id=id)

@app.route('/platform/student/<int:id>', methods=['GET'])
def student(id):
    return render_template('student.html', id=id)

@app.route('/platform/admin/<int:id>', methods=['GET'])
def admin(id):
    return render_template('admin.html', id=id)

@app.route('/platform/users', methods=['GET'])
def users():
    return render_template('users.html')


