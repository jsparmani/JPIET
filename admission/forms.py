from django import forms

from frontend import models as fro_models
from . import models


class ApplicationForm(forms.ModelForm):

	class Meta():
		model = models.Application
		fields = '__all__'



class CandidateForm(forms.ModelForm):

	class Meta():
		model = models.Candidate
		exclude = ['application', 'application_no']


	def __init__(self, pk, *args, **kwargs):
	    super(CandidateForm, self).__init__(*args, **kwargs)
	    # self.fields['application'].queryset = models.Application.objects.filter(is_active=True)
	    application = models.Application.objects.get(pk__exact=pk)

	    pk_list = []

	    for attr, value in vars(application).items():
	    	if attr[0:6]=='course' and not value == None:
	    		pk_list.append(value)

	    c = 4
	    for i in range(4-len(pk_list)):
	    	del self.fields[f'branch_{c}']
	    	c = c-1


	    for i in range(1,len(pk_list)+1):
		    self.fields[f'branch_{i}'].queryset = fro_models.Course.objects.filter(pk__in=pk_list)


