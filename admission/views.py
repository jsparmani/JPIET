from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from frontend import models as fro_models
from django.http import HttpResponse


import os
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import simpleSplit



from account import models as acc_models
from frontend import models as fro_models

from. import models
from. import forms

# Create your views here.

@login_required
def add_application(request):

	admin_all = [u['user'] for u in acc_models.AdminUser.objects.all().values('user')]
	frontend_all = [u['user'] for u in acc_models.FrontEndUser.objects.all().values('user')]
	if request.user.pk in admin_all or request.user.pk in frontend_all:
		if request.method == 'POST':
			form = forms.ApplicationForm(request.POST, request.FILES)
			if form.is_valid():
				application = form.save()
				pk_string = str(application.pk)
				for i in range(4-len(pk_string)):
					pk_string = '0'+pk_string
				models.ApplicationNumber.objects.create(application=application, application_no=int(str(form.cleaned_data['year'])[-2::]+ pk_string + '00000'))

				return redirect('success', success='Application created successfully')
			else:
				return redirect('fault', fault='Server Error')
		else:

			form = forms.ApplicationForm()
			return render(request, 'admission/add-application.html', {'form':form})

	else:
		return redirect('fault', fault='ACCESS DENIED!')




def view_application(request):

	application_list = models.Application.objects.all().filter(is_active__exact=True)
	return render(request, 'admission/view-application.html', {'application_list':application_list} )



def add_candidate(request, pk):

	if request.method == 'POST':
		form = forms.CandidateForm(data=request.POST, files=request.FILES, pk=pk)
		if form.is_valid():
			try:
				candidate = form.save(commit=False)
				candidate.application = models.Application.objects.get(pk__exact=pk)
				application_no_obj = models.ApplicationNumber.objects.get(application__pk__exact=pk)
				candidate.application_no = application_no_obj.application_no + 1
				application_no_obj.application_no  = application_no_obj.application_no + 1					
				candidate.save()
				application_no_obj.save()
				send_mail("JPIET | Application Registered",f'Dear {candidate.name}, Your application is registered with JPIET. The application number for the same is {candidate.application_no}','jpietuniversity@gmail.com',[candidate.email],fail_silently = True)
			except:
				if form.cleaned_data['aadhar'] in [u['aadhar'] for u in models.Candidate.objects.all().values('aadhar')] :
					return redirect('fault', fault='Entered AADHAR number is already registered')
				else:
					return redirect('fault', fault='Server Error')


			return redirect('success', success='Candidate created successfully')
		else:
			if int(request.POST['aadhar']) in [u['aadhar'] for u in models.Candidate.objects.all().filter(application__pk__exact=request.POST['application']).values('aadhar')] :
				return redirect('fault', fault='Entered AADHAR number is already registered')
			else:
				return redirect('fault', fault='Server Error')
	else:

		form = forms.CandidateForm(pk=pk)
		return render(request, 'admission/add-candidate.html', {'form':form})



def view_candidate(request, pk):

	admin_all = [u['user'] for u in acc_models.AdminUser.objects.all().values('user')]
	frontend_all = [u['user'] for u in acc_models.FrontEndUser.objects.all().values('user')]
	if request.user.pk in admin_all or request.user.pk in frontend_all:
		candidate_list = models.Candidate.objects.all().filter(application__pk__exact=pk)
		return render(request, 'admission/view-candidate.html', {'candidate_list':candidate_list})
	else:
		return redirect('fault', fault='ACCESS DENIED!')


<<<<<<< HEAD
def view_application_list(request):

	application_list = models.Application.objects.all().filter(is_active__exact=True)
	return render(request, 'admission/view-application-list.html', {'application_list':application_list} )


def view_application_details(request ,pk):

	try:
		application = models.Application.objects.get(pk__exact=pk, is_active__exact=True)
		return render(request, 'admission/view-application-details.html', {'application':application})
	except:
		return redirect('fault', fault="Server Error")

