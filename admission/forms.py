from django import forms

from frontend import models as fro_models
from . import models


class ApplicationForm(forms.ModelForm):

    class Meta():
        model = models.Application
        fields = '__all__'


""" class EditApplicationForm(forms.Form):

    def __init__(self, pk, *args, **kwargs):
        super(EditApplicationForm, self).__init__(*args, **kwargs)
        COURSE_CHOICES = []
        course_list = fro_models.Course.objects.all()
        for course in course_list:
            COURSE_CHOICES.append((course.pk, course.name))
        application = models.Application.objects.get(pk__exact=pk)
        self.fields['name'] = forms.CharField(label='Name', initial=application.name)
        self.fields['year'] = forms.IntegerField(label='Year', initial=application.year)
        self.fields['is_active'] = forms.BooleanField(label='Active', initial=application.is_active)
        self.fields['pdf'] = forms.FileField(label='PDF', initial=application.pdf)
        self.fields['course_1'] = forms.ModelMultipleChoiceField(queryset=fro_models.Course.objects.all())
        self.fields['course_2'] = forms.ChoiceField(choices=COURSE_CHOICES, initial=application.course_2)
        self.fields['course_3'] = forms.ChoiceField(choices=COURSE_CHOICES, initial=application.course_3)
        self.fields['course_4'] = forms.ChoiceField(choices=COURSE_CHOICES, initial=application.course_4)
        self.fields['course_5'] = forms.ChoiceField(choices=COURSE_CHOICES, initial=application.course_5)
        self.fields['course_6'] = forms.ChoiceField(choices=COURSE_CHOICES, initial=application.course_6)
        self.fields['course_7'] = forms.ChoiceField(choices=COURSE_CHOICES, initial=application.course_7)
        self.fields['course_8'] = forms.ChoiceField(choices=COURSE_CHOICES, initial=application.course_8)
        self.fields['course_9'] = forms.ChoiceField(choices=COURSE_CHOICES, initial=application.course_9)
        self.fields['course_10'] = forms.ChoiceField(choices=COURSE_CHOICES, initial=application.course_10)
        self.fields['course_11'] = forms.ChoiceField(choices=COURSE_CHOICES, initial=application.course_11)
        self.fields['course_12'] = forms.ChoiceField(choices=COURSE_CHOICES, initial=application.course_12)
        self.fields['course_13'] = forms.ChoiceField(choices=COURSE_CHOICES, initial=application.course_13)
        self.fields['course_14'] = forms.ChoiceField(choices=COURSE_CHOICES, initial=application.course_14)
        self.fields['course_15'] = forms.ChoiceField(choices=COURSE_CHOICES, initial=application.course_15) """



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


