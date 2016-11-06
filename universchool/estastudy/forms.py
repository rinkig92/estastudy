from django import forms
from .models import Student, Registration, Teacher, Course

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = [
			"s_id",
			"s_name",
			"s_dob",
			"s_email",
			"s_mobile",
			"s_address"
		]