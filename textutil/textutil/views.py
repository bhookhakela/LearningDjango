from django.http import HttpResponse
def home(request):
    return HttpResponse('''<button type="button"><a href="/cap/">Capitalize</a></button>
                            <br>
                            <br>
                            <button type="button"><a href="/rempunc/">Remove Punctuation</a></button>
                            <br>
                            <br>
                            <button type="button"><a href="/remnewline/">Remove NewLine</a></button>
                            <br>
                            <br>
                            <button type="button"><a href="/remspace/">Remove Space</a></button>
                        ''')
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