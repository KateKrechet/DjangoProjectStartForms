from django.shortcuts import render

from anketa.form import OurForm
from anketa.form import AnimalForm
from anketa.form import *
from django.http import HttpResponse


# Create your views here.
def index(req):
    return render(req, 'index.html')


def forma(req, id):
    id = int(id)
    if id == 0:
        # если заполнили форму, то Спасибо; в противном случае Форма1, которую необходимо заполнить
        if req.method == 'POST':
            name = req.POST.get('name')
            num = req.POST.get('num')
            output = '''<h1>Спасибо</h1>
            <h2>Ваше имя -- {0}</h2>
            <h2>Ваше число -- {1}</h2>
            '''.format(name, num)
            return HttpResponse(output)
        else:
            anketa1 = OurForm()
            data = {'form': anketa1}
            return render(req, 'forma.html', context=data)
    if id == 1:
        if req.method == 'POST':
            name = req.POST.get('name')
            breed = req.POST.get('breed')
            age = req.POST.get('age')
            color = req.POST.get('color')
            food = req.POST.get('food')
            # загружаем изображение (3 строчки)
            img = req.FILES.get('photo').read()
            file = open('anketa/static/upload/{0}.jpg'.format(name), 'wb')
            file.write(img)
            # выводим загруженный файл (2 строчки)
            fpath = 'upload/{0}.jpg'.format(name)
            info_animal = {'k1': name, 'k2': breed, 'k3': age, 'k4': color, 'k5': food, 'k6': fpath}
            return render(req, 'final.html', context=info_animal)
        else:
            anketa1 = AnimalForm()
            data = {'form': anketa1}
            return render(req, 'forma.html', context=data)


def forma3(req):
    if req.method == 'POST':
        k1 = req.POST.get('k1')
        k2 = req.POST.get('k2')
        k4 = req.POST.get('k4')
        k7 = req.POST.get('k7')
        k10 = req.POST.get('k10')
        print(k1, k2)
        output = '''<h1>Спасибо</h1>
        <h2>первое -- {0}</h2>
        <h2>второе -- {1}</h2>
        <h2>четвертое -- {2}</h2>
        <h2>седьмое -- {3}</h2>
        <h2>язык -- {4}</h2>
        '''.format(k1, k2, k4, k7, k10)
        return HttpResponse(output)
    else:
        anketa = Form3()
        data = {'form': anketa}
        return render(req, 'forma.html', context=data)


def upload(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        # загружаем изображение (3 строчки)
        img = req.FILES.get('img').read()
        file = open('anketa/static/upload/{0}.jpg'.format(name), 'wb')
        file.write(img)
        # выводим загруженный файл (2 строчки)
        fpath = 'upload/{0}.jpg'.format(name)
        data = {'k1': name, 'k2': fpath}
        return render(req, 'end_page.html', context=data)
    else:
        anketa = UploadForma()
        data = {'form': anketa}
        return render(req, 'forma.html', context=data)
