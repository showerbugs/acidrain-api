"""acidrain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

from users.views import UserView
from users.views import SessionView
from sentences.views import SentenceView
from assessments.views import HistoryView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/$', UserView.as_view(), name='users'),
    url(r'^sessions/$', SessionView.as_view(), name='sessions'),
    url(r'^sentences/$', SentenceView.as_view(), name='sentences'),
    url(r'^assessments/histories/$', HistoryView.as_view(), name='assessment_histories'),
]
