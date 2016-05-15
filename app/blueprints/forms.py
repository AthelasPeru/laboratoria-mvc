# coding: utf-8
from flask_wtf import Form
from wtforms import TextField, TextAreaField, SelectMultipleField, widgets
from flask_wtf.html5 import IntegerField, EmailField, URLField
from wtforms.validators import Required, Optional, NumberRange, Length


class MultiCheckboxField(SelectMultipleField):

    """Base for Multicheckbox forms"""

    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class StudentForm(Form):

    """Formulario de estudiante"""

    name = TextField(
        "Nombre", validators=[Required("Debes agregar un nombre al formulario")])
    last_name = TextField(
        "Apellido", validators=[Required("Debes agregar un apellido al formulario")])
    age = IntegerField(
        "Edad", validators=[Required("Debes agregar la edad al formulario")])
    email = EmailField(
        "Email", validators=[Required("Debes agregar la edad al formulario")])
    skills = MultiCheckboxField(
        "Habilidades Requeridas",
        coerce=int
    )


class SkillForm(Form):

    """Formulario de skill"""

    name = TextField(
        "Nombre", validators=[Required("Debes agregar un nombre al formulario")])
    description = TextAreaField("Decripción", validators=[Optional])


class CompanyForm(Form):

    """Formulario de company"""

    name = TextField(
        "Nombre", validators=[Required("Debes agregar un nombre al formulario")])
    address = TextField(
        "Dirección", validators=[Required("Debes agregar una dirección")])
    phone = TextField("Teléfono", validators=[Optional])
    website = URLField("Dirección web", validators=[Required("Debes ingresar la web de la compañía")])
    skills = MultiCheckboxField(
        "Habilidades",
        coerce=unicode
    )
