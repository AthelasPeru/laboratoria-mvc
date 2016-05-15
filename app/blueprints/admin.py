from flask_admin.contrib.sqla import ModelView

class AdminStudentView(ModelView):

    column_list = ("name", "last_name", "age", "email", "skills")



class AdminCompanyView(ModelView):

    column_list = ("name", "address", "phone", "website", "skills")