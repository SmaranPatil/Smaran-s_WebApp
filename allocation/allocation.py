# allocation/allocation.py

def allocate_rooms(groups, hostels):
    allocation = []
    hostel_dict = {hostel.id: hostel for hostel in hostels}
    
    for group in groups:
        allocated = False
        for hostel in hostels:
            if hostel.gender == group.gender and hostel.capacity >= group.members:
                allocation.append({
                    "group_id": group.group_id,
                    "hostel_name": hostel.hostel_name,
                    "room_number": hostel.room_number,
                    "members_allocated": group.members
                })
                hostel.capacity -= group.members
                allocated = True
                break
        if not allocated:
            allocation.append({
                "group_id": group.group_id,
                "hostel_name": "Not Allocated",
                "room_number": "N/A",
                "members_allocated": 0
            })
    return allocation
