import pandas
import datetime
from .models import *


def class_info_entry(data, input_by):
    data = {'class_name': data.get('class_name'),
            'from_date': data.get('from_date'),
            'to_date': data.get('to_date'),
            'level': data.get('level')}

    data = pandas.DataFrame(data)
    bulk = []
    for index, row in data.iterrows():
        bulk.append(ClassInfo(class_name=row['class_name'],
                              from_date=datetime.date(int(row['from_date'].split('-')[0]),
                                                      int(row['from_date'].split('-')[1]),
                                                      int(row['from_date'].split('-')[2])),
                              to_date=datetime.date(int(row['to_date'].split('-')[0]),
                                                    int(row['to_date'].split('-')[1]),
                                                    int(row['to_date'].split('-')[2])),
                              level=row['level'], input_by=input_by, modified_by=input_by))
    ClassInfo.objects.bulk_create(bulk)


def teacher_entry(data, input_by):
    data = {'teacher_name': data.get('teacher_name'),
            'date_of_birth': data.get('date_of_birth'),
            'cmnd': data.get('cmnd'),
            'nationality': data.get('nationality'),
            'address': data.get('address')}

    data = pandas.DataFrame(data)
    bulk = []
    for index, row in data.iterrows():
        bulk.append(
            Teacher(teacher_name=row['teacher_name'],
                    date_of_birth=datetime.date(int(row['date_of_birth'].split('-')[0]),
                                                int(row['date_of_birth'].split('-')[1]),
                                                int(row['date_of_birth'].split('-')[2])),
                    citizen_id=row['cmnd'],
                    nationality=row['nationality'],
                    address=row['address'],
                    input_by=input_by,
                    modified_by=input_by))
    Teacher.objects.bulk_create(bulk)


def student_entry(data, input_by):
    data = {'student_name': data.get('student_name'),
            'date_of_birth': data.get('date_of_birth'),
            'cmnd': data.get('cmnd'),
            'current_japanese_level': data.get('current_japanese_level'),
            'address': data.get('address')}
    data = pandas.DataFrame(data)
    bulk = []
    for index, row in data.iterrows():
        bulk.append(
            Student(student_name=row['student_name'],
                    date_of_birth=datetime.date(int(row['date_of_birth'].split('-')[0]),
                                                int(row['date_of_birth'].split('-')[1]),
                                                int(row['date_of_birth'].split('-')[2])),
                    citizen_id=row['cmnd'],
                    current_japanese_level=row['current_japanese_level'],
                    address=row['address'],
                    input_by=input_by,
                    modified_by=input_by))
    Student.objects.bulk_create(bulk)


def employer_entry(data, input_by):
    data = {'employer_name': data.get('employer_name'),
            'country': data.get('country'),
            'address': data.get('address')}
    data = pandas.DataFrame(data)
    bulk = []
    for index, row in data.iterrows():
        bulk.append(
            Employer(employer_name=row['employer_name'],
                     country=row['country'],
                     address=row['address'],
                     input_by=input_by,
                     modified_by=input_by))
    Employer.objects.bulk_create(bulk)
