#Own Created File
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps =  request.GET.get('upper', 'off')
    newline =  request.GET.get('new_line_remover', 'off')

    punctuation = ''' !()-[]{};:'"/|\,<>?.@#$%^&*_~` '''
    analyzed = ""
    if removepunc == 'on':
        for char in djtext:
            if char not in punctuation:
                analyzed += char

    if fullcaps =='on':
        analyzed = analyzed.upper()

    ans = ""
    if newline == 'on':
        for char in analyzed:
            if char != "\n" and char != '\r':
                ans += char

    params = {'purpose':'#no_wait', 'analyzed_text': ans  }
    return render(request, "analyze.html", params)


def about(request):
    return HttpResponse('Inside About')

def charCount(request):
    return HttpResponse('Inside charCount')

def capitalize(request):
    return HttpResponse('Inside capitalize')

def newLineRemove(request):
    return HttpResponse('Inside New Line Remove')

def spaceRemove(request):
    return HttpResponse('Inside space Remove')


