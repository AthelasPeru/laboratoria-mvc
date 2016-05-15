from flask import Flask
from flask_zurb_foundation import Foundation

from blueprints.frontend import frontend
from blueprints.admin import admin


def create_app(app=None, config_file=None):

    if not app:
        app = Flask(__name__, template_folder="views")

    # Config files
    app.config.from_pyfile("config/base.py")
    if config_file:
    	app.config.from_pyfile("config/{}.py".format(config_file))

    # Blueprints
    app.register_blueprint(frontend)
    app.register_blueprint(admin)

    # Extensions
    Foundation(app)

    return app
