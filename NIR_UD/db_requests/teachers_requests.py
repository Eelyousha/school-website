from django.views.decorators.csrf import csrf_exempt
from ..models import Teachers


@csrf_exempt
def add_record(request):
    Teachers().objects.create(request.POST.get('teacher_id'),
                              request.POST.get('name'),
                              request.POST.get('qualification'),
                              request.POST.get('phone_number'),
                              request.POST.get('study_load')).save()


@csrf_exempt
def delete_record(request):
    record = Teachers().objects.get(request.POST.get('teacher_id'),
                              request.POST.get('name'),
                              request.POST.get('qualification'),
                              request.POST.get('phone_number'),
                              request.POST.get('study_load'))
    if record is not None:
        record.delete()
    # else:


@csrf_exempt
def vew_table(request):
    all_records = Teachers().objects.all()


@csrf_exempt
def change_record(request):
    record = Teachers().objects.get(request.POST.get('teacher_id'),
                              request.POST.get('name'),
                              request.POST.get('qualification'),
                              request.POST.get('phone_number'),
                              request.POST.get('study_load'))

    record.teacher_id = request.POST.get('new_teacher_id') \
        if request.POST.get('new_teacher_id') is not None else record.teacher_id
    record.name = request.POST.get('new_name') \
        if request.POST.get('new_name') is not None else record.name
    record.qualification = request.POST.get('new_qualification') \
        if request.POST.get('new_qualification') is not None else record.qualification
    record.phone_number = request.POST.get('new_phone_number') \
        if request.POST.get('new_phone_number') is not None else record.phone_number
    record.study_load = request.POST.get('new_study_load') \
        if request.POST.get('new_study_load') is not None else record.study_load
    record.save()
