# coding: utf-8
from flask import Blueprint, render_template, abort, request, flash, redirect, url_for

from app.models import db
from app.models.student import Student
from app.models.company import Company
from app.models.skill import Skill

from app.blueprints.forms import SkillForm, StudentForm, CompanyForm


import sys

reload(sys)
sys.setdefaultencoding('utf8')


admin = Blueprint(
    "admin", __name__, template_folder="views", url_prefix="/admin")


@admin.route("/")
def admin_main():

    return render_template("admin/main.html")


@admin.route("/student", methods=["GET", "POST"])
@admin.route("/student/<int:student_id>", methods=["GET", "POST"])
def crud_student(student_id=None):

    form = StudentForm()
    skills = db.session.query(Skill).all()
        
        

    if request.method == "GET":
        if not student_id:
            # Agregamos las elecciones de skills al formulario

            return render_template(
                "admin/student.html",
                form=form,
                skills=skills
            )
        else:


            student = db.session.query(Student).get(student_id)
            student_skills = [skill.id for skill in student.skills]

            form.skills.choices = [(skill.id, skill.name) for skill in skills]
            form.skills.data = [
                item[0] for item in form.skills.choices if item[0] in student_skills]
            # Agregamos las opciones de skills al formulario según tiene este
            # estudiante

            form.name.data = student.name
            form.last_name.data = student.last_name
            form.age.data = student.age
            form.email.data = student.email

            return render_template(
                "admin/student.html",
                student_id=student_id,
                form=form
            )
    elif request.method == "POST":

        form = StudentForm()
        form.skills.choices = [(skill.id, skill.name) for skill in skills]

        if form.validate_on_submit():

            if not student_id:
                student = Student()

            else:

                student = db.session.query(Student).get(student_id)
            student.name = form.name.data
            student.last_name = form.last_name.data
            student.age = form.age.data
            student.email = form.email.data

            for skill in student.skills:
                if skill.id not in form.skills.data:
                    student.skills.remove(skill)
            for skill in form.skills.data:

                try:
                    sk = db.session.query(Skill).get(skill)
                    student.skills.append(sk)
                except Exception as e:
                    print e

            try:
                db.session.add(student)
                db.session.commit()
                flash("Alumno agregado correctamente", "success")
                return redirect(url_for("admin.crud_student", student_id=student.id))
            except Exception as e:
                flash(
                    "Hubo un problema al guardar los datos: {}".format(e), "alert")

            return redirect(url_for("admin.crud_student"))

        else:
            flash("El formulario no validó: {}".format(form.errors), "alert")

            if not student_id:
                return render_template(
                    "admin/student.html",
                    form=form
                )
            else:
                return render_template(
                    "admin/student.html",
                    form=form,
                    student_id=student_id
                )

    return render_template("admin/student.html")


@admin.route("/skill/<int:skill_id>", methods=["GET", "POST"])
def crud_skill():
    return render_template("admin/skill.html")


@admin.route("/company/<int:company_id>", methods=["GET", "POST"])
def crud_company():
    return render_template("admin/company.html")
