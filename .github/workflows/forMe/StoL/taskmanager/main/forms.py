from .models import list_of_executed
from django.forms import ModelForm, TextInput, Textarea

class ListForm(ModelForm):
    class Meta:
        model = list_of_executed
        fields = ['title','Name_from_list']
        widgets = {
            "title": TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Введите имя"
        }),
            'Name_from_list': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Где его найти?"

            })
        }
