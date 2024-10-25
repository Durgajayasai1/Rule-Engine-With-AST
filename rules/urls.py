# rules/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),  # Main page route
    path('create_rule/', views.create_rule, name='create_rule'),
    path('combine_rules/', views.combine_rules, name='combine_rules'),
    path('evaluate_rule/', views.evaluate_rule, name='evaluate_rule'),
    path('modify_rule/', views.modify_rule, name='modify_rule'),
    path('show_all_rules/', views.show_all_rules, name='show_all_rules'),
]
