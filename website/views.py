from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		#do stuff
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']
		# send email
		send_mail(
			message_name,  #subject
			message, #message
			message_email,  # from email
			['rorfolx@gmail.com'], # to email
			fail_silently=False,
			)
		return render(request, 'contact.html', {'message_name': message_name})


	else:
		#return page
		return render(request, 'contact.html', {})
