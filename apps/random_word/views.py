# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
        request.session['word'] = 'random_word'
        print 'setting session variables'
    context = {
        'count': request.session['count'],
        'word': request.session['word'],
    }
    print context
    return render(request, 'random_word/word.html', context)
def generate(request):
    if request.method == 'POST':
        request.session['count'] = request.session['count'] + 1
        request.session['word'] = get_random_string(length=14)
    print 'generating...'
    return redirect('/')
def reset(request):
    del request.session['count']
    del request.session['word']
    return redirect('/')
