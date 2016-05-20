from app.models import db


class Skill(db.Model):

	__tablename__ = "skills"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Unicode(50), unique=True)
	description = db.Column(db.UnicodeText)
	# agregar un logo para cada item
	logo = db.Column(db.Unicode(255))
	
	


	def __repr__(self):
		return "{}".format(self.name)