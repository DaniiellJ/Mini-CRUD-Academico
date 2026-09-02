Projeto didático "Id-academico" — app simples para gerenciar alunos

Resumo
- Django app minimal para fins didáticos: CRUD de Aluno (nome, curso, bio).

Setup local (Windows - PowerShell)
1. Criar/ativar venv:
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   
3. Instalar dependências:
   pip install -r requirements.txt
   
4. Rodar migrações e servidor:(principal)
   
   python manage.py migrate
   
   python manage.py runserver
6. Acessar: http://127.0.0.1:8000/ (irá redirecionar para /aluno/)


