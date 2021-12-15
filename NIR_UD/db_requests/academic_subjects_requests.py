from django.views.decorators.csrf import csrf_exempt
from ..models import AcademicSubjects


@csrf_exempt
def add_record(request):
    AcademicSubjects().objects.create(request.POST.get('name'),
                                      request.POST.get('about_subject'),
                                      request.POST.get('subject_id')).save()


@csrf_exempt
def delete_record(request):
    record = AcademicSubjects().objects.get(request.POST.get('name'),
                                            request.POST.get('about_subject'),
                                            request.POST.get('subject_id'))
    if record is not None:
        record.delete()
    # else:


@csrf_exempt
def vew_table(request):
    all_records = AcademicSubjects().objects.all()


@csrf_exempt
def change_record(request):
    record = AcademicSubjects().objects.get(request.POST.get('name'),
                                            request.POST.get('about_subject'),
                                            request.POST.get('subject_id'))

    record.name = request.POST.get('new_name') \
        if request.POST.get('new_name') is not None else record.lesson_date
    record.about_subject = request.POST.get('new_about_subject') \
        if request.POST.get('new_about_subject') is not None else record.is_appeared
    record.subject_id = request.POST.get('new_subject_id') \
        if request.POST.get('new_subject_id') is not None else record.subject_id

    record.save()
