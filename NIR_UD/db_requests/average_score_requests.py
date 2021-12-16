from django.views.decorators.csrf import csrf_exempt
from ..models import AverageScore


@csrf_exempt
def add_record(request):
    AverageScore().objects.create(request.POST.get('current_score'),
                                  request.POST.get('student_id'),
                                  request.POST.get('class_id'),
                                  request.POST.get('subject_id')).save()


@csrf_exempt
def delete_record(request):
    record = AverageScore().objects.get(request.POST.get('current_score'),
                                        request.POST.get('student_id'),
                                        request.POST.get('class_id'),
                                        request.POST.get('subject_id'))
    if record is not None:
        record.delete()
    # else:


@csrf_exempt
def vew_table(request):
    all_records = AverageScore().objects.all()


@csrf_exempt
def change_record(request):
    record = AverageScore().objects.get(request.POST.get('current_score'),
                                        request.POST.get('student_id'),
                                        request.POST.get('class_id'),
                                        request.POST.get('subject_id'))

    record.current_score = request.POST.get('new_current_score') \
        if request.POST.get('new_current_score') is not None else record.lesson_date
    record.student_id = request.POST.get('new_student_id') \
        if request.POST.get('new_student_id') is not None else record.student_id
    record.class_id = request.POST.get('new_class_id') \
        if request.POST.get('new_class_id') is not None else record.class_id
    record.subject_id = request.POST.get('new_subject_id') \
        if request.POST.get('new_subject_id') is not None else record.subject_id

    record.save()
