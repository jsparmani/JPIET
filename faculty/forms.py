from django import forms

from . import models


class FacultyForm(forms.ModelForm):

    class Meta():

        model = models.Faculty
        fields = '__all__'


class EditFacultyForm(forms.Form):

    def __init__(self, pk, *args, **kwargs):
        super(EditFacultyForm, self).__init__(*args, **kwargs)
        faculty = models.Faculty.objects.get(pk__exact=pk)
        self.fields['name'] = forms.CharField(label='Name', initial=faculty.name)
        self.fields['designation'] = forms.CharField(label='Designation', initial=faculty.designation)
        self.fields['contact_num'] = forms.IntegerField(label='Contact Number', initial=faculty.contact_num)
        self.fields['qualification1'] = forms.CharField(label='Qualification 1', initial=faculty.qualification1)
        self.fields['qualification2'] = forms.CharField(label='Qualification 2', initial=faculty.qualification2, required=False)
        self.fields['qualification3'] = forms.CharField(label='Qualification 3', initial=faculty.qualification3, required=False)
        self.fields['field_of_interest'] = forms.CharField(label='Field Of Interest', initial=faculty.field_of_interest, widget=forms.Textarea)
        self.fields['experience'] = forms.CharField(label='Experience', initial=faculty.experience, widget=forms.Textarea)
        self.fields['pic'] = forms.ImageField(label='Image', initial=faculty.pic)