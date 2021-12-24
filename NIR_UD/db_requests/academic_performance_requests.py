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
    print(type(record.class_id))
    record.lesson_date = request_date

    record.is_appeared = True

    record.student_mark = int(request_mark) if request_mark.isdigit() and 1 < int(request_mark) < 6 else record.student_mark

    record.student_id = request_student if Students.objects.filter(student_id=request_student).exists() else record.student_id

    record.class_id = request_class if Classes.objects.filter(class_id=request_class).exist() else record.class_id

    record.subject_id = request_subject if AcademicSubjects.objects.filter(subject_id=request_subject).exists() else record.subject_id

    record.save()

    return record


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
