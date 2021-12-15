from django.db import models

TEACHER_ID_LEN = 11
TEACHER_NAME_LEN = 100
TEACHER_QUALIFICATION_LEN = 20
PHONE_NUMBER_LEN = 10

LECTURE_HALL_ID_LEN = 10
LECTURE_HALL_NAME_LEN = 45
LECTURE_HALL_DOTW = 12
LESSON_AMOUNT_LEN = 2

CLASS_ID_LEN = 3
CLASS_NUMBER_OF_STUDENTS_LEN = 2
SUBJECT_NAME_LEN = 30
CLASSES_TP_LEN = 40

STUDENT_NAME_LEN = 100
STUDENT_ID_LEN = 11
STUDENT_PRENT_NAME_LEN = 100

AVERAGE_SCORE_LEN = 3

MARK_LEN = 1

TIMETABLE_DAY_OF_WEEK_LEN = 20


# 1 Таблица учителей
class Teachers(models.Model):
    teacher_id = models.CharField(max_length=TEACHER_ID_LEN)  # ФИО + год рождения
    name = models.CharField(max_length=TEACHER_NAME_LEN)  # ФИО
    phone_number = models.DecimalField(max_digits=PHONE_NUMBER_LEN, decimal_places=PHONE_NUMBER_LEN)  # Номер телефона
    qualification = models.CharField(
        max_length=TEACHER_QUALIFICATION_LEN)  # Квалификационная категория (высшая, первая, вторая)
    study_load = models.IntegerField()  # Учебная нагрузка (в часах)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Таблица учителей'


# 2 Таблица занятости аудиторий
class LectureHalls(models.Model):
    lecture_hall_id = models.CharField(
        max_length=LECTURE_HALL_ID_LEN)  # Название кабинета (строка, тк может быть 123абв)
    name = models.CharField(
        max_length=LECTURE_HALL_NAME_LEN)  # Название проводимого предмета (аля "английский" или "спортзал"
    lesson_index_number = models.DecimalField(max_digits=LESSON_AMOUNT_LEN,
                                              decimal_places=LESSON_AMOUNT_LEN)  # Порядковый номер проводимого урока
    day_of_the_week = models.CharField(max_length=LECTURE_HALL_DOTW)
    is_busy = models.BooleanField()  # Занят ли кабинет в данный день и данный урок

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Занятость аудитории'
        verbose_name_plural = 'Таблица занятости аудиторий'


# 3 Таблица учебных предметов
class AcademicSubjects(models.Model):
    subject_id = models.IntegerField()  # ID учебного предмета
    name = models.CharField(max_length=SUBJECT_NAME_LEN)  # Название предмета
    about_subject = models.TextField()  # Описание предмета

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Учебный предмет'
        verbose_name_plural = 'Таблица учебных предметов'


# 4 Таблица классов
class Classes(models.Model):
    class_id = models.CharField(max_length=CLASS_ID_LEN)  # ID класса (№ класса + буква)
    teacher_id = models.ForeignKey(Teachers, on_delete=models.CASCADE)  # ID классного руководителя
    number_of_students = models.IntegerField()  # Количество учеников
    training_profile = models.CharField(max_length=CLASSES_TP_LEN)  # Профиль обучения

    def __str__(self):
        return self.class_id

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Таблица классов'


# 5 Таблица учеников
class Students(models.Model):
    student_id = models.CharField(max_length=STUDENT_ID_LEN)  # ID ученика (инициалы + дата рождения)
    name = models.CharField(max_length=STUDENT_NAME_LEN)  # Имя ученика
    class_id = models.ForeignKey(Classes,
                                 on_delete=models.CASCADE)  # ID класса, который связан первичным ключом с таблицей классов. При удалении корневого объекта (класса) данный экземпляр обнулится.
    phone_number = models.DecimalField(max_digits=PHONE_NUMBER_LEN,
                                       decimal_places=PHONE_NUMBER_LEN)  # Телефонный номер ученика
    parent_name = models.CharField(max_length=STUDENT_PRENT_NAME_LEN)  # Имя родителей
    parent_phone_number = models.DecimalField(max_digits=PHONE_NUMBER_LEN,
                                              decimal_places=PHONE_NUMBER_LEN)  # Телефонный номер родителей
    address = models.TextField()  # Адрес проживания

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Таблица учеников'


