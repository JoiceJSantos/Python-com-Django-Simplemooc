from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


app_name ='accounts'

LoginView.template_name = 'accounts/login.html'
LogoutView.next_page = 'core:home'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('entrar/', LoginView.as_view(), name='login'),
    path('sair/', LogoutView.as_view(), name='logout'),
    path('cadastre-se/', views.register, name='register'),
    path('editar/', views.editar, name='edit'),
    path('nova-senha/', views.password_reset, name='password_reset'),
    path('confirmar-nova-senha/<str:key>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('editar-senha/', views.edit_password, name='edit_password'),
]

