from django import forms

from . import models

class HomeImageForm(forms.Form):

	def __init__(self, *args, **kwargs):
	    super(HomeImageForm, self).__init__(*args, **kwargs)
	    home_image = models.HomeImage.objects.get(uid__exact=1)
	    self.fields['logo_image'] = forms.ImageField(label='Logo', initial=home_image.logo_image)
	    self.fields['carousel_image1'] = forms.ImageField(label='Carousel Image 1', initial=home_image.carousel_image1)
	    self.fields['carousel_image2'] = forms.ImageField(label='Carousel Image 2', initial=home_image.carousel_image2)
	    self.fields['carousel_image3'] = forms.ImageField(label='Carousel Image 3', initial=home_image.carousel_image3)
	    self.fields['carousel_image4'] = forms.ImageField(label='Carousel Image 4', initial=home_image.carousel_image4)
	    self.fields['side_image'] = forms.ImageField(label='Side Image', initial=home_image.side_image)