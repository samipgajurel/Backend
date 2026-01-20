from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save
from .models import Attendance

def broadcast_attendance(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "attendance",
        {
            "type": "attendance_update",
            "data": {
                "intern": instance.intern.id,
                "status": instance.status,
                "date": str(instance.date),
            }
        }
    )
