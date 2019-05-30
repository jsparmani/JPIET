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


def view_notices(request):

	notices = models.Notice.objects.all()
	return render(request, 'frontend/view-notices.html', {'notices': notices})

@login_required
def delete_notice(request, pk):

	admin_all = [u['user'] for u in acc_models.AdminUser.objects.all().values('user')]
	frontend_all = [u['user'] for u in acc_models.FrontEndUser.objects.all().values('user')]
	if request.user.pk in admin_all or request.user.pk in frontend_all:
		try:
			models.Notice.objects.get(pk__exact=pk).delete()
			return redirect('frontend:view_notices')
		except:
			return redirect('fault', fault="Some error occured")
	else:
		return redirect('fault', fault='ACCESS DENIED!')


@login_required
def edit_notice(request, pk):
	admin_all = [u['user'] for u in acc_models.AdminUser.objects.all().values('user')]
	frontend_all = [u['user'] for u in acc_models.FrontEndUser.objects.all().values('user')]
	if request.user.pk in admin_all or request.user.pk in frontend_all:
		if request.method == 'POST':
			form = forms.EditNoticeForm(data=request.POST, files=request.FILES, pk=pk)
			if form.is_valid():
				notice = models.Notice.objects.get(pk__exact=pk)
				notice.text = form.cleaned_data['text']
				notice.pdf = form.cleaned_data['text']
				notice.on_landing = form.cleaned_data['on_landing']
				try:
					notice.save()
				except:
					return redirect('fault', fault='Server Error')
				return redirect('success', success='Notice changed successfully')
		else:
			form = forms.EditNoticeForm(pk=pk)
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


def view_medias(request):

	medias = models.Media.objects.all()
	return render(request, 'frontend/view-medias.html', {'medias': medias})

@login_required
def delete_media(request, pk):

	admin_all = [u['user'] for u in acc_models.AdminUser.objects.all().values('user')]
	frontend_all = [u['user'] for u in acc_models.FrontEndUser.objects.all().values('user')]
	if request.user.pk in admin_all or request.user.pk in frontend_all:
		try:
			models.Media.objects.get(pk__exact=pk).delete()
			return redirect('frontend:view_medias')
		except:
			return redirect('fault', fault="Some error occured")
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


def view_events(request):

	events = models.Event.objects.all()
	return render(request, 'frontend/view-events.html', {'events': events})

@login_required
def delete_event(request, pk):

	admin_all = [u['user'] for u in acc_models.AdminUser.objects.all().values('user')]
	frontend_all = [u['user'] for u in acc_models.FrontEndUser.objects.all().values('user')]
	if request.user.pk in admin_all or request.user.pk in frontend_all:
		try:
			models.Event.objects.get(pk__exact=pk).delete()
			return redirect('frontend:view_events')
		except:
			return redirect('fault', fault="Some error occured")
	else:
		return redirect('fault', fault='ACCESS DENIED!')


@login_required
def edit_event(request, pk):
	admin_all = [u['user'] for u in acc_models.AdminUser.objects.all().values('user')]
	frontend_all = [u['user'] for u in acc_models.FrontEndUser.objects.all().values('user')]
	if request.user.pk in admin_all or request.user.pk in frontend_all:
		if request.method == 'POST':
			form = forms.EditEventForm(data=request.POST, files=request.FILES, pk=pk)
			if form.is_valid():
				event = models.Event.objects.get(pk__exact=pk)
				event.heading = form.cleaned_data['heading']
				event.image = form.cleaned_data['image']
				event.details = form.cleaned_data['details']
				event.on_landing = form.cleaned_data['on_landing']
				try:
					event.save()
				except:
					return redirect('fault', fault='Server Error')
				return redirect('success', success='Event changed successfully')
		else:
			form = forms.EditEventForm(pk=pk)
			return render(request, 'frontend/add-event.html', {'form':form})
	else:
		return redirect('fault', fault='ACCESS DENIED!')

@login_required
def add_testimonial(request):

	admin_all = [u['user'] for u in acc_models.AdminUser.objects.all().values('user')]
	frontend_all = [u['user'] for u in acc_models.FrontEndUser.objects.all().values('user')]
	if request.user.pk in admin_all or request.user.pk in frontend_all:
		if request.method == 'POST':
			form = forms.TestimonialForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				return redirect('success', success='Testimonial created successfully')
			else:
				return redirect('fault', fault='Server Error')
		else:

			form = forms.TestimonialForm()
			return render(request, 'frontend/add-testimonial.html', {'form':form})

	else:
		return redirect('fault', fault='ACCESS DENIED!')


