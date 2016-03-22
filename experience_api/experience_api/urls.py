"""experience_api URL Configuration

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
from django.conf.urls import include, url
from experience_api import views

urlpatterns = [
    url(r'^experience/v1/home$', views.home),
    url(r'^experience/v1/post/(?P<post_id>[0-9]+)$', views.post),
    url(r'^experience/v1/post/new$', views.new_post),
    url(r'^experience/v1/sign_in$', views.sign_in),
    url(r'^experience/v1/sign_up$', views.sign_up),
]
