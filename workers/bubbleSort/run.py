
import websockets
import asyncio
import json
from bubbleSort import bubble_sort
import uuid

connection = websockets.connect(uri='ws://localhost:8765', ping_interval=None)

MSG_TYPE = {
    "REGISTER": 1,
    "REQUEST": 2,
    "RESPONSE": 3
}

IS_REGISTERED = False


async def send_response(websocket, response):
    await websocket.send(json.dumps(response))

async def handle_request(message):
    # Receieve Task
    print(f"\nTask: {message['type']}")
    print(f"UID: {message['asp_uid']}")
    print(f"Val: {message['data']}")

    # Execute Task
    sortedList = bubble_sort(message["data"])
    resp = {
        "code": MSG_TYPE["RESPONSE"],
        "worker": True,
        "type": "bubbleSort",
        "value": sortedList,
        "asp_uid": message["asp_uid"]
    }
    return resp

async def handle_message(websocket, message):
    message = json.loads(message)
    asp_uid = message["asp_uid"]

    if message["code"] == MSG_TYPE["REQUEST"]:
        response = await handle_request(message=message)
        await send_response(websocket=websocket, response=response)


async def receieve_message():
    '''
        Main loop receives jobs, executes them and responds.
    '''
    async with connection as websocket:
        asp_uid = str(uuid.uuid4())

        # Send message to register the worker.
        await websocket.send(json.dumps({
            "code": MSG_TYPE["REGISTER"],
            "worker": True,
            "type": "bubbleSort",
            "asp_uid": asp_uid
        }))
            
        # Listen for messages
        async for message in websocket:
            await handle_message(websocket=websocket, message=message)

        await websocket.close()

if __name__ == "__main__":
    asyncio.run(receieve_message())