from django.forms import ModelForm
from .models import Item

class DeleteForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'