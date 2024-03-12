from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


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
