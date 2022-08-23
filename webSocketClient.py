import websockets
import asyncio
import uuid
import json

autoexecPath = "X:/Steam/steamapps/common/Apex Legends/cfg/autoexec2.cfg"

class WebSocketClient():

    def __init__(self):
        # list of topics to subscribe to
        self.topics = ["channel-points-channel-v1.<CLIENT_ID>"]
        self.auth_token = "<USER_AUTH_TOKEN>"
        pass

    def do_thing(res):
        #C:/Program Files (x86)/Steam/steamapps/common/Apex Legends/cfg/
        #C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg
        
        print(res)

    async def connect(self):
        '''
           Connecting to webSocket server
           websockets.client.connect returns a WebSocketClientProtocol, which is used to send and receive messages
        '''
        self.connection = await websockets.connect('wss://pubsub-edge.twitch.tv')
        if self.connection.open:
            print('Connection stablished. Client correctly connected')
            # Send greeting
            message = {"type": "LISTEN", "nonce": str(self.generate_nonce()), "data":{"topics": self.topics, "auth_token": self.auth_token}}
            json_message = json.dumps(message)
            await self.sendMessage(json_message)
            return self.connection

    def generate_nonce(self):
        '''Generate pseudo-random number and seconds since epoch (UTC).'''
        nonce = uuid.uuid1()
        oauth_nonce = nonce.hex
        return oauth_nonce

    async def sendMessage(self, message):
        '''Sending message to webSocket server'''
        await self.connection.send(message)

    async def receiveMessage(self, connection):
        '''Receiving all server messages and handling them'''
        while True:
            try:
                message = await connection.recv()
                print('Received message from server: ' + str(message))
                json_message = json.loads(message)
                if json_message["type"] == "MESSAGE":

                    json_message = json.loads(json_message["data"]["message"])
                    title = json_message["data"]["redemption"]["reward"]["title"]

                    if title == '5cm':
                        value = 5.2
                    elif title == '10cm':
                        value = 2.6
                    elif title == '15cm':
                        value = 1.75
                    elif title == '20cm':
                        value = 1.3
                    elif title == '25cm':
                        value = 1.039
                    elif title == '100cm':
                        value = 0.25978
                    elif title == '0.03cm':
                        value = 1000
                    elif title == '1000cm':
                        value = 0.01

                    with open(autoexecPath, 'r') as file:
                        data = file.readlines()

                    data[0] = 'mouse_sensitivity \"{}\"\n'.format(value)
                    with open(autoexecPath, 'w') as file:
                        file.writelines(data)
                
            except websockets.exceptions.ConnectionClosed:
                print('Connection with server closed')
                break

    async def heartbeat(self, connection):
        '''
        Sending heartbeat to server every 1 minutes
        Ping - pong messages to verify/keep connection is alive
        '''
        while True:
            try:
                data_set = {"type": "PING"}
                json_request = json.dumps(data_set)
                print(json_request)
                await connection.send(json_request)
                await asyncio.sleep(60)
            except websockets.exceptions.ConnectionClosed:
                print('Connection with server closed')
                break