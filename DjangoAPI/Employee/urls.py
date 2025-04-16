from django.urls import path
from Employee import views

urlpatterns = [
    path('employee/', views.EmployeeViewSet.as_view({'get': 'list', 'post': 'create'}), name='employee-list'),
    path('employee/<int:pk>/', views.EmployeeViewSet.as_view({ 'put': 'update', 'delete': 'destroy'}), name='employee-detail'),
    path('department/', views.DepartmentViewSet.as_view({'get': 'list', 'post': 'create'}), name='department-list'),
    path('department/<int:pk>/', views.DepartmentViewSet.as_view({ 'put': 'update', 'delete': 'destroy'}), name='department-detail'),
]