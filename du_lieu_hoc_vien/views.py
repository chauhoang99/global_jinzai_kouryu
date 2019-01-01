from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
import json
from .tasks import *


# @login_required
# def data_entry_main_page(request):
#     table_to_open = request.GET.get('table')
#     if not table_to_open:
#         return render(request, 'data-entry/mainpage.html')
#     elif table_to_open == 'class':
#         return render(request, 'data-entry/class.html')
#     elif table_to_open == 'teacher':
#         return render(request, 'data-entry/teacher.html')
#     elif table_to_open == 'student':
#         return render(request, 'data-entry/student.html')
#     elif table_to_open == 'degree':
#         return render(request, 'data-entry/degree.html')
#     elif table_to_open == 'employer':
#         return render(request, 'data-entry/employer.html')
#     elif table_to_open == 'jobs':
#         return render(request, 'data-entry/jobs.html')
#
#
# @login_required
# def entry_save(request):
#     entry_to = request.POST.get('data_of')
#     data = json.loads(request.POST.get('data'))
#     input_by = request.user
#
#     if entry_to == 'ClassInfo':
#         class_info_entry(data, input_by)
#     elif entry_to == 'Teacher':
#         teacher_entry(data, input_by)
#     elif entry_to == 'Student':
#         student_entry(data, input_by)
#     elif entry_to == 'Employer':
#         employer_entry(data, input_by)
#     else:
#         pass
#     return HttpResponse("")
