from django.test import TestCase
from django.utils import timezone
from account_api.models import User
from .models import CompanyInfo, EmployeeInfo, Device, AssignmentDevice


'''
    write unit test for all models 
'''

class CompanyInfoModelTestCase(TestCase):
    def test_string_representation(self):
        company = CompanyInfo(name="Test Company")
        self.assertEqual(str(company), "Test Company")


class EmployeeInfoModelTestCase(TestCase):
    def setUp(self):
        self.company = CompanyInfo.objects.create(name="Test Company")
        self.user = User.objects.create(username="testuser")

    def test_string_representation(self):
        employee = EmployeeInfo(employee=self.user, company=self.company)
        self.assertEqual(str(employee), "testuser")


class DeviceModelTestCase(TestCase):
    def setUp(self):
        self.company = CompanyInfo.objects.create(name="Test Company")

    def test_string_representation(self):
        device = Device(serial_number="123456", company=self.company)
        self.assertEqual(str(device), "123456")


class AssignmentDeviceModelTestCase(TestCase):
    def setUp(self):
        self.company = CompanyInfo.objects.create(name="Test Company")
        self.user = User.objects.create(username="testuser")
        self.employee = EmployeeInfo.objects.create(employee=self.user, company=self.company)
        self.device = Device.objects.create(serial_number="123456", company=self.company)

    def test_string_representation(self):
        assignment = AssignmentDevice(employee=self.employee, device=self.device)
        self.assertEqual(str(assignment), "123456 - testuser")

    def test_return_date_blank_by_default(self):
        assignment = AssignmentDevice(employee=self.employee, device=self.device)
        self.assertIsNone(assignment.return_date)

    def test_return_condition_blank_by_default(self):
        assignment = AssignmentDevice(employee=self.employee, device=self.device)
        self.assertIsNone(assignment.returned_condition)

    def test_return_date_set(self):
        assignment = AssignmentDevice(employee=self.employee, device=self.device, return_date=timezone.now().date())
        self.assertEqual(assignment.return_date, timezone.now().date())

    def test_return_condition_set(self):
        assignment = AssignmentDevice(employee=self.employee, device=self.device, returned_condition="Good")
        self.assertEqual(assignment.returned_condition, "Good")

