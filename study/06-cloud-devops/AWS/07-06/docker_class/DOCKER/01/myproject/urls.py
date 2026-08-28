from django.contrib import admin
from django.urls import path
from .views import infer_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/chat/', infer_view, name='chat-api'),
]
