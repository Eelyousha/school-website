from django.views.decorators.csrf import csrf_exempt
from ..models import Timetable


@csrf_exempt
def add_record(request):
    Timetable().objects.create(request.POST.get('day_of_week'),
                               request.POST.get('lesson_number'),
                               request.POST.get('class_id'),
                               request.POST.get('subject_id'),
                               request.POST.get('lecture_hall_id')).save()


@csrf_exempt
def delete_record(request):
    record = Timetable().objects.get(request.POST.get('day_of_week'),
                                     request.POST.get('lesson_number'),
                                     request.POST.get('class_id'),
                                     request.POST.get('subject_id'),
                                     request.POST.get('lecture_hall_id'))
    if record is not None:
        record.delete()
    # else:


@csrf_exempt
def vew_table(request):
    all_records = Timetable().objects.all()


@csrf_exempt
def change_record(request):
    record = Timetable().objects.get(request.POST.get('day_of_week'),
                                     request.POST.get('lesson_number'),
                                     request.POST.get('class_id'),
                                     request.POST.get('subject_id'),
                                     request.POST.get('lecture_hall_id'))

    record.day_of_week = request.POST.get('new_day_of_week') \
        if request.POST.get('new_day_of_week') is not None else record.day_of_week
    record.lesson_number = request.POST.get('new_lesson_number') \
        if request.POST.get('new_lesson_number') is not None else record.lesson_number
    record.class_id = request.POST.get('new_class_id') \
        if request.POST.get('new_class_id') is not None else record.class_id
    record.subject_id = request.POST.get('new_subject_id') \
        if request.POST.get('new_subject_id') is not None else record.subject_id
    record.lecture_hall_id = request.POST.get('new_lecture_hall_id') \
        if request.POST.get('new_lecture_hall_id') is not None else record.lecture_hall_id
    record.save()
