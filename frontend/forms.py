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




class StatisticsForm(forms.Form):

	def __init__(self, *args, **kwargs):
	    super(StatisticsForm, self).__init__(*args, **kwargs)
	    statistics = models.Statistics.objects.get(uid__exact=1)
	    self.fields['students'] = forms.IntegerField(label='Students', initial=statistics.students)
	    self.fields['area'] = forms.IntegerField(label='Area', initial=statistics.area)
	    self.fields['alumni'] = forms.IntegerField(label='Alumni', initial=statistics.alumni)
	    self.fields['recruiters'] = forms.IntegerField(label='Recruiters', initial=statistics.recruiters)
	    self.fields['students_placed'] = forms.IntegerField(label='Students Placed', initial=statistics.students_placed)
	    self.fields['years'] = forms.IntegerField(label='Years of excellency', initial=statistics.years)



class NoticeForm(forms.ModelForm):

	class Meta():

		model = models.Notice
		exclude = ['created_at']


class MediaForm(forms.ModelForm):

	class Meta():

		model = models.Media
		fields = '__all__'


class EventForm(forms.ModelForm):

	class Meta():

		model = models.Event
		fields = '__all__'


class TestimonialForm(forms.ModelForm):

	class Meta():

		model = models.Testimonial
		fields = '__all__'


class RecruiterForm(forms.ModelForm):

	class Meta():

		model = models.Recruiter
		fields = '__all__'
