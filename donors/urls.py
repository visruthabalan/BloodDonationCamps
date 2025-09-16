from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('', views.donor_list, name='donor_list'),  # home page
    path('donors/view/', views.view_all_donors, name='view_all_donors'),
    path('donors/list/', views.donor_list, name='donor_list'),

    path('donor/register/', views.donor_register, name='donor_register'),
    path('search/', views.search_donors, name='search_donors'),
]
