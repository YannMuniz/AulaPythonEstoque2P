from django.forms import ModelForm
from .models import Saida

class SaidaForm(ModelForm):
    class Meta:
        model = Saida
        fields = ['produto', 'quantidade', 'preco']