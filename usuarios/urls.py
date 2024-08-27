from django.urls import path

from . import views
from .views import UsuarioCreateView, ListarComprasUsuarioView

urlpatterns = [
    path('cadastro/', UsuarioCreateView.as_view(), name='cadusuario'),
    path('compras/<int:usuario_id>/', ListarComprasUsuarioView.as_view(), name='listar_compras'),
    path('userpedidolist/', views.UsuarioPedidoList.as_view(), name='resumopedido'),
]