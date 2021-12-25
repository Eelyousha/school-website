from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django import template
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from .models import Classes, AcademicPerformance
import datetime
from django.db.models import Q


@csrf_exempt
def index(request):
    return render(request, 'NIR_UD/index.html')


@csrf_exempt
def about(request):
    return render(request, 'NIR_UD/about.html')


@csrf_exempt
def analytic(request):
    return render(request, 'NIR_UD/Analytic.html')


@csrf_exempt
def academic_performance(request, error=False):
    marks = AcademicPerformance.objects.all()

    if (request.user.groups.filter(name=teachers_group)):
        access = True
    else:
        access = False

    print(access)

    return render(request, 'NIR_UD/AcademicPerfomance.html', {'marks': marks, 'error': error, 'access': access})


# def classestest(request):
#     classes = Classes.objects.all()
#     return render(request, 'NIR_UD/AcademicPerfomance.html', {'classes': classes})


@csrf_exempt
def academic_subjects(request):
    return render(request, 'NIR_UD/AcademicSubjects.html')


@csrf_exempt
def average_score(request):
    return render(request, 'NIR_UD/AverageScore.html')


@csrf_exempt
def classes(request):
    return render(request, 'NIR_UD/Classes.html')


@csrf_exempt
def lecture_halls(request):
    return render(request, 'NIR_UD/LectureHalls.html')


@csrf_exempt
def teachers(request):
    return render(request, 'NIR_UD/Teachers.html')


@csrf_exempt
def timetable(request):
    return render(request, 'NIR_UD/Timetable.html')


@csrf_exempt
def homework(request):
    return render(request, 'NIR_UD/Homework.html')


@csrf_exempt
def students(request):
    return render(request, 'NIR_UD/Students.html')


@csrf_exempt
def auth(request):
    c = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if user.groups.filter(name=students_group):
            return render(request, 'NIR_UD/students_tables.html', c)
        elif user.groups.filter(name=teachers_group):
            return render(request, 'NIR_UD/teacher_tables.html', c)
        else:
            return render(request, 'NIR_UD/admin_tables.html', c)
        # Redirect to a success page.
    else:
        return HttpResponseRedirect('404')


def back(request):
    if request.user.groups.filter(name=students_group):
        return render(request, 'NIR_UD/students_tables.html')
    elif request.user.groups.filter(name=teachers_group):
        return render(request, 'NIR_UD/teacher_tables.html')
    else:
        return render(request, 'NIR_UD/admin_tables.html')


class AcademicPerfomance_SearchResultsView(ListView):
    template_name = 'NIR_UD/search_results_acper.html'
    model = AcademicPerformance

    def get_queryset(self):  # новый
        from pprint import pprint
        print(self.request.GET)
        query = self.request.GET.get('q')
        if query.isdigit():
            object_list = AcademicPerformance.objects.filter(
                Q(student_mark=int(query))
            )
        else:
            object_list = AcademicPerformance.objects.filter(
                Q(lesson_date__icontains=query) | Q(student_id__name__icontains=query) | Q(class_id__class_id__icontains=query) | Q(subject_id__name__startswith=query)
            )

        return object_list


# Права доступа к таблице средних баллов
view_as_permission = Permission.objects.get(codename='view_averagescore')

# Права доступа к таблице академической успеваемости
view_ap_permission = Permission.objects.get(codename='view_academicperformance')
add_ap_permission = Permission.objects.get(codename='add_academicperformance')
delete_ap_permission = Permission.objects.get(codename='delete_academicperformance')
change_ap_permission = Permission.objects.get(codename='change_academicperformance')

# Права доступа к расписанию уроков
view_t_permission = Permission.objects.get(codename='view_timetable')

# Права доступа к таблице домашних заданий
view_hw_permission = Permission.objects.get(codename='view_homework')
add_hw_permission = Permission.objects.get(codename='add_homework')
delete_hw_permission = Permission.objects.get(codename='delete_homework')
change_hw_permission = Permission.objects.get(codename='change_homework')

# Права доступа к таблице студентов
view_st_permission = Permission.objects.get(codename='view_students')
change_st_permission = Permission.objects.get(codename='change_students')

# Права доступа к таблице классов
view_cl_permission = Permission.objects.get(codename='view_classes')

# Права доступа к таблице учебных предметов
view_acsub_permission = Permission.objects.get(codename='view_academicsubjects')

# Права доступа ученика
students_group, _ = Group.objects.get_or_create(name='Students')
students_group.permissions.add(view_as_permission, view_ap_permission, view_t_permission,
                               view_hw_permission)

# Права доступа учителя
teachers_group, _ = Group.objects.get_or_create(name='Teachers')
teachers_group.permissions.add(add_ap_permission, view_ap_permission, delete_ap_permission,
                               change_ap_permission)
teachers_group.permissions.add(add_hw_permission, view_hw_permission, delete_hw_permission,
                               change_hw_permission)
teachers_group.permissions.add(view_acsub_permission, view_cl_permission, view_st_permission, change_st_permission,
                               view_t_permission, view_as_permission)

# Создание пользователя группы "ученики"
# student_1 = User.objects.create_user('iov14032008', '12345678')
# students_group.user_set.add(student_1)

# Создание пользователя группы "учителя"
# teacher_1 = User.objects.create_user('isv05071964', '12345678')
# teachers_group.user_set.add(teacher_1)
