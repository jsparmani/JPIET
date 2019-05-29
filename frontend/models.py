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


