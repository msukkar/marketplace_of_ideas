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
    url(r'^users$', views.users),
    url(r'^users/new$', views.users),
    url(r'^users/([0-9]+)$', views.users),

    url(r'^transactions$', views.transactions),
    url(r'^transactions/new$', views.transactions),
    url(r'^transactions/([0-9]+)$', views.transactions),

    url(r'^posts$', views.posts),
    url(r'^posts/new$', views.posts),
    url(r'^posts/([0-9]+)$', views.posts),

    url(r'^comments$', views.comments),
    url(r'^comments/new$', views.comments),
    url(r'^comments/([0-9]+)$', views.comments),

    url(r'^$', views.test),
]