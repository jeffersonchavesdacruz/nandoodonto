from django.db import models

class PacienteManager(models.Manager):
	def search(self, query):
		return self.get_queryset().filter(
			models.Q(nome__icontains=query)|models.Q(cpf__icontains=query)
		)

class Paciente(models.Model):
	nome = models.CharField(u'Nome', max_length=100)
	cpf = models.CharField(u'CPF', max_length=100)
	telefone = models.CharField(u'Telefone', max_length=100)
	celular = models.CharField(u'Celular', max_length=100)
	endereco = models.CharField(u'Endereço', max_length=100)
	bairro = models.CharField(u'Bairro', max_length=100)
	dentista = models.CharField(u'Dentista', max_length=100)
	valor = models.CharField(u'Valor Procedimento', max_length=100)
	formaPagamento = models.CharField(u'Forma de Pagamento', max_length=100)
	description = models.TextField('Descrição', blank=True)
	start_date = models.DateField('Data de Inicio', null=True, blank=True)
	created_at = models.DateTimeField('Criado em ', auto_now_add=True)
	update_at = models.DateTimeField('Atualizado em ', auto_now=True)
	objects = PacienteManager()

	
	class Meta:
		verbose_name = 'Paciente'
		verbose_name_plural = 'Pacientes'
		ordering = ['nome']