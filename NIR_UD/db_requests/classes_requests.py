from django.views.decorators.csrf import csrf_exempt
from ..models import Classes


@csrf_exempt
def add_record(request):
    Classes().objects.create(request.POST.get('training_profile'),
                             request.POST.get('teacher_id'),
                             request.POST.get('number_of_students'),
                             request.POST.get('class_id')).save()


@csrf_exempt
def delete_record(request):
    record = Classes().objects.get(request.POST.get('training_profile'),
                                   request.POST.get('teacher_id'),
                                   request.POST.get('number_of_students'),
                                   request.POST.get('class_id'))
    if record is not None:
        record.delete()
    # else:


@csrf_exempt
def vew_table(request):
    all_records = Classes().objects.all()


@csrf_exempt
def change_record(request):
    record = Classes().objects.get(request.POST.get('training_profile'),
                                   request.POST.get('teacher_id'),
                                   request.POST.get('number_of_students'),
                                   request.POST.get('class_id'))

    record.training_profile = request.POST.get('new_training_profile') \
        if request.POST.get('new_training_profile') is not None else record.lesson_date
    record.teacher_id = request.POST.get('new_teacher_id') \
        if request.POST.get('new_teacher_id') is not None else record.is_appeared
    record.number_of_students = request.POST.get('new_number_of_students') \
        if request.POST.get('new_number_of_students') is not None else record.student_mark
    record.class_id = request.POST.get('new_class_id') \
        if request.POST.get('new_class_id') is not None else record.class_id

    record.save()
