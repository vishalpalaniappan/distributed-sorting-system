#!/usr/bin/env python

import asyncio
import argparse
import json
from websockets.asyncio.server import serve

msgs = {}

MSG_TYPE = {
    "REGISTER": 1,
    "REQUEST": 2,
    "RESPONSE": 3
}

client = None
async def handle_message(websocket):
    '''
        Handles messages from websocket and echos a response.

        Registering example:
        {
            "code": 1,
            "user": true
        }
        
        Sorting example:
        {
            "code": 2,
            "type": "mergeSort",
            "data": [9323, 5, 8, 0, 2],
            "user": true
        }
    '''
    global client, msgs
    async for message in websocket:
        print(f"Received message: {message}")

        message = json.loads(message)

        # Connection
        if message["code"] == MSG_TYPE["REGISTER"]:
            if "user" in message:
                client = websocket
                await websocket.send(json.dumps(message))
            elif "worker" in message:
                msgs[message["type"]] = websocket
                await websocket.send(json.dumps(message))

        # Request submitted by user
        if message["code"] == MSG_TYPE["REQUEST"]:           
            await msgs[message["type"]].send(json.dumps(message))

        # Response from worker
        if message["code"] == MSG_TYPE["RESPONSE"]:           
            await client.send(json.dumps(message))

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
    async with serve(handle_message, args.host, args.port) as server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())