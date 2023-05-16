from rest_framework import serializers
from .models import CompanyInfo, EmployeeInfo, Device, AssignmentDevice

class CompanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = '__all__'

class EmployeeInfoSerializer(serializers.ModelSerializer):
    company = CompanyInfoSerializer(read_only=True)

    class Meta:
        model = EmployeeInfo
        fields = '__all__'

class EmployeeInfoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeInfo
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    company = CompanyInfoSerializer(read_only=True)

    class Meta:
        model = Device
        fields = '__all__'

class DevicePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class AssignmentDeviceSerializer(serializers.ModelSerializer):
    employee = EmployeeInfoSerializer(read_only=True)
    device = DeviceSerializer(read_only=True)

    class Meta:
        model = AssignmentDevice
        fields = '__all__'


class AssignmentDevicePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentDevice
        fields = '__all__'
