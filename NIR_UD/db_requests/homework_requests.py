from django.views.decorators.csrf import csrf_exempt
from ..models import HomeWork


@csrf_exempt
def add_record(request):
    HomeWork().objects.create(request.POST.get('deadline'),
                              request.POST.get('homework_text'),
                              request.POST.get('class_id'),
                              request.POST.get('subject_id')).save()


@csrf_exempt
def delete_record(request):
    record = HomeWork().objects.get(request.POST.get('deadline'),
                                    request.POST.get('homework_text'),
                                    request.POST.get('class_id'),
                                    request.POST.get('subject_id'))
    if record is not None:
        record.delete()
    # else:


@csrf_exempt
def vew_table(request):
    all_records = HomeWork().objects.all()


@csrf_exempt
def change_record(request):
    record = HomeWork().objects.get(request.POST.get('deadline'),
                                    request.POST.get('homework_text'),
                                    request.POST.get('class_id'),
                                    request.POST.get('subject_id'))

    record.deadline = request.POST.get('new_deadline') \
        if request.POST.get('new_deadline') is not None else record.deadline
    record.homework_text = request.POST.get('new_homework_text') \
        if request.POST.get('new_homework_text') is not None else record.homework_text
    record.class_id = request.POST.get('new_class_id') \
        if request.POST.get('new_class_id') is not None else record.class_id
    record.subject_id = request.POST.get('new_subject_id') \
        if request.POST.get('new_subject_id') is not None else record.subject_id

    record.save()
