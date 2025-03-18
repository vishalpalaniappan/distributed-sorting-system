
import websockets
import asyncio
import json
import random
import time
import uuid

connection = websockets.connect(uri='ws://localhost:8765', ping_interval=None)

MSG_TYPE = {
    "REGISTER": 1,
    "REQUEST": 2,
    "RESPONSE": 3
}

JOB_TYPES = [
    "bubbleSort",
    "mergeSort",
    "radixSort"
]

IS_REGISTERED = False

async def sendRandomJob(websocket, asp_uid):
    # Send response
    await websocket.send(json.dumps({
        "code": MSG_TYPE["REQUEST"],
        "worker": True,
        "type": JOB_TYPES[random.randint(0,2)],
        "data": random.sample(range(6, 101), random.randint(5,15)),
        "asp_uid": asp_uid
    }))

async def main():
    '''
        Main loop receives jobs, executes them and responds.
    '''
    async with connection as websocket:

        asp_uid = str(uuid.uuid4())

        # Send message to register the worker.
        await websocket.send(json.dumps({
            "code": MSG_TYPE["REGISTER"],
            "client": True,
            "asp_uid": asp_uid
        }))

        time.sleep(2)
        try:
            async for message in websocket:
                asp_uid = str(uuid.uuid4())

                await sendRandomJob(websocket= websocket, asp_uid= asp_uid)
                time.sleep(2)
        except KeyboardInterrupt:
            print('interrupted!')
        except:
            pass

        await websocket.close()


async def main2():
    async with connection as websocket:

         # Listen for messages
        async for message in websocket:
            print(message)


if __name__ == "__main__":
    asyncio.run(main())
    asyncio.run(main2())