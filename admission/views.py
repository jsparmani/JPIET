from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from account import models as acc_models

from. import models
from. import forms

# Create your views here.

@login_required
def add_application(request):

	admin_all = [u['user'] for u in acc_models.AdminUser.objects.all().values('user')]
	frontend_all = [u['user'] for u in acc_models.FrontEndUser.objects.all().values('user')]
	if request.user.pk in admin_all or request.user.pk in frontend_all:
		if request.method == 'POST':
			form = forms.ApplicationForm(request.POST, request.FILES)
			if form.is_valid():
				application = form.save()
				models.ApplicationNumber.objects.create(application=application, application_no=int(str(form.cleaned_data['year']) + '00000'))

				return redirect('success', success='Application created successfully')
			else:
				return redirect('fault', fault='Server Error')
		else:

			form = forms.ApplicationForm()
			return render(request, 'admission/add-application.html', {'form':form})

	else:
		return redirect('fault', fault='ACCESS DENIED!')




def view_application(request):

	application_list = models.Application.objects.all().filter(is_active__exact=True)
	return render(request, 'admission/view-application.html', {'application_list':application_list} )



def add_candidate(request, pk):

	if request.method == 'POST':
		form = forms.CandidateForm(data=request.POST, files=request.FILES, pk=pk)
		if form.is_valid():
			try:
				candidate = form.save(commit=False)
				candidate.application = models.Application.objects.get(pk__exact=pk)
				application_no_obj = models.ApplicationNumber.objects.get(application__pk__exact=pk)
				candidate.application_no = application_no_obj.application_no + 1
				application_no_obj.application_no  = application_no_obj.application_no + 1					
				candidate.save()
				application_no_obj.save()
				send_mail("JPIET | Application Registered",f'Dear {candidate.name}, Your application is registered with JPIET. The application number for the same is {candidate.application_no}','jpietuniversity@gmail.com',[candidate.email],fail_silently = True)
			except:
				if form.cleaned_data['aadhar'] in [u['aadhar'] for u in models.Candidate.objects.all().values('aadhar')] :
					return redirect('fault', fault='Entered AADHAR number is already registered')
				else:
					return redirect('fault', fault='Server Error')


			return redirect('success', success='Candidate created successfully')
		else:
			if int(request.POST['aadhar']) in [u['aadhar'] for u in models.Candidate.objects.all().values('aadhar')] :
				return redirect('fault', fault='Entered AADHAR number is already registered')
			else:
				return redirect('fault', fault='Server Error')
	else:

		form = forms.CandidateForm(pk=pk)
		return render(request, 'admission/add-candidate.html', {'form':form})



def view_candidate(request, pk):

	admin_all = [u['user'] for u in acc_models.AdminUser.objects.all().values('user')]
	frontend_all = [u['user'] for u in acc_models.FrontEndUser.objects.all().values('user')]
	if request.user.pk in admin_all or request.user.pk in frontend_all:
		candidate_list = models.Candidate.objects.all().filter(application__pk__exact=pk)
		return render(request, 'admission/view-candidate.html', {'candidate_list':candidate_list})
	else:
		return redirect('fault', fault='ACCESS DENIED!')

