from app.models import db
from app.models.relationships import company_skills


class Company(db.Model):

	__tablename__ = "companies"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Unicode(100), unique=True)
	address = db.Column(db.Unicode(255))
	phone = db.Column(db.Unicode(50))
	website = db.Column(db.Unicode(255), unique=True)
	site = db.Column(db.Unicode(255))
	skills = db.relationship("Skill", secondary=company_skills,
									backref=db.backref("companies", lazy="dynamic"))


	def __repr__(self):
		return u"{} - {}".format(self.name, self.address)

