from django.http import HttpResponse
from django.shortcuts import render
from string import punctuation
def home(request):
    return render(request,'index.html')
def analyze(request):
    homedata=request.GET.get('data', 'default')
    removepunc=request.GET.get('rempunc', 'off')
    print(homedata)
    print(removepunc)
    output=''
    if removepunc=='on':
        for char in homedata:
            if char not in punctuation:
                output+=char
    else:
        output=homedata
    param = {'purpose': removepunc, 'analyzed_text': output}
    return render(request,'analyze.html', param)
