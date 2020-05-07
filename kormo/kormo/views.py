from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponse, get_object_or_404


def index(request):
    return render(request, 'index.html')


def jobList(request):
    return render(request, 'jobList.html')
def contact(request):
    return render(request, 'contact.html')

def login(request):
    context = {}
    if request.method == "POST":
        username = request.post['username']
        password = request.post['password']
        user = authenticate(request, username=username, password=password)
        if user.is_valid:
            login(request, user)
            return HttpResponseRedirect(reversed('jobList.html'))
        else:
            context["error"] = "Provide a valid password and email"
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html', context)


def signup(request):
    return render(request, 'signup.html')


def handleSignup(request):
    return render(request, 'signup.html')