def view_testimonials(request):

	testimonials = models.Testimonial.objects.all()
	return render(request, 'frontend/view-testimonials.html', {'testimonials': testimonials})


@login_required
def delete_testimonial(request, pk):

	admin_all = [u['user'] for u in acc_models.AdminUser.objects.all().values('user')]
	frontend_all = [u['user'] for u in acc_models.FrontEndUser.objects.all().values('user')]
	if request.user.pk in admin_all or request.user.pk in frontend_all:
		try:
			models.Testimonial.objects.get(pk__exact=pk).delete()
			return redirect('frontend:view_testimonials')
		except:
			return redirect('fault', fault="Some error occured")
	else:
		return redirect('fault', fault='ACCESS DENIED!')


@login_required
def edit_testimonial(request, pk):
	admin_all = [u['user'] for u in acc_models.AdminUser.objects.all().values('user')]
	frontend_all = [u['user'] for u in acc_models.FrontEndUser.objects.all().values('user')]
	if request.user.pk in admin_all or request.user.pk in frontend_all:
		if request.method == 'POST':
			form = forms.EditTestimonialForm(data=request.POST, files=request.FILES, pk=pk)
			if form.is_valid():
				testimonial = models.Testimonial.objects.get(pk__exact=pk)
				testimonial.name = form.cleaned_data['name']
				testimonial.image = form.cleaned_data['image']
				testimonial.text = form.cleaned_data['text']
				try:
					testimonial.save()
				except:
					return redirect('fault', fault='Server Error')
				return redirect('success', success='Testimonial changed successfully')
		else:
			form = forms.EditTestimonialForm(pk=pk)
			return render(request, 'frontend/add-testimonial.html', {'form':form})
	else:
		return redirect('fault', fault='ACCESS DENIED!')


@login_required
def add_recruiter(request):

	admin_all = [u['user'] for u in acc_models.AdminUser.objects.all().values('user')]
	frontend_all = [u['user'] for u in acc_models.FrontEndUser.objects.all().values('user')]
	if request.user.pk in admin_all or request.user.pk in frontend_all:
		if request.method == 'POST':
			form = forms.RecruiterForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				return redirect('success', success='Recruiter created successfully')
			else:
				return redirect('fault', fault='Server Error')
		else:

			form = forms.RecruiterForm()
			return render(request, 'frontend/add-recruiter.html', {'form':form})

	else:
		return redirect('fault', fault='ACCESS DENIED!')


def view_recruiters(request):

	recruiters = models.Recruiter.objects.all()
	return render(request, 'frontend/view-recruiters.html', {'recruiters': recruiters})

@login_required
def delete_recruiter(request, pk):

	admin_all = [u['user'] for u in acc_models.AdminUser.objects.all().values('user')]
	frontend_all = [u['user'] for u in acc_models.FrontEndUser.objects.all().values('user')]
	if request.user.pk in admin_all or request.user.pk in frontend_all:
		try:
			models.Recruiter.objects.get(pk__exact=pk).delete()
			return redirect('frontend:view_recruiters')
		except:
			return redirect('fault', fault="Some error occured")
	else:
		return redirect('fault', fault='ACCESS DENIED!')


def view_about_us(request, uid=1):
	if uid in [1,2,3,4,5,6]:
		msg = models.Message.objects.get(uid__exact=uid)
		return render(request, 'frontend/view-about-us.html', {'msg':msg, 'uid':uid})
	elif uid == 7:
		vis = models.VisionMission.objects.get(uid__exact=1)
		return render(request, 'frontend/view-about-us.html', {'vis':vis, 'uid':uid})
	elif uid == 8:
		infrastructures = models.Infrastructure.objects.all()
		return render(request, 'frontend/view-about-us.html', {'infrastructures':infrastructures, 'uid':uid})

@login_required
def get_about_us(request):

	return render(request, 'frontend/get_about_us.html')


