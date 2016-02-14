"""marketplace_of_ideas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from marketplace_of_ideas import views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^users$', views.test),
    url(r'^users/new$', views.test),
    url(r'^users/([0-9]+)$', views.test),

    url(r'^transactions$', views.test),
    url(r'^transactions/new$', views.test),
    url(r'^transactions/([0-9]+)$', views.test),

    url(r'^posts$', views.test),
    url(r'^posts/new$', views.test),
    url(r'^posts/([0-9]+)$', views.test),

    url(r'^comments$', views.test),
    url(r'^comments/new$', views.test),
    url(r'^comments/([0-9]+)$', views.test),

    url(r'^$', views.test),
]