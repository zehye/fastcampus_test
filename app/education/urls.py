from django.urls import path

from . import views

app_name = 'education'
urlpatterns = [
    path('/schools/', views.school_list, name='school-list'),
    path('/schools/<int:school_id>/', views.school_detail, name='school-detail'),
    path('/students/', views.student_list, name='student-list'),
    path('/students/<int:student_id>/', views.student_detail, name='student-detail'),
]
