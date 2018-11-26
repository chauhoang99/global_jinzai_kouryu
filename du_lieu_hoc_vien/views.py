from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def data_entry_main_page(request):
    return render(request, 'data-entry/mainpage.html')


@login_required
def entry_class(request):
    return render(request, 'data-entry/class.html')


@login_required
def entry_save(request):
    input(request.POST)
    return render(request, 'data-entry/mainpage.html')
