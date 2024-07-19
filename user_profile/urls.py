from django.urls import path
from . import views
from user_profile import views as profile_views

urlpatterns = [
    path('', views.profile_view, name='profile'),
    path('profile/', profile_views.profile_view, name='profile'),
    path('add_project/', views.add_project, name='add_project'),
    path('edit_project/<int:pk>/', views.edit_project, name='edit_project'),
    path('delete_project/<int:pk>/', views.delete_project, name='delete_project'),
    path('add_education/', views.add_education, name='add_education'),
    path('edit_education/<int:pk>/', views.edit_education, name='edit_education'),
    path('delete_education/<int:pk>/', views.delete_education, name='delete_education'),
    path('add_certification/', views.add_certification, name='add_certification'),
    path('edit_certification/<int:pk>/', views.edit_certification, name='edit_certification'),
    path('delete_certification/<int:pk>/', views.delete_certification, name='delete_certification'),
    path('add_work_experience/', views.add_work_experience, name='add_work_experience'),
    path('edit_work_experience/<int:pk>/', views.edit_work_experience, name='edit_work_experience'),
    path('delete_work_experience/<int:pk>/', views.delete_work_experience, name='delete_work_experience'),
    path('signup/', views.signup, name='signup'),
]