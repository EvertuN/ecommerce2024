from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group, User
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from pedidos.models import Pedido
from .forms import CadUsuarioForm


class UsuarioCreateView(CreateView):
    template_name = 'usuario/cadusuario.html'
    form_class = CadUsuarioForm
    success_url = reverse_lazy('loginuser')

    def form_valid(self, form):
        form.cleaned_data
        grupo = get_object_or_404(Group, name='clientes')
        obj = form.save()
        obj.groups.add(grupo)
        messages.success(self.request, f'Usuário Cadastrado!!!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request,
                       'Não foi possível cadastrar o usuário!!!')
        return super().form_invalid(form)


class ListarComprasUsuarioView(LoginRequiredMixin, TemplateView):
    def get(self, request, usuario_id):
        usuario = get_object_or_404(User, pk=usuario_id)
        if usuario == request.user:
            pedidos = Pedido.objects.filter(cliente=usuario).order_by('-criado')
            context = {'pedidos': pedidos, 'usuario': usuario}
            return render(request, 'usuario/usuariopedidolist.html', context)
        else:
            return print("deu erro ai.")


class UsuarioPedidoList(TemplateView):
    template_name = 'usuario/usuariopedidolist.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['pedido'] = Pedido.objects.get(id=self.request.session.get('idpedido'))
        return ctx
