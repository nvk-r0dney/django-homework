# Домашнее задание по теме "04. Работа с ORM, часть 2"

## Выполнил Шаповалов Кирилл, студент группы DJ-90

<br />

Задание 1. Миграции
-------------------

Для начала, дописал view-функцию, загрузил данные из json-файла и проверил как будет работать приложение без внесенных по заданию изменений.

```py
from django.shortcuts import render
from django.views.generic import ListView

from .models import Student, Teacher


def students_list(request):
    template = "school/students_list.html"
    student = Student.objects.all().prefetch_related('teacher')
    context = {
        "object_list": student
    }
    ordering = "group"
    return render(request, template, context)
```

По сути, сразу же выполнил требование дополнительного задания - применил конструкцию `prefetch_related`, позволяющую оптимизировать запросы к БД.

Подготовил и выполнил миграции, заодно сразу же создал суперпользователя для админки.

<img src="./img/00-scholl-migrate-and-superuser.png" width="750px" height="auto" />

Загрузил данные из json.

<img src="./img/00-school-loaddata.png" width="750px" height="auto" />

Запустил сервер командой `python panage.py runserver` и проверил, что все работает

<img src="./img/00-school-list-students.png" width="750px" height="auto" />

Зайдя в админку, можно убедиться, что сейчас работает связь один-к-одному - то есть для одного ученика можно выбрать только одного преподавателя.

<img src="./img/00-one-to-one.png" width="750px" height="auto" />

Множественного выбора нет. Нужно это изменить.

Доработал модель `Student` - вместо закомментированной строки добавил новую с типом ManyToManyField

```py
class Student(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
#    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    teachers = models.ManyToManyField(Teacher, related_name='students')
    group = models.CharField(max_length=10, verbose_name='Класс')

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return self.name
```

Снова создал и применил миграции, так как любые изменения моделей требуют создания и применения миграций.

<img src="./img/00-new-migration.png" width="750px" height="auto" />

Изменил html-шаблон под новые условия - добавил вывод циклом списка учителей

```html
<div class="row">
  <ul>
  {% for student in object_list %}
    <li>{{ student.name }} {{ student.group }}
      <p>{% for teacher in student.teachers.all %} 
      Преподаватель: {{ teacher.name }} {{ teacher.subject }}<br>
      {% endfor %}</p>
    </li>
  {% endfor %}
  </ul>
</div>
```

Теперь можно снова запустить сервер и проверить работу приложения.

Сразу же перейду в админку и выберу разных учителей для разных студентов.

<img src="./img/00-many-teachers.png" width="750px" height="auto" />

Так же сделаю и для другого ученика. Теперь нужно сохранить изменения и проверить вывод на странице.

<img src="./img/00-many-to-many-works.png" width="750px" height="auto" />

**Все работает корректно, первое задание выполнено.**

<br>

Задание 2. Связь "Многие-ко-многим"
-----------------------------------

