from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('aluno/', include('aluno.urls')),

    path('', RedirectView.as_view(pattern_name='lista_alunos', permanent=False)),
]
