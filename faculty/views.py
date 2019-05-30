from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from account import models as acc_models
from . import forms
from . import models

@login_required
def add_faculty(request):

	admin_all = [u['user'] for u in acc_models.AdminUser.objects.all().values('user')]
	frontend_all = [u['user'] for u in acc_models.FrontEndUser.objects.all().values('user')]
	if request.user.pk in admin_all or request.user.pk in frontend_all:
		if request.method == 'POST':
			form = forms.FacultyForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				return redirect('success', success='Faculty added successfully')
			else:
				return redirect('fault', fault='Server Error')
		else:

			form = forms.FacultyForm()
			return render(request, 'faculty/add-faculty.html', {'form':form})

	else:
		return redirect('fault', fault='ACCESS DENIED!')


def view_faculties(request):

	faculties = models.Faculty.objects.all()
	return render(request, 'faculty/view-faculties.html', {'faculties': faculties})



@login_required
def delete_faculty(request, pk):

	admin_all = [u['user'] for u in acc_models.AdminUser.objects.all().values('user')]
	frontend_all = [u['user'] for u in acc_models.FrontEndUser.objects.all().values('user')]
	if request.user.pk in admin_all or request.user.pk in frontend_all:
		try:
			models.Faculty.objects.get(pk__exact=pk).delete()
			return redirect('faculty:view_faculties')
		except:
			return redirect('fault', fault="Server Error")
	else:
		return redirect('fault', fault='ACCESS DENIED!')


@login_required
def edit_faculty(request, pk):
	admin_all = [u['user'] for u in acc_models.AdminUser.objects.all().values('user')]
	frontend_all = [u['user'] for u in acc_models.FrontEndUser.objects.all().values('user')]
	if request.user.pk in admin_all or request.user.pk in frontend_all:
		if request.method == 'POST':
			form = forms.EditFacultyForm(data=request.POST, files=request.FILES, pk=pk)
			if form.is_valid():
				faculty = models.Faculty.objects.get(pk__exact=pk)
				faculty.name = form.cleaned_data['name']
				faculty.designation = form.cleaned_data['designation']
				faculty.contact_num = form.cleaned_data['contact_num']
				faculty.qualification1 = form.cleaned_data['qualification1']
				faculty.qualification2 = form.cleaned_data['qualification2']
				faculty.qualification3 = form.cleaned_data['qualification3']
				faculty.field_of_interest = form.cleaned_data['field_of_interest']
				faculty.experience = form.cleaned_data['experience']
				faculty.pic = form.cleaned_data['pic']
				try:
					faculty.save()
				except:
					return redirect('fault', fault='Server Error')
				return redirect('success', success='Faculty data edited successfully')
		else:
			form = forms.EditFacultyForm(pk=pk)
			return render(request, 'faculty/add-faculty.html', {'form':form})
	else:
		return redirect('fault', fault='ACCESS DENIED!')