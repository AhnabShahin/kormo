
from django.contrib import admin
from django.urls import path
from kormo import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path ('login/',views.login, name='login'),
    path ('signup/',views.signup, name='signup'),
    path ('jobList',views.jobList, name='jobList'),
    path ('contact/',views.contact, name='contact'),
]
