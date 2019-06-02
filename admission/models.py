from django.db import models

from frontend import models as fro_models

# Create your models here.


class Application(models.Model):

	name = models.CharField(max_length=100, blank=False)
	year = models.PositiveIntegerField(blank=False)
	is_active = models.BooleanField(blank=False)
	pdf = models.FileField(upload_to='pdf/application', blank=False)
	course_1 = models.ForeignKey('frontend.Course', related_name='course_1s', on_delete=models.CASCADE)
	course_2 = models.ForeignKey('frontend.Course', related_name='course_2s', on_delete=models.CASCADE, blank=True, null=True)
	course_3 = models.ForeignKey('frontend.Course', related_name='course_3s', on_delete=models.CASCADE, blank=True, null=True)
	course_4 = models.ForeignKey('frontend.Course', related_name='course_4s', on_delete=models.CASCADE, blank=True, null=True)
	course_5 = models.ForeignKey('frontend.Course', related_name='course_5s', on_delete=models.CASCADE, blank=True, null=True)
	course_6 = models.ForeignKey('frontend.Course', related_name='course_6s', on_delete=models.CASCADE, blank=True, null=True)
	course_7 = models.ForeignKey('frontend.Course', related_name='course_7s', on_delete=models.CASCADE, blank=True, null=True)
	course_8 = models.ForeignKey('frontend.Course', related_name='course_8s', on_delete=models.CASCADE, blank=True, null=True)
	course_9 = models.ForeignKey('frontend.Course', related_name='course_9s', on_delete=models.CASCADE, blank=True, null=True)
	course_10 = models.ForeignKey('frontend.Course', related_name='course_10s', on_delete=models.CASCADE, blank=True, null=True)
	course_11 = models.ForeignKey('frontend.Course', related_name='course_11s', on_delete=models.CASCADE, blank=True, null=True)
	course_12 = models.ForeignKey('frontend.Course', related_name='course_12s', on_delete=models.CASCADE, blank=True, null=True)
	course_13 = models.ForeignKey('frontend.Course', related_name='course_13s', on_delete=models.CASCADE, blank=True, null=True)
	course_14 = models.ForeignKey('frontend.Course', related_name='course_14s', on_delete=models.CASCADE, blank=True, null=True)
	course_15 = models.ForeignKey('frontend.Course', related_name='course_15s', on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return f'{self.name} {self.year}'



class ApplicationNumber(models.Model):

	application = models.ForeignKey('admission.Application', related_name='application_number', on_delete=models.CASCADE)
	application_no = models.PositiveIntegerField(blank=False)

	def __str__(self):
		return f'{self.application.name} {self.application.year}'


class Candidate(models.Model):

	INCOME_CHOICES = (('Up to Rs. 2,50,000','Up to Rs. 2,50,000'),('From Rs. 2,50,000 - Rs. 5,00,000','From Rs. 2,50,000 - Rs. 5,00,000'),('From Rs. 5,00,000 - 10,00,000','From Rs. 5,00,000 - 10,00,000'),('More than Rs. 10,00,000','More than Rs. 10,00,000'))

	application = models.ForeignKey('admission.Application', related_name='candidates', on_delete=models.CASCADE)
	application_no = models.PositiveIntegerField(unique=True, blank=False)
	name = models.CharField(max_length=120, blank=False)
	father_name = models.CharField(max_length=120, blank=False)
	mother_name = models.CharField(max_length=120, blank=False)
	dob = models.DateField(blank=False)
	aadhar = models.PositiveIntegerField(blank=False)
	corr_add = models.TextField(blank=False)
	perm_add = models.TextField(blank=False)
	gender = models.CharField(max_length=3, choices=(('M','Male'),('F','Female'),('T','Transgender')), blank=False)
	nationality = models.CharField(max_length=30, blank=False)
	email = models.EmailField(blank=False)
	phn = models.PositiveIntegerField(blank=False)
	father_occupation = models.CharField(max_length=120, blank=False)
	father_income = models.CharField(max_length=180, blank=False, choices=INCOME_CHOICES)
	roll_10 = models.PositiveIntegerField(blank=False)
	aggregate_10 = models.CharField(max_length=50, blank=False)
	pcm_10 = models.CharField(max_length=50, blank=False)
	roll_12 = models.PositiveIntegerField(blank=False)
	aggregate_12 = models.CharField(max_length=50, blank=False)
	pcm_12 = models.CharField(max_length=50, blank=False)
	roll_upsee = models.PositiveIntegerField(blank=False)
	gen_rank = models.PositiveIntegerField(blank=False)
	cat_rank = models.PositiveIntegerField(blank=False)
	branch_1 = models.ForeignKey('frontend.Course', related_name='branch_1s', on_delete=models.CASCADE) 
	branch_2 = models.ForeignKey('frontend.Course', related_name='branch_2s', on_delete=models.CASCADE, blank=True, null=True) 
	branch_3 = models.ForeignKey('frontend.Course', related_name='branch_3s', on_delete=models.CASCADE, blank=True, null=True) 
	branch_4 = models.ForeignKey('frontend.Course', related_name='branch_4s', on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):

		return self.name


	class Meta():

		unique_together = ['application','aadhar']
		ordering = ['application_no']


