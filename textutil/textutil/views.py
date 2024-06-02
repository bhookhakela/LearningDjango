from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'index.html')
def cap(request):
    return HttpResponse('''
                        <button type="button"><a href="/">Back</a></button>
                        <br>
                        <br>
                        &emsp;&emsp;&emsp;Capitalize the first letter
                        ''')
def rempunc(request):
    homedata=request.GET.get('data', 'default')
    print(homedata)
    # homedata should be processed and returned
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