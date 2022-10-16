from django.contrib import admin
from .models import Room, Topic, Message

# User is added by default

# Register your models here.
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
