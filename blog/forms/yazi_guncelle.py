from django import forms
from blog.models import YazilarModel

class YaziGuncelleModelForm(forms.ModelForm):
    class Meta:
        model = YazilarModel
        exclude = ('yazar', 'slug') #çok değişken olduğu için harici anlamındaki exclude kullandık.