from django.urls import path, include, re_path
from . import views
from .db_requests.academic_performance_requests import all_shit
from .views import AcademicPerfomance_SearchResultsView

urlpatterns = [
    path('about', views.about),
    path('', views.index),
    re_path('^NIR_UD/$', views.auth, name='namespace'),
    re_path('all_tables', views.back, name='back'),
    re_path('Analytic.html', views.analytic, name='analytics'),
    path('academicperfomance', views.academic_performance, name='academic_performance'),
    re_path('AcademicSubjects.html', views.academic_subjects),
    re_path('AverageScore.html', views.average_score),
    re_path('Classes.html', views.classes),
    re_path('LectureHalls.html', views.lecture_halls),
    re_path('Teachers.html', views.teachers),
    re_path('Timetable.html', views.timetable),
    re_path('Homework.html', views.homework),
    re_path('Students.html', views.students),
    path('ap/<operation>/<member_id>', all_shit, name="ap"),
    path('search/', AcademicPerfomance_SearchResultsView.as_view(), name='search_results'),
]

