from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from django.template.loader import render_to_string

def index(request):

	if request.method == 'POST':
		message = request.POST['message']
		context = {'name':'Dennis', 'email':'dennis@ivpath.com',  'message':message}
		template = render_to_string('app/email_template.html', context)

		send_mail('Contact Form',
		 template, 
		 settings.EMAIL_HOST_USER,
		 ['ivanovsin11@gmail.com'], 
		 fail_silently=False)
	return render(request, 'app/index.html')
