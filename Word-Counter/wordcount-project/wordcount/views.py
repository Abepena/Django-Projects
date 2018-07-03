from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.strip().split()
    count = len(wordlist)

    word_dict = {}
    for word in wordlist:
        if word in word_dict:
            #Increase
            word_dict[word] += 1
        else:
            #Add to disctionary
            word_dict[word] = 1
    
    return render(request,'count.html',{'fulltext': fulltext,
                                        'count':count,
                                        'word_dict': word_dict.items()})