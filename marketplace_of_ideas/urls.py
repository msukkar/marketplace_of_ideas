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
    url(r'^api/v1/users$', views.users),
    url(r'^api/v1/users/new$', views.users),
    url(r'^api/v1/users/([0-9]+)$', views.users),

    url(r'^api/v1/transactions$', views.transactions),
    url(r'^api/v1/transactions/new$', views.transactions),
    url(r'^api/v1/transactions/([0-9]+)$', views.transactions),

    url(r'^api/v1/posts$', views.posts),
    url(r'^api/v1/posts/new$', views.posts),
    url(r'^api/v1/posts/([0-9]+)$', views.posts),

    url(r'^api/v1/comments$', views.comments),
    url(r'^api/v1/comments/new$', views.comments),
    url(r'^api/v1/comments/([0-9]+)$', views.comments),

    url(r'^$', views.test),
]
