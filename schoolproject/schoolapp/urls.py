from django.urls import path
from . import views
from django.conf.urls.static import static
from school import settings


urlpatterns = [
    path('', views.demo, name='demo'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout',views.logout, name='logout'),
    path('form/',views.form_view, name='form')
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)