from django.shortcuts import render
from django.http import HttpResponse


def omlet(request):
    new_data = DATA['omlet']

    data = {'omlet': new_data}
    return render(request, 'calculator/omlet.html', context=data)

def pasta(request):
    new_data = DATA['pasta']
    data = {'pasta': new_data}
    return render(request, 'calculator/pasta.html', context=data)
def buter(request):
    new_data = DATA['buter']
    data = {'buter': new_data}
    return render(request, 'calculator/buter.html', context=data)




def index(request):
    data = {'data': DATA}
    return render(request, 'calculator/index.html', context=data)

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
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
