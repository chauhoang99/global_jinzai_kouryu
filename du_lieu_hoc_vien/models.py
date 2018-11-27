from django.db import models
from django.contrib.auth.models import User


class ClassInfo(models.Model):
    class_name = models.CharField(max_length=50, null=True)
    from_date = models.DateTimeField(null=True)
    to_date = models.DateTimeField(null=True)
    level = models.CharField(max_length=20, null=True)
    input_date = models.DateTimeField(auto_now=True)
    input_by = models.ForeignKey(to=User, related_name='class_input_by', on_delete=models.CASCADE)
    modified_date = models.DateTimeField(null=True)
    modified_by = models.ForeignKey(to=User, related_name='class_modifiled_by', on_delete=models.CASCADE)


class Employer(models.Model):
    employer_name = models.CharField(max_length=100, null=True)
    address = models.TextField(null=True)
    country = models.CharField(max_length=30, null=True)
    input_date = models.DateTimeField(auto_now=True)
    input_by = models.ForeignKey(to=User, related_name='employer_input_by', on_delete=models.CASCADE)
    modified_date = models.DateTimeField(null=True)
    modified_by = models.ForeignKey(to=User, related_name='employer_modifiled_by', on_delete=models.CASCADE)


class Jobs(models.Model):
    employer = models.ForeignKey(to=Employer, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100, null=True)
    job_description = models.TextField(null=True)
    required_degree = models.CharField(max_length=50, null=True)
    japanese_level = models.CharField(max_length=20, null=True)
    other_requirements = models.TextField(null=True)
    input_date = models.DateTimeField(auto_now=True)
    input_by = models.ForeignKey(to=User, related_name='job_input_by', on_delete=models.CASCADE)
    modified_date = models.DateTimeField(null=True)
    modified_by = models.ForeignKey(to=User, related_name='job_modifiled_by', on_delete=models.CASCADE)


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100, null=True)
    address = models.TextField(null=True)
    citizen_id = models.CharField(max_length=20, null=True)
    date_of_birth = models.DateField(null=True)
    input_date = models.DateTimeField(auto_now=True)
    input_by = models.ForeignKey(to=User, related_name='teacher_input_by', on_delete=models.CASCADE)
    modified_date = models.DateTimeField(null=True)
    modified_by = models.ForeignKey(to=User, related_name='teacher_modifiled_by', on_delete=models.CASCADE)


class Student(models.Model):
    student_name = models.CharField(max_length=100, null=True)
    address = models.TextField(null=True)
    citizen_id = models.CharField(max_length=20, null=True)
    date_of_birth = models.DateField(null=True)
    current_japanese_level = models.CharField(max_length=20, null=True)
    input_date = models.DateTimeField(auto_now=True)
    input_by = models.ForeignKey(to=User, related_name='student_input_by', on_delete=models.CASCADE)
    modified_date = models.DateTimeField(null=True)
    modified_by = models.ForeignKey(to=User, related_name='student_modifiled_by', on_delete=models.CASCADE)


class StudentDegree(models.Model):
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    degree_name = models.CharField(max_length=50, null=True)
    given_by = models.CharField(max_length=50, null=True)
    field_of_study = models.CharField(max_length=100, null=True)
    input_date = models.DateTimeField(auto_now=True)
    input_by = models.ForeignKey(to=User, related_name='degree_input_by', on_delete=models.CASCADE)
    modified_date = models.DateTimeField(null=True)
    modified_by = models.ForeignKey(to=User, related_name='degree_modifiled_by', on_delete=models.CASCADE)


class StudyRecord(models.Model):
    attended_class = models.ForeignKey(to=ClassInfo, on_delete=models.CASCADE)
    teacher = models.ForeignKey(to=Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    teacher_comment = models.TextField(null=True)
    notes = models.TextField(null=True)
    input_date = models.DateTimeField(auto_now=True)
    input_by = models.ForeignKey(to=User, related_name='study_record_input_by', on_delete=models.CASCADE)
    modified_date = models.DateTimeField(null=True)
    modified_by = models.ForeignKey(to=User, related_name='study_record_modifiled_by', on_delete=models.CASCADE)


class WorkRecord(models.Model):
    employer = models.ForeignKey(to=Employer, on_delete=models.CASCADE, null=True)
    job = models.ForeignKey(to=Jobs, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE, null=True)
    employer_comment = models.TextField(null=True)
    other_notes = models.TextField(null=True)
    input_date = models.DateTimeField(auto_now=True)
    input_by = models.ForeignKey(to=User, related_name='work_record_input_by', on_delete=models.CASCADE)
    modified_date = models.DateTimeField(null=True)
    modified_by = models.ForeignKey(to=User, related_name='work_record_modifiled_by', on_delete=models.CASCADE)
