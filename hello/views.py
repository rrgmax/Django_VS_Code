from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")

# You can also remove the import re statement that's no longer used

def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # BAD CODE! Avoid inline HTML for security reason, plus templates automatically escape HTML content.
    content = "<strong>Hello there, " + name + "!</strong> It's " + formatted_now

    return render(
        request,
        'hello/hello_there.html',
        {
            'title': 'Hello, Django',
            'content': content,
        }
    )
    