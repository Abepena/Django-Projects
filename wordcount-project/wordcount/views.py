from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, "index.html")


def count(request):
    fulltext = request.GET["fulltext"]
    wordlist = fulltext.strip().split()
    count = len(wordlist)

    word_dict = {}
    for word in wordlist:
        if word in word_dict:
            # Increase
            word_dict[word] += 1
        else:
            # Add to disctionary
            word_dict[word] = 1
        sorted_words = sorted(
            word_dict.items(), key=lambda elem: elem[1], reverse=True
        )
    print(sorted_words)

    return render(
        request,
        "count.html",
        {"fulltext": fulltext, "count": count, "sorted_words": sorted_words},
    )
