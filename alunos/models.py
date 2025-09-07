from django.db import models
from django.core.validators import RegexValidator


class Aluno(models.Model):
    """Modelo para representar um aluno da Univesp"""
    
    # Validador para RA (Registro Acadêmico) da Univesp
    ra_validator = RegexValidator(
        regex=r'^\d{10}$',
        message='RA deve conter exatamente 10 dígitos'
    )
    
    # Choices para cursos da Univesp
    CURSOS_CHOICES = [
        ('ENG_COMP', 'Engenharia da Computação'),
        ('CIENCIA_DADOS', 'Ciência de Dados'),
        ('TEC_INFO', 'Tecnologia da Informação'),
        ('MATEMATICA', 'Matemática'),
        ('FISICA', 'Física'),
        ('QUIMICA', 'Química'),
        ('BIOLOGIA', 'Biologia'),
        ('PEDAGOGIA', 'Pedagogia'),
        ('LETRAS', 'Letras'),
        ('ADMINISTRACAO', 'Administração'),
    ]
    
    # Campos do modelo
    ra = models.CharField(
        max_length=10, 
        unique=True, 
        validators=[ra_validator],
        verbose_name='Registro Acadêmico',
        help_text='Registro Acadêmico de 10 dígitos'
    )
    
    nome_completo = models.CharField(
        max_length=200,
        verbose_name='Nome Completo'
    )
    
    email = models.EmailField(
        unique=True,
        verbose_name='E-mail'
    )
    
    curso = models.CharField(
        max_length=20,
        choices=CURSOS_CHOICES,
        verbose_name='Curso'
    )
    
    semestre_atual = models.PositiveIntegerField(
        verbose_name='Semestre Atual',
        help_text='Semestre que o aluno está cursando atualmente'
    )
    
    data_ingresso = models.DateField(
        verbose_name='Data de Ingresso',
        help_text='Data de ingresso no curso'
    )
    
    ativo = models.BooleanField(
        default=True,
        verbose_name='Ativo',
        help_text='Indica se o aluno está ativo no curso'
    )
    
    polo = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Polo de Apoio',
        help_text='Polo de apoio presencial do aluno'
    )
    
    telefone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name='Telefone'
    )
    
    # Campos de controle
    data_criacao = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Criação'
    )
    
    data_atualizacao = models.DateTimeField(
        auto_now=True,
        verbose_name='Data de Atualização'
    )
    
    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['nome_completo']
        indexes = [
            models.Index(fields=['ra']),
            models.Index(fields=['curso']),
            models.Index(fields=['ativo']),
        ]
    
    def __str__(self):
        return f'{self.nome_completo} (RA: {self.ra})'
    
    def get_curso_display_name(self):
        """Retorna o nome completo do curso"""
        return dict(self.CURSOS_CHOICES).get(self.curso, self.curso)
