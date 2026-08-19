Projeto didático "Id-academico" — app simples para gerenciar alunos

Resumo
- Django app minimal para fins didáticos: CRUD de Aluno (nome, curso, bio).

Setup local (Windows - PowerShell)
1. Criar/ativar venv:
   python -m venv venv
   .\venv\Scripts\Activate.ps1
2. Instalar dependências:
   pip install -r requirements.txt
3. Definir variáveis de ambiente (temporariamente na sessão):
   $env:DJANGO_SECRET_KEY = 'troque-esta-chave'
   $env:DJANGO_DEBUG = 'True'
4. Rodar migrações e servidor:
   python manage.py migrate
   python manage.py runserver
5. Acessar: http://127.0.0.1:8000/ (irá redirecionar para /aluno/)

Alternativa (Unix / macOS)
export DJANGO_SECRET_KEY='troque-chave'
export DJANGO_DEBUG='True'

