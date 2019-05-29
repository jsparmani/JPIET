from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from account import models as acc_models
from . import forms
from . import models
# Create your views here.

@login_required
def change_home_image(request):

	admin_all = [u['user'] for u in acc_models.AdminUser.objects.all().values('user')]
	frontend_all = [u['user'] for u in acc_models.FrontEndUser.objects.all().values('user')]
	if request.user.pk in admin_all or request.user.pk in frontend_all:
		if request.method == 'POST':
			form = forms.HomeImageForm(request.POST, request.FILES)
			if form.is_valid():
				home = models.HomeImage.objects.get(uid__exact=1)
				home.logo_image = form.cleaned_data['logo_image']
				home.carousel_image1 = form.cleaned_data['carousel_image1']
				home.carousel_image2 = form.cleaned_data['carousel_image2']
				home.carousel_image3 = form.cleaned_data['carousel_image3']
				home.carousel_image4 = form.cleaned_data['carousel_image4']
				home.side_image = form.cleaned_data['side_image']
				try:
					home.save()
				except:
					return redirect('fault', fault = 'Server Error')
				return redirect('success', success = 'Changes completed successfully')
			else:
				return redirect('fault', fault='Server Error')
		else:
			form = forms.HomeImageForm()
			return render(request, 'frontend/change-home-image.html', {'form':form})
	else:
		return redirect('fault', fault='ACCESS DENIED!')





@login_required
def change_stats(request):

	admin_all = [u['user'] for u in acc_models.AdminUser.objects.all().values('user')]
	frontend_all = [u['user'] for u in acc_models.FrontEndUser.objects.all().values('user')]
	if request.user.pk in admin_all or request.user.pk in frontend_all:
		if request.method == 'POST':
			form = forms.StatisticsForm(request.POST, request.FILES)
			if form.is_valid():
				stat = models.Statistics.objects.get(uid__exact=1)
				stat.students = form.cleaned_data['students']
				stat.area = form.cleaned_data['area']
				stat.alumni = form.cleaned_data['alumni']
				stat.recruiters = form.cleaned_data['recruiters']
				stat.students_placed = form.cleaned_data['students_placed']
				stat.years = form.cleaned_data['years']
				try:
					stat.save()
				except:
					return redirect('fault', fault = 'Server Error')
				return redirect('success', success = 'Changes completed successfully')
			else:
				return redirect('fault', fault='Server Error')
		else:
			form = forms.StatisticsForm()
			return render(request, 'frontend/change-stats.html', {'form':form})
	else:
		return redirect('fault', fault='ACCESS DENIED!')


@login_required
def add_notice(request):

	admin_all = [u['user'] for u in acc_models.AdminUser.objects.all().values('user')]
	frontend_all = [u['user'] for u in acc_models.FrontEndUser.objects.all().values('user')]
	if request.user.pk in admin_all or request.user.pk in frontend_all:
		if request.method == 'POST':
			form = forms.NoticeForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				return redirect('success', success='Notice created successfully')
			else:
				return redirect('fault', fault='Server Error')
		else:

			form = forms.NoticeForm()
			return render(request, 'frontend/add-notice.html', {'form':form})

	else:
		return redirect('fault', fault='ACCESS DENIED!')


@login_required
def add_media(request):

	admin_all = [u['user'] for u in acc_models.AdminUser.objects.all().values('user')]
	frontend_all = [u['user'] for u in acc_models.FrontEndUser.objects.all().values('user')]
	if request.user.pk in admin_all or request.user.pk in frontend_all:
		if request.method == 'POST':
			form = forms.MediaForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				return redirect('success', success='Media created successfully')
			else:
				return redirect('fault', fault='Server Error')
		else:

			form = forms.MediaForm()
			return render(request, 'frontend/add-media.html', {'form':form})

	else:
		return redirect('fault', fault='ACCESS DENIED!')


@login_required
def add_event(request):

	admin_all = [u['user'] for u in acc_models.AdminUser.objects.all().values('user')]
	frontend_all = [u['user'] for u in acc_models.FrontEndUser.objects.all().values('user')]
	if request.user.pk in admin_all or request.user.pk in frontend_all:
		if request.method == 'POST':
			form = forms.EventForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				return redirect('success', success='Event created successfully')
			else:
				return redirect('fault', fault='Server Error')
		else:

			form = forms.EventForm()
			return render(request, 'frontend/add-event.html', {'form':form})

	else:
		return redirect('fault', fault='ACCESS DENIED!')

