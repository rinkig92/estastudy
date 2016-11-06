from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student
from django.core.urlresolvers import reverse_lazy



### Home Page ###
def home(request):
	context = {
			'title' : "Home Page"
	}
	return render(request, "home.html", context)

def insert(request):
	if request.method == 'POST':
		form = StudentForm(request.POST or None)
		if form.is_valid():
			#sid = request.POST.get('s_id')
			sname = request.POST.get('s_name')
			sdob = request.POST.get('s_dob')
			semail = request.POST.get('s_email')
			smobile = request.POST.get('s_mobile')
			saddress = request.POST.get('s_address')
			instance = form.save(commit=True)
			print form.cleaned_data.get("s_name")
			instance.save()
			return render(request, "view.html", {})
		else:
			print form.errors
	else:		
		form = StudentForm()
	return render(request, "insert.html", {'form':form})


def update(request, pk=None):
	student = get_object_or_404(Student, pk=pk)
	form = StudentForm(request.POST or None, instance=student)
	if form.is_valid():
		form.save()
		return redirect('view')
	return render(request, "update.html", {'form':form})


def delete(request):
	context = {
			'title': "Delete Page"
	}
	return render(request, "delete.html", context)


def view(request):
	queryset = Student.objects.all()
	context = {
				'title': "View Page",
				 'queryset': queryset
		}
	return render(request, "view.html", context)
