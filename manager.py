from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


from app import create_app
from app.models import db
from app.models.student import Student 
from app.models.company import Company 
from app.models.skill import Skill 


app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)


manager.add_command("db", MigrateCommand)




@manager.shell
def make_shell_context():
    return dict(
        app=app,
        db=db,
        # add models
        Student=Student,
        Company=Company,
        Skill=Skill
    )




@manager.option("-p", "--populate", default="Populating")
def populate(populate):
	"""
	Populate the database
	"""
	skills = ["Javascript", "HTML", "CSS", "SASS", "PHP", "Python"]
	
	for name in skills:
		skill = Skill(name=name)
		db.session.add(skill)

	student_1 = Student(
		name="Lucia",
		last_name="Cardenas",
		age=18,
		email="lucia.c@gmail.com"
	)
	
	student_2 = Student(
		name="Maria Gracia",
		last_name="Silva",
		age=22,
		email="mg.s@hotmail.com"
	)
	db.session.add_all([student_1, student_2])
	company = Company(
		name="Athelas",
		address="Recavarren esquina con pardo",
		phone="+51961738608",
		website="https://www.athelas.pe"
	)
	db.session.add(company)

	db.session.commit()

	skills = db.session.query(Skill).all()
	company.skills.append(skills[0])
	company.skills.append(skills[1])
	company.skills.append(skills[2])
	company.skills.append(skills[3])

	db.session.commit()

	



	

	





if __name__ == '__main__':
    manager.run()
