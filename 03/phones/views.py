from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_option = request.GET.get('sort')
    # Используем словарь для упрощения логики выбора сортировки, так же легче будет добавить новую сортировку
    sort_dict = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price',
    }
    # Получаем ключ сортировки, если такой есть, или None, если его нет
    sort_key = sort_dict.get(sort_option, None)
    phones = Phone.objects.all().order_by(sort_key) if sort_key else Phone.objects.all()
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    # Добавляем обработку исключения 404, если продукт не найден
    phone = get_object_or_404(Phone, slug=slug)
    context = {
        'phone': phone
    }
    return render(request, template, context)