#!/usr/bin/env python

import asyncio
import argparse
import json
from websockets.asyncio.server import serve

'''
{
    "type": "adli_metadata",
    "name": "Job Handler",
    "description": "A progam to received sorting jobs and pass to collection of workers.",
    "version": "0.0",
    "language": "python"
}
'''

workers = {}
client = None

MSG_TYPE = {
    "REGISTER": 1,
    "REQUEST": 2,
    "RESPONSE": 3
}

async def send_to_worker(websocket, message):
    '''
        Send message to the given worker.
    '''
    '''adli-encode-output message'''
    await websocket.send(json.dumps(message))

async def send_to_client(websocket, message):
    '''
        Send message to the given client.
    '''
    '''adli-encode-output message'''
    await websocket.send(json.dumps(message))

async def handle_register(websocket, message):
    '''
        Handle register operations.
    '''
    global client, workers  
    if "client" in message:
        client = websocket
        await send_to_client(client, message)
    elif "worker" in message:
        workers[message["type"]] = websocket
        await send_to_worker(workers[message["type"]], message)

async def handle_request(websocket, message): 
    '''
        Handle incoming requests and pass to relevant worker.
    '''
    global client, workers  
    if message["type"] in workers:
        await workers[message["type"]].send(json.dumps(message))
    else:
        message["response"] = f"message['type'] worker isn't initialized"
        print(f"{message['type']} worker isn't initialized")
        await send_to_client(client, message)

async def handle_response(message):   
    '''
        Handle response from worker and pass to client.
    '''
    global client, workers  
    if client:
        await send_to_client(client, message)
    else:
        message["response"] = "Client isn't initialized"
        print(f"client isn't initialized")
        await send_to_client(client, message)

async def handle_message(websocket, message):
    '''
        Handle message received by client.
    '''
    message = json.loads(message)
    print(f"\nReceived message: {message}")

    if message["code"] == MSG_TYPE["REGISTER"]:        
        await handle_register(websocket, message)
    elif message["code"] == MSG_TYPE["REQUEST"]:           
        await handle_request(websocket, message)
    elif message["code"] == MSG_TYPE["RESPONSE"]:        
        await handle_response(message)

async def receieve_message(websocket):
    '''
        Handles messages from websocket.

        1. Workers register using 
        {
            "code": 1,
            "type": "bubbleSort"
            "worker": True
        }

        2. Client Registers using
        {
            "code": 1,
            "client": True
        }

        3. Client runs job using
        {
            "code": 2,
            "client": True,
            "type": "bubbleSort",
            "data": [13,6,3,12,3]
        }
    '''
    async for message in websocket:
        await handle_message(websocket=websocket, message=message)


async def main():
    '''
        Creates a websocket at the provided port and initializes
        the query handler. 
    '''
    parser = argparse.ArgumentParser(description='WebSocket server for sample system queries')

    parser.add_argument('--host',
                        default='localhost',
                        help='Host to bind the server to')
                        
    parser.add_argument('--port',
                        type=int,
                        default=8765,
                        help='Port to bind the server to')
    
    args = parser.parse_args()

    print(f"Starting WebSocket server on {args.host}:{args.port}")
    async with serve(receieve_message, args.host, args.port) as server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())