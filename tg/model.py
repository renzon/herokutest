# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models
from django.db.models.base import Model


class Usuario(Model):
    nome = models.CharField()
    telefone = models.CharField()

