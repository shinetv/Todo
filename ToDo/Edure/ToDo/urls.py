from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from ToDo import views

urlpatterns = [
    path('',views.login),
    path('sign/',views.sign),
    path('dashboard/',views.dashboard),
    path('logout/',views.logout),
    path('update/<int:id>',views.update),
    path('updateedit/<int:id>',views.updateedit),
    path('delete/<int:id>',views.delete),
    path('deletetask/<int:id>',views.deletetask),
]






if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)