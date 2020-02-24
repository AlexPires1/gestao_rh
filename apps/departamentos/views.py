from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Departamentos
from django.urls import reverse_lazy


class DepartamentosList(ListView):
    model = Departamentos

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamentos.objects.filter(empresa=empresa_logada)

class DepartamentosCreate(CreateView):
    model = Departamentos
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentosCreate, self).form_valid(form)

class DepartamentosUpdate(UpdateView):
    model = Departamentos
    fields = ['nome']

class DepartamentosDelete(DeleteView):
    model = Departamentos
    success_url = reverse_lazy('list_departamentos')