from flask_admin.contrib.sqla import ModelView


class AdminStudentView(ModelView):

    """Vista que permite realizar operaciones CRUD sobre el modelo Student"""
    
    column_list = ("name", "last_name", "age", "email", "skills")



class AdminCompanyView(ModelView):
    """Vista que permite realizar operaciones CRUD sobre el modelo Company"""
    column_list = ("name", "address", "phone", "website", "skills")

class AdminSkillView(ModelView):
    """Vista que permite realizar operaciones CRUD sobre el modelo Skill"""

    column_list = ("name", "description", "logo")
