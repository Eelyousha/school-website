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
    record = AcademicPerformance.objects.get(id=member_id)

    print(request.POST)
    record.lesson_date = request.POST.get('date') \
        if request.POST.get('date') is not {} else record.lesson_date
    record.is_appeared = request.POST.get('is_appeared') \
        if request.POST.get('is_appeared') is not {} else record.is_appeared
    record.student_mark = request.POST.get('mark') \
        if request.POST.get('mark') is not {} else record.student_mark
    record.student_id = request.POST.get('student') \
        if request.POST.get('student') is not {} else record.student_id
    record.class_id = request.POST.get('class') \
        if request.POST.get('class') is not {} else record.class_id
    record.subject_id = request.POST.get('subject') \
        if request.POST.get('subject') is not {} else record.subject_id

    record.save()

    return record


@csrf_exempt
def all_shit(request, operation, member_id):
    print('dick')
    print(request)
    if operation == "out":
        view_table(request, member_id)
    elif operation == "delete":
        delete_record(request, member_id)
    elif operation == "change":
        change_record(request, member_id)

    return redirect('academic_performance')
