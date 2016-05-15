# coding: utf-8
from flask import Blueprint, render_template, abort

from app.models import db
from app.models.student import Student
from app.models.company import Company

frontend = Blueprint("front", __name__, template_folder="views")


@frontend.route("/")
def index():
    """
    Explains whats going on and shows a list of companies and students
    """
    companies = db.session.query(Company).all()
    students = db.session.query(Student).all()
    return render_template(
        "index.html",
        students=students,
        companies=companies

    )


@frontend.route("/student/<int:student_id>")
def students(student_id):
    """
    student details
    """
    student = db.session.query(Student).get(student_id)
    if not student:
    	abort(500, "Ese estudiante no existe")
    return render_template(
        "student.html",
        student=student
    )

@frontend.route("/company/<int:company_id>")
def companies(company_id):
	"""
	company details
	"""
	company = db.session.query(Company).get(company_id)
	if not company:
		abort(500, "Esa compañia no existe")

	return render_template(
		"company.html",
		company=company
	)
