from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

from .models import Aluno
from .serializers import AlunoSerializer, AlunoCreateSerializer, AlunoListSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    """ViewSet para operações CRUD com alunos da Univesp"""
    
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    
    # Configurações de filtro e busca
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['curso', 'ativo', 'semestre_atual']
    search_fields = ['nome_completo', 'ra', 'email']
    ordering_fields = ['nome_completo', 'ra', 'data_ingresso', 'semestre_atual']
    ordering = ['nome_completo']
    
    def get_serializer_class(self):
        """Retorna o serializer apropriado baseado na ação"""
        if self.action == 'create':
            return AlunoCreateSerializer
        elif self.action == 'list':
            return AlunoListSerializer
        return AlunoSerializer
    
    @action(detail=False, methods=['get'])
    def por_curso(self, request):
        """Endpoint para listar alunos agrupados por curso"""
        curso = request.query_params.get('curso')
        if not curso:
            return Response(
                {'error': 'Parâmetro curso é obrigatório'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        alunos = self.queryset.filter(curso=curso, ativo=True)
        serializer = AlunoListSerializer(alunos, many=True)
        return Response({
            'curso': curso,
            'total_alunos': alunos.count(),
            'alunos': serializer.data
        })
    
    @action(detail=False, methods=['get'])
    def ativos(self, request):
        """Endpoint para listar apenas alunos ativos"""
        alunos = self.queryset.filter(ativo=True)
        serializer = AlunoListSerializer(alunos, many=True)
        return Response({
            'total_alunos_ativos': alunos.count(),
            'alunos': serializer.data
        })
    
    @action(detail=False, methods=['get'])
    def estatisticas(self, request):
        """Endpoint para estatísticas dos alunos"""
        total_alunos = self.queryset.count()
        alunos_ativos = self.queryset.filter(ativo=True).count()
        alunos_inativos = self.queryset.filter(ativo=False).count()
        
        # Estatísticas por curso
        stats_por_curso = {}
        for curso_code, curso_name in Aluno.CURSOS_CHOICES:
            count = self.queryset.filter(curso=curso_code).count()
            if count > 0:
                stats_por_curso[curso_name] = count
        
        return Response({
            'total_alunos': total_alunos,
            'alunos_ativos': alunos_ativos,
            'alunos_inativos': alunos_inativos,
            'distribuicao_por_curso': stats_por_curso
        })
    
    @action(detail=True, methods=['post'])
    def ativar(self, request, pk=None):
        """Endpoint para ativar um aluno"""
        aluno = self.get_object()
        aluno.ativo = True
        aluno.save()
        return Response({
            'message': f'Aluno {aluno.nome_completo} foi ativado com sucesso',
            'ativo': aluno.ativo
        })
    
    @action(detail=True, methods=['post'])
    def desativar(self, request, pk=None):
        """Endpoint para desativar um aluno"""
        aluno = self.get_object()
        aluno.ativo = False
        aluno.save()
        return Response({
            'message': f'Aluno {aluno.nome_completo} foi desativado com sucesso',
            'ativo': aluno.ativo
        })
