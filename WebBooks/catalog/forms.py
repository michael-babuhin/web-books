from django import forms
from datetime import date
from .models import Book

class AuthorsForm(forms.Form):
    first_name = forms.CharField(label="Имя автора")
    second_name = forms.CharField(label="Фамилия Автора")
    date_of_birth = forms.DateField(label="Дата рождения", 
                                    initial=format(date.today()), 
                                    widget=forms.widgets.DateInput(attrs={'type': 'date'})
                                    )
    date_of_death = forms.DateField(label="Дата смерти", 
                                    initial=format(date.today()), 
                                    widget=forms.widgets.DateInput(attrs={'type': 'date'})
                                    )
    

class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'genre', 'language', 'author', 'summary', 'isbn']