# 6 Таблица средних баллов
class AverageScore(models.Model):
    student_id = models.ForeignKey(Students,
                                   on_delete=models.CASCADE)  # ID ученика, который связан первичным ключом с таблицей учеников. При удалении корневого объекта удалится и данный экземпляр.
    subject_id = models.ForeignKey(AcademicSubjects,
                                   on_delete=models.CASCADE)  # ID учебного предмета, который связан первичным ключом с таблицей учебных предметов. При удалении корневого объекта (предмета) удалится и данный экземпляр (запись о среднем балле).
    class_id = models.ForeignKey(Classes,
                                 on_delete=models.CASCADE)  # ID класса, который связан первичным ключом с таблицей классов. При удалении корневого объекта (класса) данный экземпляр обнулится.
    current_score = models.FloatField(
        max_length=AVERAGE_SCORE_LEN)  # Текущий средний балл, вычисляемый на основе таблицы успеваемости

    def __str__(self):
        return self.current_score

    class Meta:
        verbose_name = 'Средний балл'
        verbose_name_plural = 'Таблица средних баллов'


# 7 Таблица успеваемости
class AcademicPerformance(models.Model):
    lesson_date = models.DateField()  # Дата урока (в формате SQLite)
    is_appeared = models.BooleanField()  # Индикатор присутствия на уроке (есть/нет)
    student_mark = models.DecimalField(max_digits=MARK_LEN, decimal_places=MARK_LEN)  # Оценка за урок (2-5)
    student_id = models.ForeignKey(Students,
                                   on_delete=models.CASCADE)  # ID студента, который связан первичным ключом с таблицей учеников. При удалении корневого объекта удалится и данный экземпляр.
    class_id = models.ForeignKey(Classes,
                                 on_delete=models.CASCADE)  # ID класса, который связан первичным ключом с таблицей классов. При удалении корневого объекта (класса) данный экземпляр обнулится.
    subject_id = models.ForeignKey(AcademicSubjects,
                                   on_delete=models.CASCADE)  # ID предмета (целочисленное поле), связан первичным ключом с таблицей редметов. При удалении удалится и данный экземпляр.

    def __str__(self):
        return self.student_mark

    class Meta:
        verbose_name = 'Оценка за урок'
        verbose_name_plural = 'Таблица успеваемости'


# 8 Расписание уроков
class Timetable(models.Model):
    day_of_week = models.CharField(max_length=TIMETABLE_DAY_OF_WEEK_LEN)  # День недели
    lesson_number = models.IntegerField()  # Номер урока
    class_id = models.ForeignKey(Classes,
                                 on_delete=models.CASCADE)  # ID класса, который связан первичным ключом с таблицей классов. При удалении корневого объекта (класса) данный экземпляр обнулится.
    subject_id = models.ForeignKey(AcademicSubjects,
                                   on_delete=models.CASCADE)  # ID предмета (целочисленное поле), связан первичным ключом с таблицей предметов. При удалении удалится и данный экземпляр.
    lecture_hall_id = models.ForeignKey(LectureHalls,
                                        on_delete=models.CASCADE)  # ID аудитории (массив char), связан первичным ключом с таблицей занятости аудиторий. При удалении данный экземпляр обнулится.

    def __str__(self):
        return self.lesson_number

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Расписание уроков'


# 9 Домашние задания
class HomeWork(models.Model):
    deadline = models.DateField()  # Дата сдачи домашнего задания
    subject_id = models.ForeignKey(AcademicSubjects,
                                   on_delete=models.CASCADE)  # ID учебного предмета, который связан первичным ключом с таблицей учебных предметов. При удалении корневого объекта (предмета) удалится и данный экземпляр (запись о среднем балле).
    homework_text = models.TextField()  # Текст домашнего задания для ученика.
    class_id = models.ForeignKey(Classes,
                                 on_delete=models.CASCADE)  # ID класса, который связан первичным ключом с таблицей классов. При удалении корневого объекта (класса) данный экземпляр обнулится.

    def __str__(self):
        return self.class_id

    class Meta:
        verbose_name = 'Домашнее задание'
        verbose_name_plural = 'Таблица домашних заданий'
