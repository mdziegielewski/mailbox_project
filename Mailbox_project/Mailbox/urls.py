"""Mailbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from mailboxapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^main/new/$', AddNewPersonVeiw.as_view()),
    re_path(r'^main/modify/(?P<id>\d+)$', EditPersonView.as_view(), name="modify"),



    re_path(r'^main/delete/(?P<id>\d+)$', DeletePersonView.as_view()),
    re_path(r'^main/delete/address/(?P<id>\d+)$', DeleteAddressView.as_view()),
    re_path(r'^main/delete/phone/(?P<id>\d+)$', DeletePhoneNumberView.as_view()),
    re_path(r'^main/delete/email/(?P<id>\d+)$', DeleteEmailAddressView.as_view()),
    re_path(r'^main/delete/groups/$', DeleteGroupsView.as_view()),
    re_path(r'^main/delete/personfromgroup/(?P<id>\d+)$', DeletePersonFromGroupView.as_view()),





    re_path(r'^main/show/(?P<id>\d+)$', ShowPersonView.as_view()),

    re_path(r'^main/$', ShowPeopleView.as_view()),

    re_path(r'^main/addaddress/(?P<id>\d+)$', AddNewAddressView.as_view()),
    re_path(r'^main/addpphone/(?P<id>\d+)$', AddNewPhoneNumberView.as_view()),
    re_path(r'^main/addemail/(?P<id>\d+)$', AddNewEmailView.as_view()),

    re_path(r'^main/newgroups/$', AddGroupsView.as_view()),

    re_path(r'^main/linkperosontogroup/(?P<id>\d+)$', AddGroupsPersonView.as_view()),

    re_path(r'^main/search/$', SearchBoxView.as_view()),
]
