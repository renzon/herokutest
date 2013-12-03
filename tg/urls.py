from django.conf.urls import patterns, include, url

from django.contrib import admin
import tg
from tg import views

admin.autodiscover()
urlpatterns = patterns('',
    url(r'usuario/form',views.usuario_form),
     url(r'usuario/salvar',views.usuario_salvar),
    url(r'usuario',views.usuario_lista),
    url(r'^admin/', include(admin.site.urls)),
)

