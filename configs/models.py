class RoomManager(models.Manager):
    def get_recent_messages(self, room):
        recent_messages = set()
        for connected_room in room.connected_rooms.all():
            recent_messages.update(connected_room.messages.order_by('-created_at')[:5])
        recent_messages.update(room.messages.order_by('-created_at')[:5])
        return list(recent_messages)[:5]