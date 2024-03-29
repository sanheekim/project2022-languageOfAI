"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from talkingnotepad import views # .html 파일이랑 연동되도록 일단 추가(22.08.26)

urlpatterns = [
    path('admin/', admin.site.urls),
    # polls의 urls.py와 views.py를 연결하려면 필요
    # myproject/urls.py에 namespace='polls'만 추가하면 오류나므로, 꼭 polls/urls.py에 app_name = 'polls' 추가할 것.
    path('polls/', include('polls.urls', namespace='polls')),
    path('talkingnotepad/', include('talkingnotepad.urls', namespace='talkingnotepad')),
]
