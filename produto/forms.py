from django.forms import modelformset_factory, ModelForm, Select, Textarea, TextInput, DateInput, NumberInput
from .models import Produtos

class ProdutoForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['produto', 'cor', 'descricao']
        widgets = {
            'produto': Textarea(attrs={'class' : 'input is-normal'}),
            'cor': Select(attrs={'class': 'input is-normal'}),
            'descricao': Textarea(attrs={'class': 'textarea'}),
        }
