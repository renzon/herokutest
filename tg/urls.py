from django.conf.urls import patterns, include, url

from django.contrib import admin
import tg
from tg import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'usuario',views.usuario_form),
    url(r'^admin/', include(admin.site.urls)),
)
