
import websockets
import asyncio
import json
from radixSort import radixSort
import uuid

'''
    {
        "type": "adli_metadata",
        "value": {
            "name": "Radix Sort",
            "description": "A program to receive sorting jobs over a websocket server and return the sorted results.",
            "version": "0.0",
            "language": "python"
        }
    }
'''
connection = websockets.connect(uri='ws://localhost:8765', ping_interval=None)

MSG_TYPE = {
    "REGISTER": 1,
    "REQUEST": 2,
    "RESPONSE": 3
}

IS_REGISTERED = False


async def send_response(websocket, response):
    '''
        Send response to job handler.
    '''
    '''adli-encode-output response'''    
    await websocket.send(json.dumps(response))

async def handle_request(message):
    '''
        Handle request from job handler.
    '''
    # Print task info
    print(f"\nTask: {message['type']}")
    print(f"UID: {message['asp_uid']}")
    print(f"Val: {message['data']}")
    print(f"User: {message['user']}")

    # Execute Task
    n = len(message["data"])
    sortedList = radixSort(message["data"])
    resp = {
        "code": MSG_TYPE["RESPONSE"],
        "worker": True,
        "type": "radixSort",
        "value": sortedList,
        "asp_uid": message["asp_uid"],
        "user": message["user"]
    }
    return resp

async def handle_message(websocket, message):
    '''
        Handle the received message.
    '''
    message = json.loads(message)
    asp_uid = message["asp_uid"]

    if message["code"] == MSG_TYPE["REQUEST"]:
        response = await handle_request(message=message)
        await send_response(websocket=websocket, response=response)

async def register(websocket):
    '''
        Register the worker with the job handler.
    '''
    asp_uid = str(uuid.uuid4())

    response = {
        "code": MSG_TYPE["REGISTER"],
        "worker": True,
        "type": "radixSort",
        "asp_uid": asp_uid
    }
    # Send message to register the worker.
    await send_response(websocket=websocket, response=response)


async def receieve_message():
    '''
        Main loop receives jobs, executes them and responds.
    '''
    async with connection as websocket:
        await register(websocket=websocket)
        # Listen for messages
        async for message in websocket:
            await handle_message(websocket=websocket, message=message)

        await websocket.close()

if __name__ == "__main__":
    asyncio.run(receieve_message())