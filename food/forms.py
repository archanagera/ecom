from django import forms
from .models import Item
class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
    n1=forms.IntegerField(label="num1",required=False)
    n2=forms.IntegerField(label="num2")

class ItemForm(forms.Form):
    name=forms.CharField(label="Item name")
    desc=forms.CharField(label="Item Description")
    price=forms.IntegerField(label="Item Price")
    image=forms.CharField(label="Item Image")

class ItemFormModel(forms.ModelForm):
    class Meta:
        model=Item
        fields=['item_name','item_price','item_desc','item_image']