# coding: utf-8
from flask import Blueprint, render_template, abort

from app.models import db
from app.models.student import Student
from app.models.company import Company
from app.models.skill import Skill

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

    matching_companies = []
    student_skills = set([skill.id for skill in student.skills])
    companies = db.session.query(Company).all()

    for company in companies:

        company_skills = set([skill.id for skill in company.skills])
        match_skills = [skill for skill in student_skills & company_skills]
        other_skills = [skill for skill in company_skills - student_skills]
        if len(match_skills) > 0:

            # Model lists
            match_skills_obj = [
                db.session.query(Skill).get(skill) for skill in match_skills]
            other_skills_obj = [
                db.session.query(Skill).get(skill) for skill in other_skills]

            match = {
                "model": company,
                "matches": len(match_skills),
                "skills": match_skills_obj,
                "other_skills": other_skills_obj
            }
            matching_companies.append(match)

        # sort the list by matches, most matches first
        from operator import itemgetter
        sorted_matching_companies = sorted(matching_companies,
                                           key=itemgetter('matches'),
                                           reverse=True)

    return render_template(
        "student.html",
        student=student,
        matching_companies=sorted_matching_companies
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
