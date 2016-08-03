from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse
#from django.shortcuts import render
#from .models import Paciente

from .models import Paciente
class PacienteAdmin(admin.ModelAdmin):
	#list_display = ['nome','cpf','telefone','celular','endereco','bairro','dentista','valor','formaPagamento','start_date','description','detalhes']
	list_display = ['nome','cpf','telefone','celular','endereco','bairro','dentista','valor','formaPagamento','start_date','description']
	search_fields = ['nome','cpf']
	fieldsets = [(None, { 'fields': (('nome', 'cpf','telefone', 'celular','endereco','bairro','dentista','valor','formaPagamento','start_date'),'description')})]
	#save_as = True
	#save_on_top = True
	#pub_date = 'start_date'-nao sei se deu certo
	#fields = ['nome', 'cpf'] deu certo
	#fieldsets = [(None, { 'fields': ('nome', 'cpf')})]
	list_display_links = ('nome', 'telefone')
	list_per_page = 10 #quantidade de item listadospor paginas
admin.site.register(Paciente,PacienteAdmin) 


"""def index(request):
	pacientes = Paciente.objects.all();
	context={
		'pacientes':pacientes
	}
	return render(request,'index.html', context)"""