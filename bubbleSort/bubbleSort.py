
import websockets
import asyncio
import json

connection = websockets.connect(uri='ws://localhost:8765')

MSG_TYPE = {
    "CONNECT": 1,
    "REQUEST": 2,
    "RESPONSE": 3
}

IS_REGISTERED = False

def bubble_sort(arr):
    # Taken from here: https://www.geeksforgeeks.org/python-program-for-bubble-sort/
    
    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):
        swapped = False  
        for i in range(n):
            if arr[i] > arr[i + 1]:

                # Swap elements if they are in the wrong order
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        if not swapped:
            break

    return arr
    

async def main():
    async with connection as websocket:
        await websocket.send('{"code": 1, "worker": true, "type": "bubbleSort"}')

        async for message in websocket:
            message = json.loads(message)

            if message["code"] == MSG_TYPE["CONNECT"]:
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