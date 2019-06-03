from django import forms

from frontend import models as fro_models
from . import models


class ApplicationForm(forms.ModelForm):

    class Meta():
        model = models.Application
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course_1'].widget.attrs['onchange'] = 'choiceSelection(event)'
        self.fields['course_2'].widget.attrs['onchange'] = 'choiceSelection(event)'
        self.fields['course_3'].widget.attrs['onchange'] = 'choiceSelection(event)'
        self.fields['course_4'].widget.attrs['onchange'] = 'choiceSelection(event)'
        self.fields['course_5'].widget.attrs['onchange'] = 'choiceSelection(event)'
        self.fields['course_6'].widget.attrs['onchange'] = 'choiceSelection(event)'
        self.fields['course_7'].widget.attrs['onchange'] = 'choiceSelection(event)'
        self.fields['course_8'].widget.attrs['onchange'] = 'choiceSelection(event)'
        self.fields['course_9'].widget.attrs['onchange'] = 'choiceSelection(event)'
        self.fields['course_10'].widget.attrs['onchange'] = 'choiceSelection(event)'
        self.fields['course_11'].widget.attrs['onchange'] = 'choiceSelection(event)'
        self.fields['course_12'].widget.attrs['onchange'] = 'choiceSelection(event)'
        self.fields['course_13'].widget.attrs['onchange'] = 'choiceSelection(event)'
        self.fields['course_14'].widget.attrs['onchange'] = 'choiceSelection(event)'
        self.fields['course_15'].widget.attrs['onchange'] = 'choiceSelection(event)'


class EditApplicationForm(forms.Form):

    def __init__(self, pk, *args, **kwargs):
        super(EditApplicationForm, self).__init__(*args, **kwargs)
        application = models.Application.objects.get(pk__exact=pk)
        self.fields['is_active'] = forms.BooleanField(label='Active', initial=application.is_active, required=False)



class CandidateForm(forms.ModelForm):

    class Meta():
        model = models.Candidate
        exclude = ['application', 'application_no']


    def __init__(self, pk, *args, **kwargs):
        super(CandidateForm, self).__init__(*args, **kwargs)
        # self.fields['application'].queryset = models.Application.objects.filter(is_active=True)
        application = models.Application.objects.get(pk__exact=pk)
        self.fields['branch_1'].widget.attrs['onchange'] = 'choiceSelection(event)'
        self.fields['branch_2'].widget.attrs['onchange'] = 'choiceSelection(event)'
        self.fields['branch_3'].widget.attrs['onchange'] = 'choiceSelection(event)'
        self.fields['branch_4'].widget.attrs['onchange'] = 'choiceSelection(event)'

        pk_list = []

        for attr, value in vars(application).items():
            if attr[0:6]=='course' and not value == None:
                pk_list.append(value)

        c = 4
        for i in range(4-len(pk_list)):
            del self.fields[f'branch_{c}']
            c = c-1

        if (len(pk_list)<5):
            for i in range(1,len(pk_list)+1):
                self.fields[f'branch_{i}'].queryset = fro_models.Course.objects.filter(pk__in=pk_list)
        else:
            for i in range(1,5):
                self.fields[f'branch_{i}'].queryset = fro_models.Course.objects.filter(pk__in=pk_list)


