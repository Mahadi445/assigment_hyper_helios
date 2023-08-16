from django.urls import path
from curd import views

urlpatterns = [
    
    path('user-information/', views.user_information, name='user_information'),
    path('contact-list/', views.contact_list_view, name='contact_list'),
    path('update-contact/<int:pk>/', views.update_contact_view, name='update_contact'),
    path('delete-contact/<int:pk>/', views.delete_contact_view, name='delete_contact'),
    
]
