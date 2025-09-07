from rest_framework import serializers
from .models import Aluno


class AlunoSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Aluno"""
    
    curso_nome = serializers.CharField(source='get_curso_display_name', read_only=True)
    
    class Meta:
        model = Aluno
        fields = [
            'id',
            'ra',
            'nome_completo',
            'email',
            'curso',
            'curso_nome',
            'semestre_atual',
            'data_ingresso',
            'ativo',
            'polo',
            'telefone',
            'data_criacao',
            'data_atualizacao'
        ]
        read_only_fields = ['data_criacao', 'data_atualizacao']
    
    def validate_ra(self, value):
        """Valida o RA do aluno"""
        if not value.isdigit():
            raise serializers.ValidationError("RA deve conter apenas números")
        if len(value) != 10:
            raise serializers.ValidationError("RA deve ter exatamente 10 dígitos")
        return value
    
    def validate_semestre_atual(self, value):
        """Valida o semestre atual"""
        if value < 1 or value > 10:
            raise serializers.ValidationError("Semestre deve estar entre 1 e 10")
        return value


class AlunoCreateSerializer(serializers.ModelSerializer):
    """Serializer específico para criação de alunos"""
    
    class Meta:
        model = Aluno
        fields = [
            'ra',
            'nome_completo',
            'email',
            'curso',
            'semestre_atual',
            'data_ingresso',
            'ativo',
            'polo',
            'telefone'
        ]


class AlunoListSerializer(serializers.ModelSerializer):
    """Serializer simplificado para listagem de alunos"""
    
    curso_nome = serializers.CharField(source='get_curso_display_name', read_only=True)
    
    class Meta:
        model = Aluno
        fields = [
            'id',
            'ra',
            'nome_completo',
            'email',
            'curso',
            'curso_nome',
            'semestre_atual',
            'ativo'
        ]
