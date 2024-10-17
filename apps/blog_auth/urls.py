from django.urls import path
from .views import SignUpView, LoginView, ListarEventosView, DetalleEventoView, CrearEventoView, ActualizarEventoView, EliminarEventoView
from django.contrib.auth.views import LogoutView

app_name = "apps.blog_auth"

urlpatterns = [
    path("register/", SignUpView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="/auth/login/"), name="logout"),
    path('', ListarEventosView.as_view(), name='lista_eventos'),
    path('<int:pk>', DetalleEventoView.as_view(), name='detalle_eventos'),
    path('crear/', CrearEventoView.as_view(), name='crear_evento'),
    path('editar/<int:pk>/', ActualizarEventoView.as_view(),
         name='actualizar_evento'),
    path('eliminar/<int:pk>/', EliminarEventoView.as_view(), name='eliminar_evento'),
]
