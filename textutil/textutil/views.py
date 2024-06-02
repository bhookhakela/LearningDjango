from django.http import HttpResponse
from django.shortcuts import render
from string import punctuation
def home(request):
    return render(request,'index.html')
def analyze(request):
    homedata=request.GET.get('data', 'default')
    removepunc=request.GET.get('rempunc', 'off')
    caps=request.GET.get('caps', 'off')
    remnewline=request.GET.get('remnewline', 'off')
    output=''
    if removepunc=='on':
        for char in homedata:
            if char not in punctuation:
                output+=char
    else:
        output=homedata
    if caps=='on':
        output=output.upper()
    final=''
    if remnewline=='on':
        for char in output:
            if char is not '\n':
                final+=char
    else:
        final=output

    param = {'rempunc': removepunc,'caps': caps,'remnewline': remnewline, 'analyzed_text': final}
    return render(request,'analyze.html', param)
