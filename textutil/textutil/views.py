from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    parameters = {'name': 'Harsh','place': 'Thane'}
    return render(request,'index.html',parameters)
def cap(request):
    return HttpResponse('''
                        <button type="button"><a href="/">Back</a></button>
                        <br>
                        <br>
                        &emsp;&emsp;&emsp;Capitalize the first letter
                        ''')
def rempunc(request):
    return HttpResponse('''
                        <button type="button"><a href="/">Back</a></button>
                        <br>
                        <br>
                        &emsp;&emsp;&emsp;Remove the punctuation
                        ''')
def remnewline(request):
    return HttpResponse('''
                        <button type="button"><a href="/">Back</a></button>
                        <br>
                        <br>
                        &emsp;&emsp;&emsp;Remove the Newline
                        ''')
def remspace(request):
    return HttpResponse('''
                        <button type="button"><a href="/">Back</a></button>
                        <br>
                        <br>
                        &emsp;&emsp;&emsp;Remove the Space
                        ''')