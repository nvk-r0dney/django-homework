# Домашнее задание по теме "02. Обработка запросов и шаблоны"

## Выполнил Шаповалов Кирилл, студент группы DJ-90

В `app - calculator` написал следующую view-функцию:

```py
def recipe_view(requests, get_recipe):
    template_name = "calculator/index.html"
    servings = int(requests.GET.get('servings', 1))
    dishes = {}
    for dish, ingridient in DATA.items():
        if get_recipe == dish:
            for ing, count in ingridient.items():
                dishes[ing] = count * servings

    context = {
        'recipe': dishes
    }
    return render(requests, template_name, context)
```

В `urls.py` проекта зарегистрировал view-функцию:

```py
from django.contrib import admin
from django.urls import path

from calculator.views import recipe_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("<get_recipe>/", recipe_view, name='recipe')
]
```

Запустил сервер. Проверяю в браузере.

**Получаю ингридиенты омлета на 1 порцию**

<img src="./img/01-get-recipe.png" width="750px" height="auto" />

**Получаю ингридиенты омлета на 3 порции**

<img src="./img/01-get-recipe-with-servings.png" width="750px" height="auto" />

Для дополнительной проверки получу еще один рецепт.

**1 порция**

<img src="./img/02-get-another-recipe.png" width="750px" height="auto" />

**5 порций**

<img src="./img/02-get-another-recipe-with-servings.png" width="750px" height="auto" />

Все корректно работает, задание выполнено.