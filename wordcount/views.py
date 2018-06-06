# views

from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    # return HttpResponse('Hello Zia')
      return render(request, 'home.html', {'Name': 'I am Mohammed Zia'})

def eggs(request):
	return HttpResponse('I like eggs!!')

def count(request):
	get_fulltext = request.GET['fulltext']
	# print(get_fulltext)

	words = get_fulltext.split()
	no_of_words = len(words)

	wordsdictionary = {}

	for word in words:
		if word in wordsdictionary:
			wordsdictionary[word] += 1
		else:
			wordsdictionary[word] = 1

	sortedwords = sorted(wordsdictionary.items(), key=operator.itemgetter(1), reverse=True)

	return render(request, 'count.html', {'fulltext': get_fulltext, 'no_of_words': no_of_words, 'wordsdictionary':sortedwords})
