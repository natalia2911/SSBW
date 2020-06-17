from django.db import models
from django import forms

class Visita(models.Model):
	nombre      = models.CharField(max_length=100)
	descripción = models.CharField(max_length=1000)
	likes       = models.IntegerField(default=0)
	foto = models.FileField(upload_to='foto', blank=True)

class Comentario(models.Model):
	visita      = models.ForeignKey(Visita, on_delete=models.CASCADE)
	texto       = models.CharField(max_length=500)

class VisitaForm(forms.ModelForm):
	class Meta:
		model = Visita
		fields = ['nombre', 'descripción', 'foto']
		widgets = {
			'nombre': forms.TextInput(attrs={'size': 40}),
			'descripción': forms.Textarea(attrs={'rows': 3, 'cols': 50}),
			'foto': forms.FileInput()
		}
	def clean(self):
		data = self.cleaned_data
		if not data["descripcion"][0].isupper():
			raise ValidationError("El campo descripción tiene que comenzar por mayúscula")
