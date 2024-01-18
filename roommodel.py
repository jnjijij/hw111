class Room(models.Model):
    # Your Room model fields here

    objects = models.Manager()  # The default manager
    recent_messages = RoomManager()  # Your custom manager

    # Your Room model methods here