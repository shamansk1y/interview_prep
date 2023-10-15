from django.contrib import admin
from django.urls import path
from questions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('easy/', views.easy_page, name='easy_page'),
    path('medium/', views.medium_page, name='medium_page'),
    path('hard/', views.hard_page, name='hard_page'),
]

