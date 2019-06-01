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


class DepartmentForm(forms.ModelForm):

    class Meta():

        model = models.Department
        fields = '__all__'


class EditDepartmentForm(forms.Form):

    def __init__(self, pk, *args, **kwargs):
        super(EditDepartmentForm, self).__init__(*args, **kwargs)
        department = models.Department.objects.get(pk__exact=pk)
        self.fields['name'] = forms.CharField(label='Name', initial=department.name)
        self.fields['image'] = forms.ImageField(label='Image', initial=department.image)
        self.fields['text'] = forms.CharField(label='Text', initial=department.text, widget=forms.Textarea)


class FacultyForm(forms.ModelForm):

    class Meta():

        model = models.Faculty
        fields = '__all__'


class EditFacultyForm(forms.Form):

    def __init__(self, pk, *args, **kwargs):
        super(EditFacultyForm, self).__init__(*args, **kwargs)
        faculty = models.Faculty.objects.get(pk__exact=pk)
        self.fields['department'] = forms.CharField(label='Department', initial=faculty.department)
        self.fields['name'] = forms.CharField(label='Name', initial=faculty.name)
        self.fields['designation'] = forms.CharField(label='Designation', initial=faculty.designation)
        self.fields['contact_num'] = forms.IntegerField(label='Contact Number', initial=faculty.contact_num)
        self.fields['qualification1'] = forms.CharField(label='Qualification 1', initial=faculty.qualification1)
        self.fields['qualification2'] = forms.CharField(label='Qualification 2', initial=faculty.qualification2, required=False)
        self.fields['qualification3'] = forms.CharField(label='Qualification 3', initial=faculty.qualification3, required=False)
        self.fields['field_of_interest'] = forms.CharField(label='Field Of Interest', initial=faculty.field_of_interest, widget=forms.Textarea)
        self.fields['experience'] = forms.CharField(label='Experience', initial=faculty.experience, widget=forms.Textarea)
        self.fields['pic'] = forms.ImageField(label='Image', initial=faculty.pic)


class LabForm(forms.ModelForm):

    class Meta():

        model = models.Lab
        fields = '__all__'


class EditLabForm(forms.Form):

    def __init__(self, pk, *args, **kwargs):
        super(EditLabForm, self).__init__(*args, **kwargs)
        lab = models.Lab.objects.get(pk__exact=pk)
        DEPARTMENT_CHOICES = []
        department_list = models.Department.objects.all()
        for department in department_list:
            DEPARTMENT_CHOICES.append((department.pk, department.name))
        self.fields['department'] = forms.ChoiceField(choices=DEPARTMENT_CHOICES)
        self.fields['lab'] = forms.CharField(label='lab', initial=lab.lab)
        
        
class TrainingPlacementForm(forms.ModelForm):

    class Meta():

        model = models.TrainingPlacement
        fields = '__all__'


class EditTrainingPlacementForm(forms.Form):

    def __init__(self, pk, *args, **kwargs):
        super(EditTrainingPlacementForm, self).__init__(*args, **kwargs)
        tp = models.TrainingPlacement.objects.get(pk__exact=pk)
        self.fields['heading'] = forms.CharField(label='Heading', initial=tp.heading)
        self.fields['image'] = forms.ImageField(label='Image', initial=tp.image)
        self.fields['text'] = forms.CharField(label='Text', initial=tp.text, widget=forms.Textarea)


class CourseForm(forms.ModelForm):

    class Meta():

        model = models.Course
        fields = '__all__'

class EditCourseForm(forms.Form):

    def __init__(self, pk, *args, **kwargs):
        super(EditCourseForm, self).__init__(*args, **kwargs)
        course = models.Course.objects.get(pk__exact=pk)
        DEPARTMENT_CHOICES = []
        department_list = models.Department.objects.all()
        for department in department_list:
            DEPARTMENT_CHOICES.append((department.pk, department.name))
        self.fields['department'] = forms.ChoiceField(choices=DEPARTMENT_CHOICES, initial=course.department.pk)
        self.fields['name'] = forms.CharField(label='lab', initial=course.name)
        self.fields['semesters'] = forms.IntegerField(label='Semesters', initial=course.semesters)

class SyllabusForm(forms.ModelForm):

    class Meta():

        model = models.Syllabus
        fields = '__all__'


class EditSyllabusForm(forms.Form):

    def __init__(self, pk, *args, **kwargs):
        super(EditSyllabusForm, self).__init__(*args, **kwargs)
        syllabus = models.Syllabus.objects.get(pk__exact=pk)
        COURSE_CHOICES = []
        course_list = models.Course.objects.all()
        for course in course_list:
            COURSE_CHOICES.append((course.pk, course.name))
        self.fields['course'] = forms.ChoiceField(choices=COURSE_CHOICES, initial=syllabus.course.pk)
        self.fields['semester'] = forms.IntegerField(label='Semester', initial=syllabus.semester)
        self.fields['pdf'] = forms.FileField(label='PDF', initial=syllabus.pdf)


class ExamForm(forms.ModelForm):

    class Meta():

        model = models.Exam
        fields = '__all__'

class EditExamForm(forms.Form):

    def __init__(self, pk, *args, **kwargs):
        super(EditExamForm, self).__init__(*args, **kwargs)
        exam = models.Exam.objects.get(pk__exact=pk)
        COURSE_CHOICES = []
        course_list = models.Course.objects.all()
        for course in course_list:
            COURSE_CHOICES.append((course.pk, course.name))
        self.fields['course'] = forms.ChoiceField(choices=COURSE_CHOICES, initial=exam.course.pk)
        self.fields['semester'] = forms.IntegerField(label='Semester', initial=exam.semester)
        self.fields['date'] = forms.DateField(label='Date', initial=exam.date)
        self.fields['pdf'] = forms.FileField(label='PDF', initial=exam.pdf)


class HomePDFForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(HomePDFForm, self).__init__(*args, **kwargs)
        home_pdf = models.HomePDF.objects.get(uid__exact=1)
        self.fields['application_form'] = forms.FileField(label='Application Form', initial=home_pdf.application_form)
        self.fields['information_brochure'] = forms.FileField(label='Information Brochure', initial=home_pdf.information_brochure)
        self.fields['fees'] = forms.FileField(label='Fees', initial=home_pdf.fees)
        self.fields['aicte'] = forms.FileField(label='AICTE Approval', initial=home_pdf.aicte)
        self.fields['anti_ragging'] = forms.FileField(label='Anti Ragging', initial=home_pdf.anti_ragging)
        self.fields['training_placement'] = forms.FileField(label='Training and Placement', initial=home_pdf.training_placement)