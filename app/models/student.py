from app.models import db
from app.models.relationships import student_skills


class Student(db.Model):

	__tablename__ = "students"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Unicode(255))
	last_name = db.Column(db.Unicode(255))
	age = db.Column(db.Integer)
	email = db.Column(db.Unicode(50), unique=True)

	skills = db.relationship("Skill", secondary=student_skills,
									backref=db.backref("students", lazy="dynamic"))


	def __repr__(self):
		return "{}, {}".format(self.name, self.email)