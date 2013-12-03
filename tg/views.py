# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.forms.models import ModelForm
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.template import loader, Context, RequestContext
from tg.models import Usuario


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'


def usuario_lista(request):
    usuarios = list(Usuario.objects.all())
    tmpl = loader.get_template('usuario_lista.html')
    context = Context({'usuarios': usuarios})
    return HttpResponse(tmpl.render(context))


def usuario_form(request):
    tmpl = loader.get_template('usuario_form.html')
    context = RequestContext(request,{'form': UsuarioForm()})
    return HttpResponse(tmpl.render(context))


def usuario_salvar(request):
    form = UsuarioForm(request.POST)
    form.save()
    return redirect('/usuario')