@login_required
def change_message(request, uid):

	admin_all = [u['user'] for u in acc_models.AdminUser.objects.all().values('user')]
	frontend_all = [u['user'] for u in acc_models.FrontEndUser.objects.all().values('user')]
	if request.user.pk in admin_all or request.user.pk in frontend_all:
		if request.method == 'POST':
			form = forms.MessageForm(data=request.POST, files=request.FILES, uid=uid)
			if form.is_valid():
				msg = models.Message.objects.get(uid__exact=uid)
				msg.title = forms.cleaned_data['title']
				msg.name = forms.cleaned_data['name']
				msg.image = forms.cleaned_data['image']
				msg.message = forms.cleaned_data['message']
				try:
					msg.save()
				except:
					return redirect('fault', fault='Server Error')
				return redirect('success', success='Message changed successfully')
			else:
				return redirect('fault', fault='Server Error')
		else:
			form = forms.MessageForm(uid=uid)
			return render(request, 'frontend/change-message.html', {'form':form})
	else:
		return redirect('fault', fault='ACCESS DENIED!')



@login_required
def add_infrastructure(request):

	admin_all = [u['user'] for u in acc_models.AdminUser.objects.all().values('user')]
	frontend_all = [u['user'] for u in acc_models.FrontEndUser.objects.all().values('user')]
	if request.user.pk in admin_all or request.user.pk in frontend_all:
		if request.method == 'POST':
			form = forms.InfrastructureForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				return redirect('success', success='Infrastructure created successfully')
			else:
				return redirect('fault', fault='Server Error')
		else:

			form = forms.InfrastructureForm()
			return render(request, 'frontend/add-infrastructure.html', {'form':form})

	else:
		return redirect('fault', fault='ACCESS DENIED!')


@login_required
def delete_infrastructure(request, pk):

	admin_all = [u['user'] for u in acc_models.AdminUser.objects.all().values('user')]
	frontend_all = [u['user'] for u in acc_models.FrontEndUser.objects.all().values('user')]
	if request.user.pk in admin_all or request.user.pk in frontend_all:
		try:
			models.Infrastructure.objects.get(pk__exact=pk).delete()
			return redirect('frontend:view_about_us', uid=8)
		except:
			return redirect('fault', fault="Some error occured")
	else:
		return redirect('fault', fault='ACCESS DENIED!')


@login_required
def edit_infrastructure(request, pk):
	admin_all = [u['user'] for u in acc_models.AdminUser.objects.all().values('user')]
	frontend_all = [u['user'] for u in acc_models.FrontEndUser.objects.all().values('user')]
	if request.user.pk in admin_all or request.user.pk in frontend_all:
		if request.method == 'POST':
			form = forms.EditInfrastructureForm(data=request.POST, files=request.FILES, pk=pk)
			if form.is_valid():
				infra = models.Infrastructure.objects.get(pk__exact=pk)
				infra.title = form.cleaned_data['title']
				infra.image = form.cleaned_data['image']
				infra.text = form.cleaned_data['text']
				try:
					infra.save()
				except:
					return redirect('fault', fault='Server Error')
				return redirect('success', success='Infrastructure changed successfully')
		else:
			form = forms.EditInfrastructureForm(pk=pk)
			return render(request, 'frontend/add-infrastructure.html', {'form':form})
	else:
		return redirect('fault', fault='ACCESS DENIED!')


@login_required
def change_vision_mission(request):
	admin_all = [u['user'] for u in acc_models.AdminUser.objects.all().values('user')]
	frontend_all = [u['user'] for u in acc_models.FrontEndUser.objects.all().values('user')]
	if request.user.pk in admin_all or request.user.pk in frontend_all:
		if request.method == 'POST':
			form = forms.VisionMissionForm(request.POST)
			if form.is_valid():
				vis = models.VisionMission.objects.get(uid__exact=1)
				vis.text_above = form.cleaned_data['text_above']
				vis.bullet1 = form.cleaned_data['bullet1']
				vis.bullet2 = form.cleaned_data['bullet2']
				vis.bullet3 = form.cleaned_data['bullet3']
				vis.bullet4 = form.cleaned_data['bullet4']
				vis.bullet5 = form.cleaned_data['bullet5']
				vis.bullet6 = form.cleaned_data['bullet6']
				vis.bullet7 = form.cleaned_data['bullet7']
				vis.bullet8 = form.cleaned_data['bullet8']
				vis.bullet9 = form.cleaned_data['bullet9']
				vis.bullet10 = form.cleaned_data['bullet10']
				vis.text_above = form.cleaned_data['text_above']
				try:
					vis.save()
				except:
					return redirect('fault', fault = 'Server Error')
				return redirect('success', success = 'Changes completed successfully')
			else:
				return redirect('fault', fault='Server Error')
		else:
			form = forms.VisionMissionForm()
			return render(request, 'frontend/change-vision-mission.html', {'form':form})
	else:
		return redirect('fault', fault='ACCESS DENIED!')





