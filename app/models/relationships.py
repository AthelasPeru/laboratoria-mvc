from app.models import db

company_skills = db.Table("company_skills",
	db.Column("company_id", db.Integer, db.ForeignKey("companies.id")),
	db.Column("skills_id", db.Integer, db.ForeignKey("skills.id"))
)


student_skills = db.Table("student_skills",
	db.Column("student_id", db.Integer, db.ForeignKey("students.id")),
	db.Column("skills_id", db.Integer, db.ForeignKey("skills.id"))
)