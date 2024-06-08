from django.forms import modelformset_factory, ModelForm, Select, Textarea, TextInput, DateInput, NumberInput
from .models import Entradas

class EntradaForm(ModelForm):
    class Meta:
        model = Entradas
        fields = ['produto', 'quantidade', 'preco']
        widgets = {
            'produto': Select(attrs={'class' : 'input is-normal'}),
            'quantidade': TextInput(attrs={'class': 'input is-normal'}),
            'preco': NumberInput(attrs={'class': 'input is-normal'}),
        }