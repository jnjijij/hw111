room = Room.objects.get(id=your_room_id)
recent_messages = room.get_recent_unique_messages()