
import websockets
import asyncio
import json
from mergeSort import mergeSort

connection = websockets.connect(uri='ws://localhost:8765', ping_interval=None)

MSG_TYPE = {
    "REGISTER": 1,
    "REQUEST": 2,
    "RESPONSE": 3
}

IS_REGISTERED = False

async def main():
    '''
        Main loop receives jobs, executes them and responds.
    '''
    async with connection as websocket:

        # Send message to register the worker.
        await websocket.send(json.dumps({
            "code": MSG_TYPE["REGISTER"],
            "worker": True,
            "type": "mergeSort"
        }))

        # Listen for messages
        async for message in websocket:
            message = json.loads(message)

            if message["code"] == MSG_TYPE["REGISTER"]:
                print(f"Registered {message['type']} worker.")
                global IS_REGISTERED
                IS_REGISTERED = True
            else:
                # Receieve Task
                print(f"Task: {message['type']}, Value:{message['data']}")

                # Execute Task
                
                n = len(message["data"])
                sortedList = mergeSort(message["data"], 0, n - 1)
                resp = {
                    "code": MSG_TYPE["RESPONSE"],
                    "worker": True,
                    "type": "mergeSort",
                    "value": sortedList
                }

                # Send response
                await websocket.send(json.dumps(resp))
            
        await websocket.close()

if __name__ == "__main__":
    asyncio.run(main())