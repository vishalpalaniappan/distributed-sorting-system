
import websockets
import asyncio
import json
from bubbleSort import bubble_sort

connection = websockets.connect(uri='ws://localhost:8765')

MSG_TYPE = {
    "REGISTER": 1,
    "REQUEST": 2,
    "RESPONSE": 3
}

IS_REGISTERED = False

async def main():
    async with connection as websocket:
        await websocket.send('{"code": 1, "worker": true, "type": "bubbleSort"}')

        async for message in websocket:
            message = json.loads(message)

            if message["code"] == MSG_TYPE["REGISTER"]:
                global IS_REGISTERED
                IS_REGISTERED = True
            else:
                print(f"Task: {message['type']}, Value:{message['data']}")
                resp = {
                    "code": MSG_TYPE["RESPONSE"],
                    "worker": True,
                    "type": "bubbleSort",
                    "value": bubble_sort(message["data"])
                }
                await websocket.send(json.dumps(resp))
            
        await websocket.close()

asyncio.run(main())