from app.models import db
from app.models.relationships import student_skills
from app.models.company import Company
from app.models.skill import Skill


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

    @property
    def _student_skills_as_set(self):
        """
        returns student skills as set to work with it
        """
        return set([skill.id for skill in self.skills])

    def matching_companies(self):
        """
        Returns a list of matching companiesordered by relevance
        """
        student_skills = self._student_skills_as_set

        companies = db.session.query(Company).all()
        print companies
        matching_companies = []
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
        return sorted_matching_companies


