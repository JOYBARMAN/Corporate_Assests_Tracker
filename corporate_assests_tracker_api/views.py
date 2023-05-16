from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CompanyInfoSerializer, EmployeeInfoSerializer,EmployeeInfoPostSerializer, DeviceSerializer, AssignmentDeviceSerializer,DevicePostSerializer,AssignmentDevicePostSerializer
from .models import CompanyInfo, EmployeeInfo, Device, AssignmentDevice
from  account_api.renderers import UserRenderers
from rest_framework.permissions import IsAuthenticated,IsAdminUser

class CompanyListCreateAPIView(APIView):
    """
    API endpoint for listing and creating companies
    """
    renderer_classes = [UserRenderers]
    permission_classes = [IsAuthenticated,IsAdminUser]
    def get(self, request):
        companies = CompanyInfo.objects.all()
        serializer = CompanyInfoSerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanyInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyRetrieveUpdateDestroyAPIView(APIView):
    """
    API endpoint for retrieving, updating and deleting a company
    """
    renderer_classes = [UserRenderers]
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get_object(self, pk):
        try:
            return CompanyInfo.objects.get(pk=pk)
        except CompanyInfo.DoesNotExist:
            return None

    def get(self, request, pk):
        company = self.get_object(pk)
        if company:
            serializer = CompanyInfoSerializer(company)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        company = self.get_object(pk)
        if company:
            serializer = CompanyInfoSerializer(company, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        company = self.get_object(pk)
        if company:
            company.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


class EmployeeListCreateAPIView(APIView):
    """
    API endpoint for listing and creating employees
    """
    renderer_classes = [UserRenderers]
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get(self, request):
        employees = EmployeeInfo.objects.all()
        serializer = EmployeeInfoSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = EmployeeInfoPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeRetrieveUpdateDestroyAPIView(APIView):
    """
    API endpoint for retrieving, updating and deleting an employee
    """
    renderer_classes = [UserRenderers]
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get_object(self, pk):
        try:
            return EmployeeInfo.objects.get(pk=pk)
        except EmployeeInfo.DoesNotExist:
            return None

    def get(self, request,  pk):
        employee = self.get_object(pk)
        if employee :
            serializer = EmployeeInfoSerializer(employee)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        employee = self.get_object(pk)
        if employee :
            serializer = EmployeeInfoPostSerializer(employee, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        employee = self.get_object(pk)
        if employee :
            employee.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

class DeviceListCreateAPIView(APIView):
    """
    API endpoint for listing and creating devices
    """
    renderer_classes = [UserRenderers]
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get(self, request):
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)


    def post(self, request):
        data = request.data
        serializer = DevicePostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class DeviceRetrieveUpdateDestroyAPIView(APIView):
    """
    API endpoint for retrieving, updating and deleting a device
    """
    renderer_classes = [UserRenderers]
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get_object(self, pk):
        try:
            return Device.objects.get(pk=pk)
        except Device.DoesNotExist:
            return None


    def get(self, request, pk):
        device = self.get_object(pk)
        if device:
            serializer = DeviceSerializer(device)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        device = self.get_object(pk)
        if device:
            serializer = DevicePostSerializer(device, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        device = self.get_object(pk)
        if device :
            device.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
class DeviceAssignmentListCreateAPIView(APIView):
    """
    API endpoint for listing and creating device assignments
    """
    renderer_classes = [UserRenderers]
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get(self, request):
        assignments = AssignmentDevice.objects.all()
        serializer = AssignmentDeviceSerializer(assignments, many=True)
        return Response(serializer.data)


    def post(self, request):
        data = request.data
        serializer = AssignmentDevicePostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class DeviceAssignmentRetrieveUpdateDestroyAPIView(APIView):
    """
    API endpoint for retrieving, updating and deleting a device assignment
    """
    renderer_classes = [UserRenderers]
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get_object(self, pk):
        try:
            return AssignmentDevice.objects.get(pk=pk)
        except AssignmentDevice.DoesNotExist:
            return None

    def get(self, request, pk):
        assignment = self.get_object(pk)
        if assignment :
            serializer = AssignmentDeviceSerializer(assignment)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        assignment = self.get_object(pk)
        if assignment :
            serializer = AssignmentDevicePostSerializer(assignment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request,pk):
        assignment = self.get_object(pk)
        if assignment:
            assignment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)





