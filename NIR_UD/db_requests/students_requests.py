from django.views.decorators.csrf import csrf_exempt
from ..models import Students


@csrf_exempt
def add_record(request):
    Students().objects.create(request.POST.get('student_id'),
                              request.POST.get('name'),
                              request.POST.get('class_id'),
                              request.POST.get('phone_number'),
                              request.POST.get('parent_name'),
                              request.POST.get('parent_phone_number'),
                              request.POST.get('address')).save()


@csrf_exempt
def delete_record(request):
    record = Students().objects.get(request.POST.get('student_id'),
                                    request.POST.get('name'),
                                    request.POST.get('class_id'),
                                    request.POST.get('phone_number'),
                                    request.POST.get('parent_name'),
                                    request.POST.get('parent_phone_number'),
                                    request.POST.get('address'))
    if record is not None:
        record.delete()
    # else:


@csrf_exempt
def vew_table(request):
    all_records = Students().objects.all()


@csrf_exempt
def change_record(request):
    record = Students().objects.get(request.POST.get('student_id'),
                                    request.POST.get('name'),
                                    request.POST.get('class_id'),
                                    request.POST.get('phone_number'),
                                    request.POST.get('parent_name'),
                                    request.POST.get('parent_phone_number'),
                                    request.POST.get('address'))

    record.student_id = request.POST.get('new_student_id') \
        if request.POST.get('new_student_id') is not None else record.student_id
    record.name = request.POST.get('new_name') \
        if request.POST.get('new_name') is not None else record.name
    record.class_id = request.POST.get('new_class_id') \
        if request.POST.get('new_class_id') is not None else record.class_id
    record.phone_number = request.POST.get('new_phone_number') \
        if request.POST.get('new_phone_number') is not None else record.phone_number
    record.parent_name = request.POST.get('new_parent_name') \
        if request.POST.get('new_parent_name') is not None else record.parent_name
    record.parent_phone_number = request.POST.get('new_parent_phone_number') \
        if request.POST.get('new_parent_phone_number') is not None else record.parent_phone_number
    record.address = request.POST.get('new_address') \
        if request.POST.get('new_address') is not None else record.address
    record.save()
