from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('post/<int:pk>/', views.post_page, name='post_page'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('project/<int:pk>/', views.project_page, name='project_page'),
    path('project/new/', views.project_new, name='project_new'),
    path('project/<int:pk>/edit/', views.project_edit, name='project_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)