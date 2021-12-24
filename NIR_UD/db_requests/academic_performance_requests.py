from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from ..models import *


@csrf_exempt
def add_record(request):
    return AcademicPerformance().objects.create(request.POST.get('lesson_date'),
                                                request.POST.get('is_appeared'),
                                                request.POST.get('student_mark'),
                                                request.POST.get('student_id'),
                                                request.POST.get('class_id'),
                                                request.POST.get('subject_id')).save()


@csrf_exempt
def edit_member(request, member_id):
    member = AcademicPerformance.objects.get(member_id)
    form = AcademicPerformance(request.POST or None, instance=member)

    if request.method == 'POST':
        form.save()
        # do something else, like redirect to a different view

    return form


@csrf_exempt
def delete_record(request, member_id):
    record = AcademicPerformance.objects.get(id=member_id)
    if record is not None:
        record.delete()

    return record


@csrf_exempt
def view_table(request):
    all_records = AcademicPerformance().objects.all()

    return all_records


@csrf_exempt
def change_record(request, member_id):
    record = AcademicPerformance.objects.get(id=member_id)

    request_date = request.POST.get('date')
    request_presence = request.POST.get('is_appeared')
    request_mark = request.POST.get('mark')
    request_student = request.POST.get('student')
    request_class = request.POST.get('class')
    request_subject = request.POST.get('subject')

    print(request.POST)
    print(type(record.class_id_id))
    print(record.class_id_id)
    print(Students.objects.filter(name=request_student))

    record.lesson_date = request_date

    if request_presence == "true":
        record.is_appeared = True
    elif request_presence == "false":
        record.is_appeared = False

    record.student_mark = int(request_mark) if request_mark.isdigit() and 1 < int(request_mark) < 6 else record.student_mark

    if Students.objects.filter(name=request_student).exists():
        student_name = Students.objects.get(name=request_student)
        student_name_id = student_name.id
        record.student_id_id = student_name_id

    if Classes.objects.filter(class_id=request_class).exists():
        class_name = Classes.objects.get(class_id=request_class)
        class_class_id = class_name.id
        record.class_id_id = class_class_id

    if AcademicSubjects.objects.filter(name=request_subject).exists():
        subject_name = AcademicSubjects.objects.get(name=request_subject)
        subject_name_id = subject_name.id
        record.subject_id_id = subject_name_id

    record.save()

    # return record
    redirect('academic_performance')


@csrf_exempt
def all_shit(request, operation, member_id):
    print(request)
    if operation == "out":
        view_table(request, member_id)
    elif operation == "delete":
        delete_record(request, member_id)
    elif operation == "change":
        change_record(request, member_id)

    return redirect('academic_performance')
