from django.urls import path
from .views import CompanyListCreateAPIView, CompanyRetrieveUpdateDestroyAPIView,EmployeeListCreateAPIView, EmployeeRetrieveUpdateDestroyAPIView, DeviceListCreateAPIView, DeviceRetrieveUpdateDestroyAPIView, DeviceAssignmentListCreateAPIView,DeviceAssignmentRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('companies/', CompanyListCreateAPIView.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', CompanyRetrieveUpdateDestroyAPIView.as_view(), name='company-retrieve-update-destroy'),
    path('employees/', EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employee-retrieve-update-destroy'),
    path('devices/', DeviceListCreateAPIView.as_view(), name='device-list-create'),
    path('devices/<int:pk>/', DeviceRetrieveUpdateDestroyAPIView.as_view(), name='device-retrieve-update-destroy'),
    path('assignments/', DeviceAssignmentListCreateAPIView.as_view(), name='device-assignment-list-create'),
    path('assignments/<int:pk>/', DeviceAssignmentRetrieveUpdateDestroyAPIView.as_view(), name='device-assignment-retrieve-update-destroy'),
]
