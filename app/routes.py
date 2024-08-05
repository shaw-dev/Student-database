# routes.py
from flask import render_template, redirect, url_for, request, flash
from .main import main
from . import db
from .models import Student
from .forms import StudentForm

@main.route('/add_student', methods=['GET', 'POST'])
def add_student():
    form = StudentForm()
    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data
        major = form.major.data
        
        new_student = Student(name=name, age=age, major=major)
        db.session.add(new_student)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            flash(f"Error: {e}", "danger")
        
        return redirect(url_for('main.index'))
    
    return render_template('add_student.html', form=form)

@main.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

@main.route('/delete_student/<int:id>', methods=['POST'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    try:
        db.session.delete(student)
        db.session.commit()
        flash(f"Student {student.name} deleted successfully!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Error: {e}", "danger")
    return redirect(url_for('main.index'))
