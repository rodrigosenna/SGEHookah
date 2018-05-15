from django import forms
from core.models import *
#from core.models import Teste

''' class TesteForm(forms.ModelForm):
	nome = forms.CharField(widget=forms.TextInput(attrs={'class':'codProdutoInput'}))
	
	nome.widget.attrs.update({'class':'Descricao'})
	
	class Meta:
		model = Teste
		fields = ['nome', 'descricao'] '''
		
__all__ = ['Teste', 'FreteForm', 'ProdutoForm', 'UpdateInfoForm', 'CategoriaprodutoForm']

class CategoriaprodutoForm(forms.ModelForm):
	nomecategoria = forms.CharField(label="Nome da Categoria", max_length=50)
	
	nomecategoria.widget.attrs.update({'placeholder':'...'})

	class Meta :
		model = Categoriaproduto
		fields = ["nomecategoria"]
		
class ProdutoForm(forms.ModelForm):
	codproduto = forms.CharField(label="*Código", max_length=8)
	nomeproduto = forms.CharField(label="*Nome")
	preco = forms.DecimalField(label="*Preço", max_digits=10, decimal_places=2)
	precocusto = forms.DecimalField(label="Preço de Custo", max_digits=10, decimal_places=2, required=False)
	sabor = forms.CharField(label="*Sabor")
	marca = forms.CharField(label="Marca", required=False)
	altura = forms.FloatField(label="Altura")
	largura = forms.FloatField(label="Largura")
	profundidade = forms.FloatField(label="Profundidade")
	peso = forms.FloatField(label="Peso")
	fkid_categoria = forms.ModelChoiceField(label="Categoria", queryset=Categoriaproduto.objects.filter(hide=False), initial=0)
	fkid_unidademedida = forms.ModelChoiceField(label="Unidade", queryset=Unidademedida.objects.filter(hide=False), initial=0)
	fotoproduto = forms.FileField(label="Escolha a Foto", required=False)
	descricao = forms.CharField(label="Descrição", widget=forms.Textarea, required=False)
	
	descricao.widget.attrs.update({'class':'Descricao'})
	fotoproduto.widget.attrs.update({'class':'FotoInput'})
	altura.widget.attrs.update({'placeholder':'Em cm'})
	largura.widget.attrs.update({'placeholder':'Em cm'})
	profundidade.widget.attrs.update({'placeholder':'Em cm'})
	peso.widget.attrs.update({'placeholder':'Em cm'})
	
	class Meta:
		model = Produto
		fields = ["codproduto", "nomeproduto", "preco", "precocusto",
		"sabor", "marca","altura", "largura", "profundidade", "peso","fkid_unidademedida" ,"fkid_categoria", 
		"fotoproduto", "descricao"]

class Teste(forms.Form):
	nome = forms.CharField(label='Your name', max_length=100)
	idade = forms.CharField(label='Idade', max_length=100)
	teste = forms.CharField(label='teste', max_length=100)
	teste2 = forms.CharField(label='teste2', max_length=100)
	teste3 = forms.CharField(label='teste3', max_length=100)
	teste4 = forms.CharField(label='teste4', max_length=100)
	teste5 = forms.CharField(label='teste5', max_length=100)
	teste5 = forms.CharField(label='teste5', max_length=100)
	
class FreteForm(forms.Form):
	tipo_choices = (('4014', 'Sedex'), ('4510', 'PAC'))
	nCdServico = forms.CharField(label="Serviço", widget=forms.Select(choices=tipo_choices))
	formato_choices = ((1, "Caixa"), (2, "Rolo/Prisma"), (3, "Envelope"))
	nCdFormato = forms.IntegerField(label="Formato", widget=forms.Select(choices=formato_choices))
	sCepOrigem = forms.IntegerField(label="Cep Origem", widget=forms.NumberInput(attrs={'placeholder': '0000000'}))
	sCepDestino = forms.IntegerField(label="Cep Destino", widget=forms.NumberInput(attrs={'placeholder': '0000000'}))
	nVlPeso = forms.FloatField(label="Peso", widget=forms.NumberInput(attrs={'placeholder': 'Peso em Kg'}))
	nVlLargura = forms.FloatField(label="Largura", widget=forms.NumberInput(attrs={'placeholder': 'Largura em cm'}))
	nVlComprimento = forms.FloatField(label="Comprimento", widget=forms.NumberInput(attrs={'placeholder': 'Comprimento em cm'}))
	nVlAltura = forms.FloatField(label="Altura", widget=forms.NumberInput(attrs={'placeholder': 'Altura em cm'}))
	#nVlDiametro = forms.FloatField(label="Diametro")
	#sCdMaoPropria
	#nVlValorDeclarado
	#sCdAvisoRecebimento
	
class UpdateInfoForm(forms.ModelForm):
	email = forms.EmailField(label="E-mail", required=True)
	first_name = forms.CharField(label="Nome", required=True)
	last_name = forms.CharField(label="Sobrenome", required=True)
	
	class Meta :
		model = AuthUser
		fields = ('email', 'first_name', 'last_name')
		
	def clean_email(self):
		email = self.cleaned_data.get('email')
		if email and AuthUser.objects.filter(email=email).count():
			raise forms.ValidationError('Esse e-mail já está em uso.')
		return email
			
	def save(self, commit=True):
		user = super(UpdateInfoForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		
		if commit :
			user.save()
			
		return user
