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

		#delete from nodes
		#i=1
		#while res.status_code==200:
		#	es.delete(index='pk', doc_type='pokemon', id=i)
		#	i+=1



		#max_score None then its the other one
		# search = "pokemon"
		# p = es.search(index="pk", body={"query": {"match": {'name':form_search}}})
		# if(p['hits']['total']==0):
		# 	p=es.search(index="sw", body={"query": {"match": {'name':form_search}}})
		# 	search ="starwars"
		
		# if(p['hits']['total']==0):
		# 	context = {
		# 	"answer": "No results",

		# 	}
		# 	search="fail"
		# else:
		# 	answer = p['hits']['hits']# can get you the score
		# 	answer = answer[0]['_source']

		poke = es.search(index="pk", body={"query": {"match": {'name':form_search}}})
		star = es.search(index="sw", body={"query": {"match": {'name':form_search}}})
		pokelike = es.search(index="pk", body={"query": {"prefix": {'name':form_search}}})
		#starlike = es.search(index="sw", body={"query": {"fuzzy_like_this_field" : { "name" : {"like_text": form_search, "max_query_terms":5}}}})
		#pyData = demjson.decode(res.content)
		# 	title = "My Title %s" %(request.user)
		if(poke['hits']['total']!=0):
			answer=poke['hits']['hits'][0]['_source']
			context = {
				"title": "you searched for %s" %(answer['name']),
				#"answer": "result eye color : %s  result gender: %s" %(answer['eye_color'], answer['gender']),
				"answer": "result height: %s  type: %s" %(answer['height'], answer['types'][0]['name'])

			}
		elif(star['hits']['total']!=0):
			answer=star['hits']['hits'][0]['_source']
			context = {
				"title": "you searched for %s" %(answer['name']),
				"answer": "result eye color : %s  result gender: %s" %(answer['eye_color'], answer['gender']),
				#"answer": "result height: %s  type: %s" %(answer['height'], answer['types'][0]['name'])
				
			}
		elif(pokelike['hits']['total']!=0):
			answer=pokelike['hits']['hits'][0]['_source']
			context = {
				"title": "you searched for %s" %(answer['name']),
				#"answer": "result eye color : %s  result gender: %s" %(answer['eye_color'], answer['gender']),
				"answer": "result height: %s  type: %s" %(answer['height'], answer['types'][0]['name'])
				
			}
		# elif(starlike['hits']['total']!=0):
		# 	answer=starlike['hits']['hits'][0]['_source']
		# 	context = {
		# 		"title": "you searched for %s" %(answer['name']),
		# 		"answer": "result eye color : %s  result gender: %s" %(answer['eye_color'], answer['gender']),
		# 		#"answer": "result height: %s  type: %s" %(answer['height'], answer['types'][0]['name'])
				
		# 	}
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
		p = es.search(index="sw", body={"query": {"match": {'name':form_search}}})
		pyData = demjson.decode(p.content)
		context = {
			"title": "you searched for %s" %(pyData),
		}

	return render(request, "answer.html",context)