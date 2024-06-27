# allocation/views.py

import csv
from django.shortcuts import render
from django.http import JsonResponse
from .models import Group, Hostel
from .allocation import allocate_rooms
from django.http import JsonResponse


def upload_csv(request):
    if request.method == "POST":
        group_file = request.FILES['group_file']
        hostel_file = request.FILES['hostel_file']
        
        # Parse group file
        Group.objects.all().delete()
        group_reader = csv.reader(group_file.read().decode('utf-8').splitlines())
        next(group_reader)  # Skip header
        for row in group_reader:
            Group.objects.create(group_id=row[0], members=row[1], gender=row[2])
        
        # Parse hostel file
        Hostel.objects.all().delete()
        hostel_reader = csv.reader(hostel_file.read().decode('utf-8').splitlines())
        next(hostel_reader)  # Skip header
        for row in hostel_reader:
            Hostel.objects.create(hostel_name=row[0], room_number=row[1], capacity=row[2], gender=row[3])
        
        # Perform allocation
        groups = Group.objects.all()
        hostels = Hostel.objects.all()
        allocation = allocate_rooms(groups, hostels)
        
        return JsonResponse(allocation, safe=False)

    return render(request, 'upload.html')

def get_allocations(request):
    # Fetch allocation data from the database or perform logic here
    # This is a placeholder, replace with actual data retrieval logic
    allocations = []
    return JsonResponse(allocations, safe=False)
