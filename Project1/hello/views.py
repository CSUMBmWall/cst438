from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import SearchForm
import requests
from elasticsearch import Elasticsearch
from models import pokeTypeFormatter

# Create your views here.
def home(request):
	title = "Welcome to Searching information "
	form = SearchForm(request.POST or None)
	answer= ""
	innefective=""
	superEffective=""
	resistance=""
	everything=""

	#add a form
	#res = requests.get('http://localhost:9200')
	
	context = {
		"title": title,
		"form": form,
		"answer": answer,
		"innefective":innefective,
		"superEffective":superEffective,
		"resistance":resistance,
		"all": everything

	}

	if form.is_valid():
		form_search = form.cleaned_data.get("search")
		
		#do some thing that searches for what was submitted
		#connnect to the elasticsearch cluster
		es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
		
		
		#i=1
		#res = requests.get('http://swapi.co/api/people/1')

		#while res.status_code==200:
		#	es.index(index='sw', doc_type='people', id=i, body=res.content)
		#	res = requests.get('http://swapi.co/api/people/' + str(i))
		#	i=i+1
		

		#res = requests.get('http://swapi.co/api/people/18')
		#i=18
		#while res.status_code==200:
		#	es.index(index='sw', doc_type='people', id=i, body=res.content)
		#	res = requests.get('http://swapi.co/api/people/' + str(i))
		#	i=i+1


		#res = requests.get('http://swapi.co/api/people/1')


		#adding pokemon
		#i=1
		#res = requests.get('http://pokeapi.co/api/v1/pokemon/' + str(i))

		#while res.status_code==200:
		#	es.index(index='pk', doc_type='pokemon', id=i, body=res.content)
		#	res = requests.get('http://pokeapi.co/api/v1/pokemon/' + str(i))
		#	i=i+1
		#http://pokeapi.co/api/v1/pokemon/i
		#max=718

		#i=1
		#res = requests.get('http://pokeapi.co/api/v1/type/' + str(i))

		#while res.status_code==200:
		#	es.index(index='type', doc_type='pokemon', id=i, body=res.content)
		#	res = requests.get('http://pokeapi.co/api/v1/type/' + str(i))
		#	i=i+1

		#delete from nodes
		#i=1
		#while res.status_code==200:
		#	es.delete(index='pk', doc_type='pokemon', id=i)
		#	i+=1


		# 3 doc_types (pokemon,type,people)



		poke = es.search(index="pk", body={"query": {"match": {'name':form_search}}})
		#poke = es.search(body={"query": {"query_string": {"query":form_search, "fields": ["name"]}}})



		star = es.search(index="sw", body={"query": {"match": {'name':form_search}}})
		pokelike = es.search(index="pk", body={"query": {"prefix": {'name':form_search}}})
		starlike = es.search(body={"query": {"prefix" : { "name" : form_search}}})

		#pyData = demjson.decode(res.content)
		# 	title = "My Title %s" %(request.user)
		if(poke['hits']['total']!=0):
			answer=poke['hits']['hits'][0]['_source']
			second=poke['hits']['hits'][0]['_source']['types'][0]['name']
			temp=pokeTypeFormatter(second)
			# check how to go over more than one type and cycle through the innefective
			pokeType= es.search(index="type", body={"query": {"match": {'name':second}}})
			
			innefective = pokeType['hits']['hits'][0]['_source']['ineffective']
			superEffective = pokeType['hits']['hits'][0]['_source']['super_effective']
			resistance =pokeType['hits']['hits'][0]['_source']['resistance']
			items = pokeType['hits']['hits'][0]['_source']['super_effective']

			context = {
				"title": "you searched for %s" %(answer['name']),
				"type":answer['types'],
				"innefective":innefective,
				"superEffective":superEffective,
				"resistance":resistance,
				"all":"all: %s" %(pokeType['hits']['hits'][0]['_source']),
				"items": temp,
				"doing":1

			}
		elif(star['hits']['total']!=0):
			answer=star['hits']['hits'][0]['_source']
			context = {
				"title": "you searched for %s" %(answer['name']),
				"answer": answer,
				#"answer": "result height: %s  type: %s" %(answer['height'], answer['types'][0]['name'])
				"doing":2,
				
			}
		elif(pokelike['hits']['total']!=0):
			answer=pokelike['hits']['hits'][0]['_source']
			context = {
				"title": "you searched for %s" %(answer['name']),
				#"answer": "result eye color : %s  result gender: %s" %(answer['eye_color'], answer['gender']),
				"answer": answer,
				"doing":3,				
			}
		elif(starlike['hits']['total']!=0):
			answer=starlike['hits']['hits'][0]['_source']
			context = {
				"title": "you searched for %s" %(answer['name']),
				"answer": "result eye color : %s  result gender: %s" %(answer['eye_color'], answer['gender']),
				#"answer": "result height: %s  type: %s" %(answer['height'], answer['types'][0]['name'])
				
			}
		else:
			context ={"answer":"no result"}
	return render(request, "home.html",context)




def answer(request):
	title = "Welcome to Searching information "
	form = SearchForm(request.POST or None)
	answer= ""

	context = {
		"title": title,
		"form": form,
		"answer": answer
	}

	if form.is_valid():
		form_search = form.cleaned_data.get("search")
		
		es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

		poke = es.search(index="pk", body={"query": {"match": {'name':form_search}}})
		
		answer=poke['hits']['hits'][0]['_source']
		context = {
			"title": "you searched for %s" %(answer['name']),
			#"answer": "result eye color : %s  result gender: %s" %(answer['eye_color'], answer['gender']),
			"answer": "result : %s" %(poke['hits'])

		}
	
	return render(request, "answer.html",context)




from models import todo
from django.shortcuts import render_to_response
 
def index(request): #Define our function, accept a request
 
    items = todo.objects.all() #ORM queries the database for all of the to-do entries.
 
    return render_to_response('index.html', {'items': items})