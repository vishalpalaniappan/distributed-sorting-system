
import websockets
import asyncio
import json
from mergeSort import mergeSort

connection = websockets.connect(uri='ws://localhost:8765')

MSG_TYPE = {
    "REGISTER": 1,
    "REQUEST": 2,
    "RESPONSE": 3
}

async def main():
    async with connection as websocket:
        await websocket.send('{"code": 1, "worker": true, "type": "mergeSort"}')

        async for message in websocket:
            message = json.loads(message)

            if message["code"] == MSG_TYPE["REGISTER"]:
                global IS_REGISTERED
                IS_REGISTERED = True
            else:
                print(f"Task: {message['type']}, Value:{message['data']}")
                n = len(message["data"])
                resp = {
                    "code": MSG_TYPE["RESPONSE"],
                    "worker": True,
                    "type": "mergeSort",
                    "value": mergeSort(message["data"], 0, n-1)
                }
                await websocket.send(json.dumps(resp))
            
        await websocket.close()

asyncio.run(main())