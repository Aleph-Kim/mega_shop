from django.urls import path

import questions.views
from products import views

app_name = 'products'

urlpatterns = [
    path('list/', views.index, name='index'),
    path('<int:product_id>/', views.detail, name='detail'),
    path('<int:product_id>/question/create/', questions.views.create, name='question_create'),
    path('<int:product_id>/question/<int:question_id>/modify/', questions.views.modify, name='question_modify'),
    path('<int:product_id>/question/<int:question_id>/delete/', questions.views.delete, name='question_delete'),
    path('search/', views.search, name='search'),
]
