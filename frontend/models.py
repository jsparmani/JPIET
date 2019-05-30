from django.db import models

# Create your models here.

class HomeImage(models.Model):

	uid = models.PositiveIntegerField(unique=True, blank=False)
	logo_image = models.ImageField(upload_to = 'images/logo', blank=False)
	carousel_image1 = models.ImageField(upload_to = 'images/carousel', blank=False)
	carousel_image2 = models.ImageField(upload_to = 'images/carousel', blank=False)
	carousel_image3 = models.ImageField(upload_to = 'images/carousel', blank=False)
	carousel_image4 = models.ImageField(upload_to = 'images/carousel', blank=False)
	side_image = models.ImageField(upload_to = 'images/side', blank=False)


class Statistics(models.Model):

	uid = models.PositiveIntegerField(blank=False)
	students = models.PositiveIntegerField(blank=False) 
	area = models.PositiveIntegerField(blank=False) 
	alumni = models.PositiveIntegerField(blank=False) 
	recruiters = models.PositiveIntegerField(blank=False) 
	students_placed = models.PositiveIntegerField(blank=False) 
	years = models.PositiveIntegerField(blank=False) 


class Notice(models.Model):

	text = models.TextField(blank=False)
	pdf = models.FileField(upload_to='pdf/notices', blank=False)
	on_landing = models.BooleanField(blank=False)
	created_at = models.DateField(auto_now=True)

	def __str__(self):
		return self.text

	class Meta():

		ordering = ['-pk']


class Media(models.Model):

	pic = models.ImageField(upload_to='images/media_coverage', blank=False)
	on_landing = models.BooleanField(blank=False)

	class Meta():

		ordering = ['-pk']


class Event(models.Model):

	heading = models.CharField(max_length=100, blank=False)
	image = models.ImageField(upload_to='images/event', blank=False)
	details = models.TextField(blank=False)
	on_landing = models.BooleanField(blank=False)

	class Meta():

		ordering = ['-pk']


class Testimonial(models.Model):

	name = models.CharField(max_length=100, blank=False)
	text = models.TextField(blank=False)
	image = models.ImageField(upload_to='images/testimonials', blank=False)

	class Meta():

		ordering = ['-pk']


class Recruiter(models.Model):

	image = models.ImageField(upload_to='images/recruiters', blank=False)
	on_landing = models.BooleanField(blank=False)

	class Meta():

		ordering = ['-pk']



##############ABOUT US#################

class Message(models.Model):

	uid = models.PositiveIntegerField(unique=True, blank=False)
	title = models.CharField(max_length=100, blank=False)
	name = models.CharField(max_length=100, blank=False)
	image = models.ImageField(upload_to='images/message', blank=False)
	message = models.TextField(blank=False)


	def __str__(self):
		return self.title

	class Meta():

		ordering = ['uid']


class Infrastructure(models.Model):

	title = models.CharField(max_length=100, blank=False) 
	image = models.ImageField(upload_to='images/infrastructure', blank=False)
	text = models.TextField(blank=False)

	class Meta():

		ordering = ['pk']

	def __str__(self):
		return self.title


class VisionMission(models.Model):

	uid = models.PositiveIntegerField(unique=True)
	text_above = models.TextField(blank=True)
	bullet1 = models.TextField(blank=True)
	bullet2 = models.TextField(blank=True)
	bullet3 = models.TextField(blank=True)
	bullet4 = models.TextField(blank=True)
	bullet5 = models.TextField(blank=True)
	bullet6 = models.TextField(blank=True)
	bullet7 = models.TextField(blank=True)
	bullet8 = models.TextField(blank=True)
	bullet9 = models.TextField(blank=True)
	bullet10 = models.TextField(blank=True)
	text_below = models.TextField(blank=True)