""" 
def edit_application(request, pk):

	if request.method == 'POST':
		form = forms.EditApplicationForm(data=request.POST, files=request.FILES, pk=pk)
		if form.is_valid():
			application = models.Application.objects.get(pk__exact=pk)
			application.name = form.cleaned_data['name']
			application.year = form.cleaned_data['year']
			application.is_active = form.cleaned_data['is_active']
			application.pdf = form.cleaned_data['pdf']
			application.course_1 = fro_models.Course.objects.get(pk__exact=form.cleaned_data['course_1'])
			application.course_2 = fro_models.Course.objects.get(pk__exact=form.cleaned_data['course_2'])
			application.course_3 = fro_models.Course.objects.get(pk__exact=form.cleaned_data['course_3'])
			application.course_4 = fro_models.Course.objects.get(pk__exact=form.cleaned_data['course_4'])
			application.course_5 = fro_models.Course.objects.get(pk__exact=form.cleaned_data['course_5'])
			application.course_6 = fro_models.Course.objects.get(pk__exact=form.cleaned_data['course_6'])
			application.course_7 = fro_models.Course.objects.get(pk__exact=form.cleaned_data['course_7'])
			application.course_8 = fro_models.Course.objects.get(pk__exact=form.cleaned_data['course_8'])
			application.course_9 = fro_models.Course.objects.get(pk__exact=form.cleaned_data['course_9'])
			application.course_10 = fro_models.Course.objects.get(pk__exact=form.cleaned_data['course_10'])
			application.course_11 = fro_models.Course.objects.get(pk__exact=form.cleaned_data['course_11'])
			application.course_12 = fro_models.Course.objects.get(pk__exact=form.cleaned_data['course_12'])
			application.course_13 = fro_models.Course.objects.get(pk__exact=form.cleaned_data['course_13'])
			application.course_14 = fro_models.Course.objects.get(pk__exact=form.cleaned_data['course_14'])
			application.course_15 = fro_models.Course.objects.get(pk__exact=form.cleaned_data['course_15'])
			try:
				application.save()
			except:
				return redirect('fault', fault='Server Error')
			return redirect('success', success='Application data changed successfully')
	else:
		form = forms.EditApplicationForm(pk=pk)
		return render(request, 'admission/add-application.html', {'form':form})
 """


def delete_application(request, pk):

	
	try:
		models.Application.objects.get(pk__exact=pk).delete()
		return redirect('admission:view_application_list')
	except:
		return redirect('fault', fault="Some error occured")
	
=======

def view_candidate_application(request, pk):

	admin_all = [u['user'] for u in acc_models.AdminUser.objects.all().values('user')]
	frontend_all = [u['user'] for u in acc_models.FrontEndUser.objects.all().values('user')]
	if request.user.pk in admin_all or request.user.pk in frontend_all:
		try:
			candidate = models.Candidate.objects.get(pk__exact=pk)
		except:
			return redirect('fault', fault='Server Error')
		return render(request, 'admission/view-candidate-application.html', {'candidate':candidate})

	else:
		return redirect('fault', fault='ACCESS DENIED!')






