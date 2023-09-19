from django import forms


class OurForm(forms.Form):
    name = forms.CharField(label='Ваше имя')
    num = forms.IntegerField(label='Номер', required=False, max_value=100, initial=12,
                             help_text='напишите, сколько вам лет', disabled=True)


class AnimalForm(forms.Form):
    name = forms.CharField(label="Имя животного")
    breed = forms.CharField(label="Порода животного")
    age = forms.IntegerField(label="Возраст животного", max_value=30)
    color = forms.CharField(label="Цвет животного")
    food = forms.CharField(label="Любимая еда")
    photo = forms.ImageField(label = 'Фото питомца')


class Form3(forms.Form):
    k1 = forms.DecimalField(label='десятичные числа', decimal_places=2)
    k2 = forms.EmailField(label='email')
    k3 = forms.BooleanField(label='поставьте галочку', required=False)
    k4 = forms.NullBooleanField(label='вы человек')
    k5 = forms.URLField(label='адрес в инете', help_text='http://www.el.ru')
    k6 = forms.GenericIPAddressField(label='ip')
    k7 = forms.FilePathField(label='выберите файл', path='C:\\Users\\nimba\\Desktop', allow_folders=True,
                             match='.*\.txt')
    k8 = forms.ImageField(label='картинка')
    k9 = forms.FileField(label='файл')
    vibor = ((2, 'en'), (1, 'ru'), (3, 'fr'))
    k10 = forms.TypedChoiceField(choices=vibor)


class UploadForma(forms.Form):
    name = forms.CharField()
    img = forms.ImageField()
