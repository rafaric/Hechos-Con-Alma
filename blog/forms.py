from django import forms


from .models import Post, Categoria, Suscriptores

# choices = Categoria.objects.all().values_list('nombre', 'nombre')
# choice_list = []
# for item in choices:
#     choice_list.append(item)

class PosteoForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), 
                                        widget=forms.Select(attrs={'class':'form-control'})     
                                        )
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'imagen','categoria', 'autor']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class':'form-control','cols': 80, 'rows': 5}),
            # 'categoria': forms.RadioSelect(attrs={'class':'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control','type': 'hidden', 'id': 'autor', 'value': ''}),
            #'autor': forms.Select(attrs={'class': 'form-control'}),
        }

class EdicionForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class':'form-control','cols': 80, 'rows': 5}),
            #'autor': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
        }
        
class suscripcion(forms.ModelForm):
    class Meta:
        model = Suscriptores
        fields= ['nombre','apellido','correo']
        Widget = {
            'nombre': forms.TextInput(),
            'apellido': forms.TextInput(),
            'correo': forms.EmailInput(),
        }
