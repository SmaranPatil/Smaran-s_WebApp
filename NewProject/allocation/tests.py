# allocation/tests.py

from django.test import TestCase
from .models import Group, Hostel
from .allocation import allocate_rooms

class AllocationTest(TestCase):
    def setUp(self):
        Group.objects.create(group_id="101", members=3, gender="Boys")
        Hostel.objects.create(hostel_name="Boys Hostel A", room_number="101", capacity=3, gender="Boys")

    def test_allocation(self):
        groups = Group.objects.all()
        hostels = Hostel.objects.all()
        allocation = allocate_rooms(groups, hostels)
        self.assertEqual(len(allocation), 1)
        self.assertEqual(allocation[0]['group_id'], "101")
        self.assertEqual(allocation[0]['hostel_name'], "Boys Hostel A")
        self.assertEqual(allocation[0]['room_number'], "101")
        self.assertEqual(allocation[0]['members_allocated'], 3)
