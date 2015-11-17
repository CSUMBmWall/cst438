from django import forms



class SearchForm(forms.Form):
	search = forms.CharField()
	#title = forms.CharField()
	#year = forms.CharField()

	def cleaned_search(self):
		full_search = self.cleaned.data.get('search')
		#dont store nulls in database
		return full_search