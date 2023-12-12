from django.contrib import admin
from django.urls import path, re_path        # 4 create urls at hello(app) level and import path and repath
from Hello import views      # 4.3  import hello (function) from views


urlpatterns = [                        # 4.1
     path('admin/', admin.site.urls),
     re_path(r'^$', views.Hello, name="Hello"),    # 4.3 takes the function(Hello) directly from views(Hello)
     re_path(r'^List/', views.list_view, name='list_view'),           # 10.7

]