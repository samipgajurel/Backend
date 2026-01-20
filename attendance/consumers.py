from channels.generic.websocket import AsyncJsonWebsocketConsumer

class AttendanceConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("attendance", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("attendance", self.channel_name)

    async def attendance_update(self, event):
        await self.send_json(event["data"])
