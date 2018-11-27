from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
import json
import pandas
import datetime
from .models import *


@login_required
def data_entry_main_page(request):
    return render(request, 'data-entry/mainpage.html')


@login_required
def entry_class(request):
    return render(request, 'data-entry/class.html')


@login_required
def entry_save(request):
    entry_to = request.POST.get('data_of')
    if entry_to == 'ClassInfo':
        data = json.loads(request.POST.get('data'))
        data = {'class_name': data.get('class_name'),
                'from_date': data.get('from_date'),
                'to_date': data.get('to_date'),
                'level': data.get('level')}

        data = pandas.DataFrame(data)
        input_by = request.user
        bulk = []
        for index, row in data.iterrows():
            # bulk.append(ClassInfo(class_name=row['class_name'],
            #                       from_date=datetime.date(row['from_date']),
            #                       to_date=datetime.date(row['to_date']),
            #                       level=row['level'],
            #                       input_by=input_by))

            input_data = ClassInfo(class_name=row['class_name'],
                                   from_date=datetime.date(int(row['from_date'].split('-')[0]), int(row['from_date'].split('-')[1]), int(row['from_date'].split('-')[2])),
                                   to_date=datetime.date(int(row['to_date'].split('-')[0]), int(row['to_date'].split('-')[1]), int(row['to_date'].split('-')[2])),
                                   level=row['level'], input_by=input_by, modified_by=input_by)
            input_data.save()
    else:
        pass
    return HttpResponse("")
