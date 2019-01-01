from django.contrib import admin

from .models import *


@admin.register(ClassInfo)
class ClassInfoAdmin(admin.ModelAdmin):
    fields = ('class_name', 'from_date', 'to_date', 'level', 'teacher',)
    list_display = ('class_name', 'from_date', 'to_date', 'level', 'teacher',)

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user
        if not obj.input_by_id:
            obj.input_by = request.user
        obj.save()


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    fields = ('employer_name', 'address', 'country',)
    list_display = ('employer_name', 'address', 'country',)

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user
        if not obj.input_by_id:
            obj.input_by = request.user
        obj.save()



@admin.register(Jobs)
class JobAdmin(admin.ModelAdmin):
    fields = ('employer', 'job_title', 'job_description', 'required_degree', 'japanese_level', 'other_requirements',)
    list_display = ('employer', 'job_title', 'job_description', 'required_degree', 'japanese_level', 'other_requirements',)

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user
        if not obj.input_by_id:
            obj.input_by = request.user
        obj.save()


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    fields = ('teacher_name', 'address', 'citizen_id', 'date_of_birth', 'nationality',)
    list_display = ('teacher_name', 'address', 'citizen_id', 'date_of_birth', 'nationality',)

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user
        if not obj.input_by_id:
            obj.input_by = request.user
        obj.save()


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ('student_name', 'address', 'citizen_id', 'date_of_birth', 'current_japanese_level',)
    list_display = ('student_name', 'address', 'citizen_id', 'date_of_birth', 'current_japanese_level',)

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user
        if not obj.input_by_id:
            obj.input_by = request.user
        obj.save()


@admin.register(StudentDegree)
class StudentDegreeAdmin(admin.ModelAdmin):
    fields = ('student', 'degree_name', 'given_by', 'field_of_study',)
    list_display = ('student', 'degree_name', 'given_by', 'field_of_study',)

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user
        if not obj.input_by_id:
            obj.input_by = request.user
        obj.save()


@admin.register(StudyRecord)
class StudyRecordAdmin(admin.ModelAdmin):
    fields = ('attended_class', 'teacher', 'student','teacher_comment', 'notes',)
    list_display = ('attended_class', 'teacher', 'student','teacher_comment', 'notes',)

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user
        if not obj.input_by_id:
            obj.input_by = request.user
        obj.save()


@admin.register(WorkRecord)
class WorkRecordAdmin(admin.ModelAdmin):
    fields = ('employer', 'job', 'student', 'employer_comment', 'other_notes',)
    list_display = ('employer', 'job', 'student', 'employer_comment', 'other_notes',)

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user
        if not obj.input_by_id:
            obj.input_by = request.user
        obj.save()
