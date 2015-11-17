from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import SearchForm
# Create your views here.
def home(request):
	title = "Welcome to Searching information "
	form = SearchForm(request.POST or None)
	answer= "this";
	#add a form
	context = {
		"title": title,
		"form": form,
		"answer": answer
	}


	if form.is_valid():
		form_search = form.cleaned_data.get("search");
		
		#do some thing that searches for what was submitted


		# 	title = "My Title %s" %(request.user)
		context = {
			"title": "you searched for %s" %(form_search)
			#"answer": "BLA BLA BLA"

		}


	return render(request, "forms.html",context)


# example for how to do forms
def contact(request):
	form = ContactForm(request.POST or None)
			
	context = {
		"form": form,
	}

	return render(request, "home.html", context)