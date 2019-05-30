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



class EditNoticeForm(forms.Form):

    def __init__(self, pk, *args, **kwargs):
        super(EditNoticeForm, self).__init__(*args, **kwargs)
        notice = models.Notice.objects.get(pk__exact=pk)
        self.fields['pdf'] = forms.FileField(label='PDF', initial=notice.pdf)
        self.fields['text'] = forms.CharField(label='Text', initial=notice.text, widget=forms.Textarea)
        self.fields['on_landing'] = forms.BooleanField(label='Show on Landing Page', initial=notice.on_landing)


class MediaForm(forms.ModelForm):

    class Meta():

        model = models.Media
        fields = '__all__'


class EventForm(forms.ModelForm):

    class Meta():

        model = models.Event
        fields = '__all__'


class EditEventForm(forms.Form):

    def __init__(self, pk, *args, **kwargs):
        super(EditEventForm, self).__init__(*args, **kwargs)
        event = models.Event.objects.get(pk__exact=pk)
        self.fields['heading'] = forms.CharField(label='Heading', initial=event.heading)
        self.fields['image'] = forms.ImageField(label='Image', initial=event.image)
        self.fields['details'] = forms.CharField(label='Details', initial=event.details, widget=forms.Textarea)
        self.fields['on_landing'] = forms.BooleanField(label='Show on Landing Page', initial=event.on_landing)


class TestimonialForm(forms.ModelForm):

    class Meta():

        model = models.Testimonial
        fields = '__all__'


class EditTestimonialForm(forms.Form):

    def __init__(self, pk, *args, **kwargs):
        super(EditTestimonialForm, self).__init__(*args, **kwargs)
        testimonial = models.Testimonial.objects.get(pk__exact=pk)
        self.fields['name'] = forms.CharField(label='Name', initial=testimonial.name)
        self.fields['image'] = forms.ImageField(label='Image', initial=testimonial.image)
        self.fields['text'] = forms.CharField(label='Text', initial=testimonial.text, widget=forms.Textarea)


class RecruiterForm(forms.ModelForm):

    class Meta():

        model = models.Recruiter
        fields = '__all__'







class MessageForm(forms.Form):

    def __init__(self, uid, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        msg = models.Message.objects.get(uid__exact=uid)
        self.fields['title'] = forms.CharField(label='Title', initial=msg.title)
        self.fields['name'] = forms.CharField(label='Name', initial=msg.name)
        self.fields['image'] = forms.ImageField(label='Image', initial=msg.image)
        self.fields['message'] = forms.TextField(label='Message', initial=msg.message)


class InfrastructureForm(forms.ModelForm):

    class Meta():

        model = models.Infrastructure
        fields = '__all__'


class EditInfrastructureForm(forms.Form):

    def __init__(self, pk, *args, **kwargs):
        super(EditInfrastructureForm, self).__init__(*args, **kwargs)
        infra = models.Infrastructure.objects.get(pk__exact=pk)
        self.fields['title'] = forms.CharField(label='Title', initial=infra.title)
        self.fields['image'] = forms.ImageField(label='Image', initial=infra.image)
        self.fields['text'] = forms.CharField(label='Text', initial=infra.text, widget=forms.Textarea)


class VisionMissionForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(VisionMissionForm, self).__init__(*args, **kwargs)
        vis = models.VisionMission.objects.get(uid__exact=1)
        self.fields['text_above'] = forms.CharField(label='Text Above', initial=vis.text_above, required=False)
        self.fields['bullet1'] = forms.CharField(label='Bullet 1', initial=vis.bullet1, required=False)
        self.fields['bullet2'] = forms.CharField(label='Bullet 2', initial=vis.bullet2, required=False)
        self.fields['bullet3'] = forms.CharField(label='Bullet 3', initial=vis.bullet3, required=False)
        self.fields['bullet4'] = forms.CharField(label='Bullet 4', initial=vis.bullet4, required=False)
        self.fields['bullet5'] = forms.CharField(label='Bullet 5', initial=vis.bullet5, required=False)
        self.fields['bullet6'] = forms.CharField(label='Bullet 6', initial=vis.bullet6, required=False)
        self.fields['bullet7'] = forms.CharField(label='Bullet 7', initial=vis.bullet7, required=False)
        self.fields['bullet8'] = forms.CharField(label='Bullet 8', initial=vis.bullet8, required=False)
        self.fields['bullet9'] = forms.CharField(label='Bullet 9', initial=vis.bullet9, required=False)
        self.fields['bullet10'] = forms.CharField(label='Bullet 10', initial=vis.bullet10, required=False)
        self.fields['text_below'] = forms.CharField(label='Text Below', initial=vis.text_below, required=False)
