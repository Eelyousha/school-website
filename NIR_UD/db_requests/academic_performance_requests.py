from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from ..models import *


def is_valid(data):
    result = []
    print(data.POST)
    request_date = data.POST.get('date')
    result.append(request_date)
    request_presence = data.POST.get('radio')
    result.append(request_presence)
    request_mark = data.POST.get('mark')
    if request_mark.isdigit() and 1 < int(request_mark) < 6:
        result.append(request_mark)
    else:
        return []

    request_student = data.POST.get('student')
    request_class = data.POST.get('class')
    request_subject = data.POST.get('subject')

    if Students.objects.filter(name=request_student).exists():
        student_name = Students.objects.get(name=request_student)
        student_name_id = student_name.id
        result.append(student_name_id)
    else:
        return []

    class_class_id = ''
    if Classes.objects.filter(class_id=request_class).exists():
        class_name = Classes.objects.get(class_id=request_class)
        class_class_id = class_name.id
        result.append(class_class_id)
    else:
        return []

    subject_name_id = ''
    if AcademicSubjects.objects.filter(name=request_subject).exists():
        subject_name = AcademicSubjects.objects.get(name=request_subject)
        subject_name_id = subject_name.id
        result.append(subject_name_id)
    else:
        return []

    return result


@csrf_exempt
def add_record(request):
    error = False
    data = is_valid(request)
    print(data)
    if not data:
        error = True
        print(error)
        return error
    elif data:
        record = AcademicPerformance.objects.create(is_appeared=data[1] == 'true',
                                                lesson_date=data[0],
                                                student_mark=data[2],
                                                student_id_id=data[3],
                                                class_id_id=data[4],
                                                subject_id_id=data[5])
        record.save()
        return error


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
    request_presence = request.POST.get('is_appeared_'+member_id)
    print(request_presence)
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
    error = False
    if operation == "out":
        view_table(request, member_id)
    elif operation == "delete":
        delete_record(request, member_id)
    elif operation == "change":
        change_record(request, member_id)
    elif operation == "add":
        error = add_record(request)
    return redirect('invalid_fill_ap', error)
