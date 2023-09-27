from django import forms 
from .models import Book , Category 


class CategoryForm (forms.ModelForm):
    class Meta: 
        model = Category 
        fields = ['name']
        widgets =     {
        'name': forms.TextInput(attrs = {'class':'form-control'}),
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('active',)
        widgets = {
            'title': forms.TextInput(attrs = {'class':'form-control'}),
            'title': forms.TextInput(attrs = {'class':'form-control'}),
            'author': forms.TextInput(attrs = {'class':'form-control'}),
            'photo_book':forms.FileInput(attrs = {'class':'form-control'}),
            'photo_author':forms.FileInput(attrs = {'class':'form-control'}),
            'price':forms.NumberInput(attrs = {'class':'form-control'}),
            'pages':forms.NumberInput(attrs = {'class':'form-control'}),
            'rental_price_day':forms.NumberInput(attrs = {'class':'form-control','id':'rental_price_day'}),
            'rental_total':forms.NumberInput(attrs = {'class':'form-control','id':'rental_total'}),
            'rental_duration':forms.NumberInput(attrs = {'class':'form-control','id':'rental_duration'}),
            'status':forms.Select(attrs = {'class':'form-control'}),
            'category':forms.Select(attrs = {'class':'form-control'}),
        }

