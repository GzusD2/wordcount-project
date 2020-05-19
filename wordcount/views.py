from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
	return render(request, 'home.html')

def bacon(request):
	return HttpResponse('<h1>Boy do I love this bacon</h1>')

def about(request):
	return render(request, 'about.html')

def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()

	dictionary = {}

	for word in wordlist:
		if word in dictionary:
			#Increase
			dictionary[word] += 1
		else:
			#Add to dictionary
			dictionary[word] = 1

	sortedWords = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)


	return render(request, 'count.html', {'fulltext':fulltext,'count':len(wordlist),'sortedWords':sortedWords})