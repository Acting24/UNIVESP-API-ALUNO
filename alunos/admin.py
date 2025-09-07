from django.contrib import admin
from .models import Aluno


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    """Configuração do admin para o modelo Aluno"""
    
    list_display = [
        'ra', 
        'nome_completo', 
        'email', 
        'curso', 
        'semestre_atual', 
        'ativo',
        'data_ingresso'
    ]
    
    list_filter = [
        'curso', 
        'ativo', 
        'semestre_atual', 
        'data_ingresso',
        'polo'
    ]
    
    search_fields = [
        'ra', 
        'nome_completo', 
        'email'
    ]
    
    readonly_fields = [
        'data_criacao', 
        'data_atualizacao'
    ]
    
    fieldsets = [
        ('Informações Pessoais', {
            'fields': ('nome_completo', 'email', 'telefone')
        }),
        ('Informações Acadêmicas', {
            'fields': ('ra', 'curso', 'semestre_atual', 'data_ingresso', 'ativo')
        }),
        ('Localização', {
            'fields': ('polo',)
        }),
        ('Controle do Sistema', {
            'fields': ('data_criacao', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    ]
    
    list_per_page = 25
    ordering = ['nome_completo']
