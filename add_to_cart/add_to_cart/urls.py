from django.conf.urls import include, url
from django.contrib import admin
from demo.views import *
from simple_mail.views import *

urlpatterns = [
    # Examples:
    url(r'^$', 'demo.views.home', name='home'),
    url(r'^link/', 'demo.views.AddToCartDavidson', name='link'),
    url(r'^cookie/', 'demo.views.Cookie_Monster', name='cookie'),
    url(r'^email/', 'simple_mail.views.email', name='email'),
    url(r'^admin/', include(admin.site.urls)),
]