def print_candidate_application(request, pk):

	admin_all = [u['user'] for u in acc_models.AdminUser.objects.all().values('user')]
	frontend_all = [u['user'] for u in acc_models.FrontEndUser.objects.all().values('user')]
	if request.user.pk in admin_all or request.user.pk in frontend_all:
		try:
			candidate = models.Candidate.objects.get(pk__exact=pk)
		except:
			return redirect('fault', fault='Server Error')
		# return render(request, 'admission/view-candidate-application.html', {'candidate':candidate})

		response = HttpResponse(content_type='application/pdf')
		response['Content-Disposition'] = f'attachment; filename="{candidate.application_no}.pdf" '
		buffer = BytesIO()
		p = canvas.Canvas(buffer, bottomup=0)
		width_A4, height_A4 = A4



		p.saveState()
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		temp = fro_models.HomeImage.objects.get(id__exact=1).logo_image.name
		logo_path = os.path.join(BASE_DIR, f'media/{temp}')
		logo = ImageReader(logo_path)
		p.scale(1,-1)
		p.drawImage(logo, inch/3, -inch/3, 100, -100)
		p.restoreState()


		p.setFont("Helvetica", 20)
		org_name = 'JP Institute of Engineering and Technology'
		org_name_width = stringWidth(org_name, "Helvetica", 20)
		p.drawString(((width_A4+100-org_name_width)/2), 50 , org_name)

		p.setFont("Helvetica", 15)
		org_add1 = 'College Code : 282'
		org_add1_width = stringWidth(org_add1, "Helvetica", 15)
		p.drawString(((width_A4+100-org_add1_width)/2), 80 , org_add1)

		p.setLineWidth(1)
		p.line(inch/2, 140, width_A4-inch/2,140)



		p.setFont("Helvetica-Bold", 16)
		heading = f"CANDIDATE APPLICATION - {candidate.application.name}"
		heading_width = stringWidth(heading, "Helvetica-Bold", 16)
		p.drawString(((width_A4-heading_width)/2), 180 , heading)

		p.setLineWidth(1)
		p.line(((width_A4-heading_width)/2), 181, ((width_A4-heading_width)/2)+heading_width,181)


		p.setFont("Helvetica-Bold", 12)
		item1_1 = f"Application Number: "
		p.drawString(inch/2, 220, item1_1)
		p.setFont("Helvetica", 12)
		item1_2 = f"{candidate.application_no}"
		p.drawString((inch/2)+stringWidth(item1_1, "Helvetica-Bold", 12), 220, item1_2)


		p.setFont("Helvetica-Bold", 12)
		item2_1 = f"Name: "
		p.drawString(width_A4/2, 220, item2_1)
		p.setFont("Helvetica", 12)
		item2_2 = f"{candidate.name}"
		p.drawString((width_A4/2)+stringWidth(item2_1, "Helvetica-Bold", 12), 220, item2_2)


		p.setFont("Helvetica-Bold", 12)
		item3_1 = f"Father's name: "
		p.drawString(inch/2, 240, item3_1)
		p.setFont("Helvetica", 12)
		item3_2 = f"{candidate.father_name}"
		p.drawString((inch/2)+stringWidth(item3_1, "Helvetica-Bold", 12), 240, item3_2)


		p.setFont("Helvetica-Bold", 12)
		item4_1 = f"Mother's Name: "
		p.drawString(width_A4/2, 240, item4_1)
		p.setFont("Helvetica", 12)
		item4_2 = f"{candidate.mother_name}"
		p.drawString((width_A4/2)+stringWidth(item4_1, "Helvetica-Bold", 12), 240, item4_2)


		p.setFont("Helvetica-Bold", 12)
		item5_1 = f"Date of Birth: "
		p.drawString(inch/2, 260, item5_1)
		p.setFont("Helvetica", 12)
		item5_2 = f"{candidate.dob}"
		p.drawString((inch/2)+stringWidth(item5_1, "Helvetica-Bold", 12), 260, item5_2)


		p.setFont("Helvetica-Bold", 12)
		item6_1 = f"AADHAR Number: "
		p.drawString(width_A4/2, 260, item6_1)
		p.setFont("Helvetica", 12)
		item6_2 = f"{candidate.aadhar}"
		p.drawString((width_A4/2)+stringWidth(item6_1, "Helvetica-Bold", 12), 260, item6_2)


		p.setFont("Helvetica-Bold", 12)
		item7_1 = f"Gender: "
		p.drawString(inch/2, 280, item7_1)
		p.setFont("Helvetica", 12)
		item7_2 = f"{candidate.gender}"
		p.drawString((inch/2)+stringWidth(item7_1, "Helvetica-Bold", 12), 280, item7_2)


		p.setFont("Helvetica-Bold", 12)
		item8_1 = f"Nationality: "
		p.drawString(width_A4/2, 280, item8_1)
		p.setFont("Helvetica", 12)
		item8_2 = f"{candidate.nationality}"
		p.drawString((width_A4/2)+stringWidth(item8_1, "Helvetica-Bold", 12), 280, item8_2)


		p.setFont("Helvetica-Bold", 12)
		item9_1 = f"Email: "
		p.drawString(inch/2, 300, item9_1)
		p.setFont("Helvetica", 12)
		item9_2 = f"{candidate.email}"
		p.drawString((inch/2)+stringWidth(item9_1, "Helvetica-Bold", 12), 300, item9_2)


		p.setFont("Helvetica-Bold", 12)
		item10_1 = f"Contact Number: "
		p.drawString(width_A4/2, 300, item10_1)
		p.setFont("Helvetica", 12)
		item10_2 = f"{candidate.phn}"
		p.drawString((width_A4/2)+stringWidth(item10_1, "Helvetica-Bold", 12), 300, item10_2)


		p.setFont("Helvetica-Bold", 12)
		item11_1 = f"Father's Occupation: "
		p.drawString(inch/2, 320, item11_1)
		p.setFont("Helvetica", 12)
		item11_2 = f"{candidate.father_occupation}"
		p.drawString((inch/2)+stringWidth(item11_1, "Helvetica-Bold", 12), 320, item11_2)


		p.setFont("Helvetica-Bold", 12)
		item12_1 = f"Father's Income: "
		p.drawString(width_A4/2, 320, item12_1)
		p.setFont("Helvetica", 12)
		item12_2 = f"{candidate.father_income}"
		p.drawString((width_A4/2)+stringWidth(item12_1, "Helvetica-Bold", 12), 320, item12_2)


		p.setFont("Helvetica-Bold", 14)
		head_10 = f"Class 10th Details"
		heading_width = stringWidth(head_10, "Helvetica-Bold", 14)
		p.drawString(inch/2, 360, head_10)


		p.setLineWidth(1)
		p.line((inch/2), 361, (inch/2)+heading_width,361)


		p.setFont("Helvetica-Bold", 12)
		item13_1 = f"Roll number: "
		p.drawString(inch/2, 380, item13_1)
		p.setFont("Helvetica", 12)
		item13_2 = f"{candidate.roll_10}"
		p.drawString((inch/2)+stringWidth(item13_1, "Helvetica-Bold", 12), 380, item13_2)


		p.setFont("Helvetica-Bold", 12)
		item14_1 = f"Aggregate Score: "
		p.drawString(width_A4/3, 380, item14_1)
		p.setFont("Helvetica", 12)
		item14_2 = f"{candidate.aggregate_10}"
		p.drawString((width_A4/3)+stringWidth(item14_1, "Helvetica-Bold", 12), 380, item14_2)


		p.setFont("Helvetica-Bold", 12)
		item15_1 = f"PCM Score: "
		p.drawString(0.67*width_A4, 380, item15_1)
		p.setFont("Helvetica", 12)
		item15_2 = f"{candidate.pcm_10}"
		p.drawString((0.67*width_A4)+stringWidth(item15_1, "Helvetica-Bold", 12), 380, item15_2)


		p.setFont("Helvetica-Bold", 14)
		head_10 = f"Class 12th Details"
		heading_width = stringWidth(head_10, "Helvetica-Bold", 14)
		p.drawString(inch/2, 420, head_10)


		p.setLineWidth(1)
		p.line((inch/2), 421, (inch/2)+heading_width, 421)


		p.setFont("Helvetica-Bold", 12)
		item16_1 = f"Roll number: "
		p.drawString(inch/2, 440, item16_1)
		p.setFont("Helvetica", 12)
		item16_2 = f"{candidate.roll_12}"
		p.drawString((inch/2)+stringWidth(item16_1, "Helvetica-Bold", 12), 440, item16_2)


		p.setFont("Helvetica-Bold", 12)
		item17_1 = f"Aggregate Score: "
		p.drawString(width_A4/3, 440, item17_1)
		p.setFont("Helvetica", 12)
		item17_2 = f"{candidate.aggregate_12}"
		p.drawString((width_A4/3)+stringWidth(item17_1, "Helvetica-Bold", 12), 440, item17_2)


		p.setFont("Helvetica-Bold", 12)
		item18_1 = f"PCM Score: "
		p.drawString(0.67*width_A4, 440, item18_1)
		p.setFont("Helvetica", 12)
		item18_2 = f"{candidate.pcm_12}"
		p.drawString((0.67*width_A4)+stringWidth(item18_1, "Helvetica-Bold", 12), 440, item18_2)


		p.setFont("Helvetica-Bold", 14)
		head_10 = f"UPSEE Details"
		heading_width = stringWidth(head_10, "Helvetica-Bold", 14)
		p.drawString(inch/2, 480, head_10)


		p.setLineWidth(1)
		p.line((inch/2), 481, (inch/2)+heading_width, 481)


		p.setFont("Helvetica-Bold", 12)
		item19_1 = f"Roll number: "
		p.drawString(inch/2, 500, item19_1)
		p.setFont("Helvetica", 12)
		item19_2 = f"{candidate.roll_upsee}"
		p.drawString((inch/2)+stringWidth(item19_1, "Helvetica-Bold", 12), 500, item19_2)


		p.setFont("Helvetica-Bold", 12)
		item20_1 = f"General Rank: "
		p.drawString(width_A4/3, 500, item20_1)
		p.setFont("Helvetica", 12)
		item20_2 = f"{candidate.gen_rank}"
		p.drawString((width_A4/3)+stringWidth(item20_1, "Helvetica-Bold", 12), 500, item20_2)


		p.setFont("Helvetica-Bold", 12)
		item21_1 = f"Category Rank: "
		p.drawString(0.67*width_A4, 500, item21_1)
		p.setFont("Helvetica", 12)
		item21_2 = f"{candidate.cat_rank}"
		p.drawString((0.67*width_A4)+stringWidth(item21_1, "Helvetica-Bold", 12), 500, item21_2)


		p.setFont("Helvetica-Bold", 14)
		head_10 = f"Branch Preferences"
		heading_width = stringWidth(head_10, "Helvetica-Bold", 14)
		p.drawString(inch/2, 540, head_10)


		p.setLineWidth(1)
		p.line((inch/2), 542, (inch/2)+heading_width, 542)

		add_height=0

		if candidate.branch_1:
			p.setFont("Helvetica-Bold", 12)
			item22_1 = f"Preference 1: "
			p.drawString(inch/2, 560, item22_1)
			p.setFont("Helvetica", 12)
			item22_2 = f"{candidate.branch_1}"
			p.drawString((inch/2)+stringWidth(item22_1, "Helvetica-Bold", 12), 560, item22_2)
			add_height = 560


		if candidate.branch_2:
			p.setFont("Helvetica-Bold", 12)
			item23_1 = f"Preference 2: "
			p.drawString(inch/2, 580, item23_1)
			p.setFont("Helvetica", 12)
			item23_2 = f"{candidate.branch_2}"
			p.drawString((inch/2)+stringWidth(item23_1, "Helvetica-Bold", 12), 580, item23_2)
			add_height = 580


		if candidate.branch_3:
			p.setFont("Helvetica-Bold", 12)
			item24_1 = f"Preference 3: "
			p.drawString(inch/2, 600, item24_1)
			p.setFont("Helvetica", 12)
			item24_2 = f"{candidate.branch_3}"
			p.drawString((inch/2)+stringWidth(item24_1, "Helvetica-Bold", 12), 600, item24_2)
			add_height = 600


		if candidate.branch_4:
			p.setFont("Helvetica-Bold", 12)
			item25_1 = f"Preference 4: "
			p.drawString(inch/2, 620, item25_1)
			p.setFont("Helvetica", 12)
			item25_2 = f"{candidate.branch_4}"
			p.drawString((inch/2)+stringWidth(item25_1, "Helvetica-Bold", 12), 620, item25_2)
			add_height = 620



		p.setFont("Helvetica-Bold", 14)
		head_10 = f"Correspondance Address"
		heading_width = stringWidth(head_10, "Helvetica-Bold", 14)
		p.drawString(inch/2, add_height+40, head_10)


		p.setLineWidth(1)
		p.line((inch/2), add_height+41, (inch/2)+heading_width, add_height+41)

		style = ParagraphStyle(name='Normal', fontName = 'Helvetica', fontSize = 12, firstLineIndent = heading_width+5, leading=16)
		corr_add = Paragraph(f'{candidate.corr_add}', style)
		w,h = corr_add.wrap(width_A4-inch,height_A4-add_height-40)
		corr_add.drawOn(p,inch/2,add_height+36-h+style.leading)

		add_height = add_height+40+h

		p.setFont("Helvetica-Bold", 14)
		head_10 = f"Permanent Address"
		heading_width = stringWidth(head_10, "Helvetica-Bold", 14)
		p.drawString(inch/2, add_height+40, head_10)


		p.setLineWidth(1)
		p.line((inch/2), add_height+41, (inch/2)+heading_width, add_height+41)


		style = ParagraphStyle(name='Normal', fontName = 'Helvetica', fontSize = 12, firstLineIndent = heading_width+5, leading=16)
		perm_add = Paragraph(f'{candidate.perm_add}', style)
		w,h = perm_add.wrap(width_A4-inch,height_A4-add_height-40)
		perm_add.drawOn(p,inch/2,add_height+36-h+style.leading)




		p.showPage()
		p.save()
		pdf = buffer.getvalue()
		buffer.close()
		response.write(pdf)

		return response



	else:
		return redirect('fault', fault='ACCESS DENIED!')

>>>>>>> origin/phase1
