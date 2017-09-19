# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    print 'here is a webpage'
    if 'entries' not in request.session:
        request.session['entries'] = []
        print 'entries:'
        print request.session['entries']
    context = {
        'entries': request.session['entries'],
    }
    return render(request,'words/words.html', context)
def process(request):
    print request.POST['word']
    print request.POST['color']
    print request.POST['size']
    word = request.POST['word']
    color = request.POST['color']
    size = request.POST['size']
    entry = {
        'words' : word,
        'color' : color,
        'size' : size,
    }
    temp = request.session['entries']
    temp.append(entry)
    request.session['entries']=temp
    print request.session['entries']
    return redirect('/session_words')
def reset(request):
    del request.session['entries']
    return redirect('/session_words')