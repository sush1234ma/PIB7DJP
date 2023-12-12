"""
URL configuration for PI_proj1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path,include   # 3 repath: regular expression used to match the text
from Hello import views                  # 3.1 import views from hello views
# from django.conf.urls import include   # 3.3 import include from django
#(include: repath(include)is enough last commented line is not necessary)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.index, name="index"),   # 3.2 from views call function on views(hello) and name it (anything)
    re_path(r'^Hello/', include('Hello.urls')) ,  # 3.4  go to hello app [(comment after creating urls at hello(app) level

]
# r : raw string dont consider the character as special character
