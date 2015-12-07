from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import SearchForm
import requests
from elasticsearch import Elasticsearch
import demjson

# Create your views here.
def home(request):
	title = "Welcome to Searching information "
	form = SearchForm(request.POST or None)
	answer= ""

	#add a form
	#res = requests.get('http://localhost:9200')
	
	context = {
		"title": title,
		"form": form,
		"answer": answer
	}

	


	if form.is_valid():
		form_search = form.cleaned_data.get("search")
		
		#do some thing that searches for what was submitted
		#connnect to the elasticsearch cluster
		es = Elasticsearch([{'host': '52.34.82.61', 'port': 9200}])
		
		# i=2
		# res = requests.get('http://swapi.co/api/people/2')

		# while res.status_code==200:

		# 	es.index(index='sw', doc_type='people', id=i, body=res.content)
		# 	res = requests.get('http://swapi.co/api/people/' + str(i))
		# 	i=i+1
		

		# res = requests.get('http://swapi.co/api/people/2')
		# i=18
		# while res.status_code==200:

		# 	es.index(index='sw', doc_type='people', id=i, body=res.content)
		# 	res = requests.get('http://swapi.co/api/people/' + str(i))


		#res = requests.get('http://swapi.co/api/people/1')
		p = es.search(index="sw", body={"query": {"match": {'name':form_search}}})

		answer = p['hits']['hits']# can get you the score
		answer = answer[0]['_source']

		#pyData = demjson.decode(res.content)
		# 	title = "My Title %s" %(request.user)
		context = {
			"title": "you searched for %s" %(answer['name']),
			"answer": "result eye color : %s  result gender: %s" %(answer['eye_color'], answer['gender'])

		}


	return render(request, "forms.html",context)


# example for how to do forms
def contact(request):
	form = ContactForm(request.POST or None)
			
	context = {
		"form": form,
	}

	return render(request, "home.html", context)