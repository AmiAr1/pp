from django import forms


class PageForm(forms.Form):
    page = forms.CharField(
        label="Количество первых страниц ",
        max_length=20,
        widget=forms.NumberInput(
        attrs={
                "max": 20,
                "class":"form-control",
                "style":"width: 100px;" 
            }))
    
