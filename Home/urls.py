from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [ 
    path('', views.Home, name='Home'),
    path('detaillist/', views.list, name='details-list'),
    path('update/<int:pk>/', views.update, name='details-update'),
    path('delete/<int:pk>/', views.delete, name='details-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)