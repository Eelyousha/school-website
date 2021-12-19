from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from ..models import AcademicPerformance


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
    record = AcademicPerformance().objects.get(member_id)

    record.lesson_date = request.POST.get('new_lesson_date') \
        if request.POST.get('new_lesson_date') is not None else record.lesson_date
    record.is_appeared = request.POST.get('new_is_appeared') \
        if request.POST.get('new_is_appeared') is not None else record.is_appeared
    record.student_mark = request.POST.get('new_student_mark') \
        if request.POST.get('new_student_mark') is not None else record.student_mark
    record.student_id = request.POST.get('new_student_id') \
        if request.POST.get('new_student_id') is not None else record.student_id
    record.class_id = request.POST.get('new_class_id') \
        if request.POST.get('new_class_id') is not None else record.class_id
    record.subject_id = request.POST.get('new_subject_id') \
        if request.POST.get('new_subject_id') is not None else record.subject_id

    record.save()

    return record


@csrf_exempt
def all_shit(request, operation, member_id):
    print(request.GET)
    if request.method == "GET":
        if operation == "out":
            view_table(request, member_id)
        elif operation == "delete":
            delete_record(request, member_id)
        elif operation == "change":
            change_record(request, member_id)
    return redirect('academic_performance')
