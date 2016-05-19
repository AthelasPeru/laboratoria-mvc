from flask import Flask
from flask_zurb_foundation import Foundation
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView




from app.models import db
from app.models.student import Student
from app.models.skill import Skill
from app.models.company import Company

from blueprints.frontend import frontend
from blueprints.admin import AdminStudentView, AdminCompanyView, AdminSkillView



def create_app(app=None, config_file=None):

    if not app:
        app = Flask(__name__, template_folder="views")

    # Config files
    app.config.from_pyfile("config/base.py")
    if config_file:
    	app.config.from_pyfile("config/{}.py".format(config_file))

    # Extensions
    Foundation(app)
    admin = Admin(app, name='Bolsa de Trabajo', template_mode='bootstrap3')

    """
    CONTROLADORES 
    """
    # Blueprints
    app.register_blueprint(frontend)    

    # Admin Views
    admin.add_view(AdminSkillView(Skill, db.session))
    admin.add_view(AdminStudentView(Student, db.session))
    admin.add_view(AdminCompanyView(Company, db.session))

    return app
