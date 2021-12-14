from django.contrib import admin
from .models import Teachers, LectureHalls, AcademicSubjects, \
    Classes, AcademicPerformance, Students, AverageScore, \
    Timetable, HomeWork

admin.site.register(Teachers)
admin.site.register(LectureHalls)
admin.site.register(AcademicSubjects)
admin.site.register(Classes)
admin.site.register(AcademicPerformance)
admin.site.register(Students)
admin.site.register(AverageScore)
admin.site.register(Timetable)
admin.site.register(HomeWork)
