"""Herashop_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from Herashop import views

urlpatterns = [
    url(r'^$', views.test),
    url(r'^admin/', admin.site.urls),
    url(r'^stores', views.stores),
    url(r'^storetype', views.storetype),
    url(r'^stock/$', views.stock),
    url(r'^stock/(?P<storeid>[0-9]+)/(?P<excludeid>[0-9]+)/$', views.stock),
    url(r'^icon/(?P<path>[\w.]+)/$', views.icon),
    url(r'^image/(?P<path>[\w.-]+)/$', views.image),
    url(r'^imageId/(?P<id>[0-9]+)/$', views.imageId),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

