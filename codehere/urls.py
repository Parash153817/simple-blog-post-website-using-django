from django.urls import path
from . import views

urlpatterns = [

    path('', views.home_view, name='home'),

    path('signup/', views.signup_view, name='signup'),

    path('login/', views.login_view, name='login'),

    path('dashboard/', views.dashboard_view, name='dashboard'),

    path('create-note/',views.create_note_view,name='create_note'),

    path('update-note/<int:note_id>/',views.update_note_view,name='update_note'),

    path('delete-note/<int:note_id>/',views.delete_note_view,name='delete_note'),

    path('logout/',views.logout_view,name='logout'),

    

]