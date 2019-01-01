from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    # return render(request, 'home.html')
    return HttpResponseRedirect('/admin')
