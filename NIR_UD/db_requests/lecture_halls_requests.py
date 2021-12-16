from django.views.decorators.csrf import csrf_exempt
from ..models import LectureHalls


@csrf_exempt
def add_record(request):
    LectureHalls().objects.create(request.POST.get('lecture_hall_id'),
                                  request.POST.get('name'),
                                  request.POST.get('lesson_index_number'),
                                  request.POST.get('day_of_the_week'),
                                  request.POST.get('is_busy')).save()


@csrf_exempt
def delete_record(request):
    record = LectureHalls().objects.get(request.POST.get('lecture_hall_id'),
                                        request.POST.get('name'),
                                        request.POST.get('lesson_index_number'),
                                        request.POST.get('day_of_the_week'),
                                        request.POST.get('is_busy'))
    if record is not None:
        record.delete()
    # else:


@csrf_exempt
def vew_table(request):
    all_records = LectureHalls().objects.all()


@csrf_exempt
def change_record(request):
    record = LectureHalls().objects.get(request.POST.get('lecture_hall_id'),
                                        request.POST.get('name'),
                                        request.POST.get('lesson_index_number'),
                                        request.POST.get('day_of_the_week'),
                                        request.POST.get('is_busy'))

    record.lecture_hall_id = request.POST.get('new_lecture_hall_id') \
        if request.POST.get('new_lecture_hall_id') is not None else record.lecture_hall_id
    record.name = request.POST.get('new_name') \
        if request.POST.get('new_name') is not None else record.name
    record.lesson_index_number = request.POST.get('new_lesson_index_number') \
        if request.POST.get('new_lesson_index_number') is not None else record.lesson_index_number
    record.day_of_the_week = request.POST.get('new_day_of_the_week') \
        if request.POST.get('new_day_of_the_week') is not None else record.day_of_the_week
    record.is_busy = request.POST.get('new_is_busy') \
        if request.POST.get('new_is_busy') is not None else record.is_busy

    record.save()
