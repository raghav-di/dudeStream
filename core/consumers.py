import json
from channels.generic.websocket import AsyncWebsocketConsumer

class SignalingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.group_name = f"room_{self.room_name}"
        
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        
        # If a message has a 'target', send it directly to that channel
        if 'target' in data:
            target_channel_name = data['target']
            # Add sender's ID so the recipient knows who it's from
            data['sender'] = self.channel_name
            await self.channel_layer.send(
                target_channel_name,
                {
                    'type': 'signal.message',
                    'data': data
                }
            )
            return

        # If no target, it's a broadcast message (like 'join')
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'signal.message',
                'data': {
                    **data, # Include original data fields
                    'sender': self.channel_name,
                },
                'sender_channel': self.channel_name
            }
        )

    # Receive message from room group or direct send
    async def signal_message(self, event):
        # Don't send messages back to the original sender
        if event.get('sender_channel') == self.channel_name:
            return
            
        await self.send(text_data=json.dumps(event['data']))