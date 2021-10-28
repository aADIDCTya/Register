from django.forms import ModelForm, fields
from .models import Form


class StudentForm(ModelForm):
    class Meta:
        model = Form
        fields =('Student_Name','College_Name','Specialization','Degree_Name','Phone_No','Email_id','Intern','City','Gender')