from django.db import models

# Create your models here.

class Faculty(models.Model):

    name = models.CharField(max_length=50, blank=False)
    designation = models.CharField(max_length=50, blank=False)
    contact_num = models.PositiveIntegerField(blank=False)
    qualification1 = models.CharField(max_length=50, blank=False)
    qualification2 = models.CharField(max_length=50, blank=True)
    qualification3 = models.CharField(max_length=50, blank=True)
    field_of_interest = models.TextField(blank=False)
    experience = models.TextField(blank=False)
    pic = models.ImageField(upload_to='images/faculty',blank=False)

    class Meta:
        verbose_name_plural = "Faculties"

    def __str__(self):
        return self.name
