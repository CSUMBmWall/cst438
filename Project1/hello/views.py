from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import SearchForm
# Create your views here.
def home(request):
	title = "Welcome"
	# if request.user.is_authenticated():
	# 	title = "My Title %s" %(request.user)
	form = SearchForm(request.POST or None)
	#add a form
	context = {
		"title": title,
		"form": form
	}


	
	return render(request, "home.html",context)



def contact(request):
	form = ContactForm(request.POST or None)
			
	context = {
		"form": form,
	}

	return render(request, "forms.html", context)