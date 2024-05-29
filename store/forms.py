from django import forms
from .models import Product, Promotion

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category']

class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['discount', 'start_date', 'end_date']