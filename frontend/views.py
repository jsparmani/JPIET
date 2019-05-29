from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from account import models as acc_models
from . import forms
from . import models
# Create your views here.

@login_required
def home_image(request):

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
			return render(request, 'frontend/home-image.html', {'form':form})
	else:
		return redirect('fault', fault='ACCESS DENIED!')