# Minha Jornada de Aprendizado na Semana 5 - Frameworks Python e APIs

Esta semana foi muito rica em aprendizado! Consegui compreender conceitos fundamentais sobre desenvolvimento web com Python e como as tecnologias se conectam para criar soluções modernas.

## Frameworks Python e Django

Descobri que existem diversos frameworks Python para desenvolvimento web, como **Django**, **Flask**, **Web2py**, **CherryPy** e **Bottle**. O Django se destacou como o mais robusto e completo. Entendi que ele é um framework de alto nível, gratuito e open source, que utiliza o padrão **MTV (Model-Template-View)** e segue o princípio **DRY (Don't Repeat Yourself)**. 

O que mais me impressionou foi como o Django facilita o desenvolvimento com seu **ORM integrado**, que mapeia objetos para tabelas do banco de dados, eliminando a necessidade de escrever SQL diretamente. A interface de administração **Django Admin** também é fantástica para gerenciar dados.

## Conceitos de APIs e Web Services

Aprendi as diferenças fundamentais entre **APIs** e **Web Services**. Compreendi que uma API é um conjunto de protocolos que permite comunicação entre aplicativos, podendo ser local ou via rede. Já os Web Services sempre precisam de rede para funcionar. A regra é: 

> **Todo Web Service é uma API, mas nem toda API é um Web Service.**

## Protocolos e Formatos de Dados

Estudei sobre os diferentes protocolos e formatos:

- **XML** e **JSON** para armazenar e transmitir dados
- **HTTP** como protocolo base para transferência na internet
- **SOAP** para troca de informações estruturadas
- **REST** como arquitetura mais ágil e flexível para APIs

## Desenvolvimento Prático com Django

Na parte prática, aprendi a:

1. Criar projetos com `django-admin.py startproject`
2. Desenvolver apps com `django-admin.py startapp`
3. Definir models com campos específicos
4. Usar migrations para estruturar o banco de dados
5. Implementar views para processar requisições
6. Configurar roteamento de URLs
7. Criar templates para interface

## Django REST Framework

O ponto alto foi aprender sobre o **Django REST Framework**. Consegui entender como transformar uma aplicação Django comum em uma API REST, utilizando:

- **Serializers** para converter objetos em JSON
- **APIView** para lidar com requisições HTTP
- **Métodos HTTP** (GET, POST, PUT, DELETE) para operações CRUD
- **Configuração de rotas** para endpoints da API

### Exemplo Prático

```python path=null start=null
# Serializer
class AlunoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AlunoUnivesp
        fields = ['nome', 'sobrenome', 'matricula']

# APIView
class ListaAlunosUnivesp(APIView):
    def get(self, request):
        alunos = AlunoUnivesp.objects.all()
        mat = self.request.params.get('mat', None)
        if matricula:
            alunos = AlunoUnivesp.objects.filter(matricula=mat)
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)
```

## Aplicação Prática

Coloquei tudo em prática criando uma **API REST para gerenciar alunos da Univesp**. Implementei:

- ✅ Serialização da classe `AlunoUnivesp`
- ✅ APIView para listar alunos com filtros por matrícula
- ✅ Configuração das rotas necessárias

Foi gratificante ver como o código ficou limpo e funcional.

## Reflexão Final

Agora me sinto preparada para:

- 🚀 Desenvolver aplicações web completas
- 🔗 Criar APIs que permitem integração entre diferentes sistemas
- 📊 Seguir as melhores práticas de desenvolvimento
- 🛠️ Utilizar o Django para projetos de médio e grande porte

Esta semana realmente consolidou minha compreensão sobre como sistemas modernos se comunicam e como o Python, através do Django, oferece ferramentas poderosas para desenvolvimento web e criação de APIs.

---

**Objetivos de Aprendizagem Alcançados:**

- [x] Identificar frameworks de desenvolvimento em Python
- [x] Conhecer características específicas do framework Django
- [x] Desenvolver aplicações no framework Django com Python
- [x] Entender os conceitos de APIs e webservices
- [x] Exercitar os conceitos aprendidos criando uma API do tipo REST
