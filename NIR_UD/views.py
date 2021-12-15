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


def index(request):
    return render(request, 'NIR_UD/index.html')


def about(request):
    return render(request, 'NIR_UD/about.html')


@csrf_exempt
def admin(request):
    return render(request, 'NIR_UD/admin_tables.html')


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
