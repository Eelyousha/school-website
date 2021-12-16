from django.views.decorators.csrf import csrf_exempt
from ..models import AcademicPerformance


@csrf_exempt
def add_record(request):
    AcademicPerformance().objects.create(request.POST.get('lesson_date'),
                                         request.POST.get('is_appeared'),
                                         request.POST.get('student_mark'),
                                         request.POST.get('student_id'),
                                         request.POST.get('class_id'),
                                         request.POST.get('subject_id')).save()


@csrf_exempt
def delete_record(request):
    record = AcademicPerformance().objects.get(request.POST.get('lesson_date'),
                                               request.POST.get('is_appeared'),
                                               request.POST.get('student_mark'),
                                               request.POST.get('student_id'),
                                               request.POST.get('class_id'),
                                               request.POST.get('subject_id'))
    if record is not None:
        record.delete()
    # else:


@csrf_exempt
def vew_table(request):
    all_records = AcademicPerformance().objects.all()


@csrf_exempt
def change_record(request):
    record = AcademicPerformance().objects.get(request.POST.get('lesson_date'),
                                               request.POST.get('is_appeared'),
                                               request.POST.get('student_mark'),
                                               request.POST.get('student_id'),
                                               request.POST.get('class_id'),
                                               request.POST.get('subject_id'))

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
