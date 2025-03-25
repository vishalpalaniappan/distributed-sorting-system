import traceback
import logging
import json
import sys
from pathlib import Path
from clp_logging.handlers import CLPFileHandler
clp_handler = CLPFileHandler(Path('./jobHandler.clp.zst'))
logger = logging.getLogger('adli')
logger.setLevel(logging.INFO)
logger.addHandler(clp_handler)

def aspAdliVarLog(val, varid):
    try:
        val = json.dumps(val, default=lambda o: o.__dict__)
    except:
        pass
    logger.info(f'# {varid} {val}')

def aspTraceLog(traceType, value):
    try:
        value = json.dumps(value, default=lambda o: o.__dict__)
    except:
        pass
    logger.info(f'@ {traceType} {value}')
logger.info('{"fileTree": {"jobHandler.py": {"source": "#!/usr/bin/env python\\n\\nimport asyncio\\nimport argparse\\nimport json\\nfrom websockets.asyncio.server import serve\\n\\nworkers = {}\\nclient = None\\n\\nMSG_TYPE = {\\n    \\"REGISTER\\": 1,\\n    \\"REQUEST\\": 2,\\n    \\"RESPONSE\\": 3\\n}\\n\\nasync def send_to_worker(websocket, message):\\n    \'\'\'\\n        Send message to the given worker.\\n    \'\'\'\\n    await websocket.send(json.dumps(message))\\n\\nasync def send_to_client(websocket, message):\\n    \'\'\'\\n        Send message to the given client.\\n    \'\'\'\\n    await websocket.send(json.dumps(message))\\n\\nasync def handle_register(websocket, message):\\n    \'\'\'\\n        Handle register operations.\\n    \'\'\'\\n    global client, workers  \\n    if \\"client\\" in message:\\n        client = websocket\\n        await send_to_client(client, message)\\n    elif \\"worker\\" in message:\\n        workers[message[\\"type\\"]] = websocket\\n        await send_to_worker(workers[message[\\"type\\"]], message)\\n\\nasync def handle_request(websocket, message): \\n    \'\'\'\\n        Handle incoming requests and pass to relevant worker.\\n    \'\'\'\\n    if message[\\"type\\"] in workers:\\n        await workers[message[\\"type\\"]].send(json.dumps(message))\\n    else:\\n        message[\\"response\\"] = f\\"message[\'type\'] worker isn\'t initialized\\"\\n        print(f\\"{message[\'type\']} worker isn\'t initialized\\")\\n        await websocket.send(json.dumps(message))\\n\\nasync def handle_response(message):   \\n    \'\'\'\\n        Handle response from worker and pass to client.\\n    \'\'\'\\n    global client, workers  \\n    if client:\\n        await send_to_client(client, message)\\n    else:\\n        message[\\"response\\"] = \\"Client isn\'t initialized\\"\\n        print(f\\"client isn\'t initialized\\")\\n        await send_to_client(client, message)\\n\\nasync def handle_message(websocket, message):\\n    \'\'\'\\n        Handle message received by client.\\n    \'\'\'\\n    message = json.loads(message)\\n    asp_uid = message[\\"asp_uid\\"]\\n    print(f\\"\\\\nReceived message: {message}\\")\\n\\n    if message[\\"code\\"] == MSG_TYPE[\\"REGISTER\\"]:        \\n        await handle_register(websocket, message)\\n    elif message[\\"code\\"] == MSG_TYPE[\\"REQUEST\\"]:           \\n        await handle_request(websocket, message)\\n    elif message[\\"code\\"] == MSG_TYPE[\\"RESPONSE\\"]:        \\n        await handle_response(message)\\n\\nasync def receieve_message(websocket):\\n    \'\'\'\\n        Handles messages from websocket.\\n\\n        1. Workers register using \\n        {\\n            \\"code\\": 1,\\n            \\"type\\": \\"bubbleSort\\"\\n            \\"worker\\": True\\n        }\\n\\n        2. Client Registers using\\n        {\\n            \\"code\\": 1,\\n            \\"client\\": True\\n        }\\n\\n        3. Client runs job using\\n        {\\n            \\"code\\": 2,\\n            \\"client\\": True,\\n            \\"type\\": \\"bubbleSort\\",\\n            \\"data\\": [13,6,3,12,3]\\n        }\\n    \'\'\'\\n    async for message in websocket:\\n        await handle_message(websocket=websocket, message=message)\\n\\n\\nasync def main():\\n    \'\'\'\\n        Creates a websocket at the provided port and initializes\\n        the query handler. \\n    \'\'\'\\n    parser = argparse.ArgumentParser(description=\'WebSocket server for sample system queries\')\\n\\n    parser.add_argument(\'--host\',\\n                        default=\'localhost\',\\n                        help=\'Host to bind the server to\')\\n                        \\n    parser.add_argument(\'--port\',\\n                        type=int,\\n                        default=8765,\\n                        help=\'Port to bind the server to\')\\n    \\n    args = parser.parse_args()\\n\\n    print(f\\"Starting WebSocket server on {args.host}:{args.port}\\")\\n    async with serve(receieve_message, args.host, args.port) as server:\\n        await server.serve_forever()\\n\\nif __name__ == \\"__main__\\":\\n    asyncio.run(main())", "minLt": 0, "maxLt": 63}}, "ltMap": {"1": {"id": 1, "funcid": 0, "lineno": 3, "end_lineno": 3, "type": "child"}, "2": {"id": 2, "funcid": 0, "lineno": 4, "end_lineno": 4, "type": "child"}, "3": {"id": 3, "funcid": 0, "lineno": 5, "end_lineno": 5, "type": "child"}, "4": {"id": 4, "funcid": 0, "lineno": 6, "end_lineno": 6, "type": "child"}, "5": {"id": 5, "funcid": 0, "lineno": 8, "end_lineno": 8, "type": "child"}, "6": {"id": 6, "funcid": 0, "lineno": 9, "end_lineno": 9, "type": "child"}, "7": {"id": 7, "funcid": 0, "lineno": 11, "end_lineno": 15, "type": "child"}, "8": {"id": 8, "funcid": 8, "lineno": 17, "end_lineno": 21, "type": "function", "name": "send_to_worker"}, "9": {"id": 9, "funcid": 8, "lineno": 18, "end_lineno": 20, "type": "child"}, "10": {"id": 10, "funcid": 8, "lineno": 21, "end_lineno": 21, "type": "child"}, "11": {"id": 11, "funcid": 11, "lineno": 23, "end_lineno": 27, "type": "function", "name": "send_to_client"}, "12": {"id": 12, "funcid": 11, "lineno": 24, "end_lineno": 26, "type": "child"}, "13": {"id": 13, "funcid": 11, "lineno": 27, "end_lineno": 27, "type": "child"}, "14": {"id": 14, "funcid": 14, "lineno": 29, "end_lineno": 39, "type": "function", "name": "handle_register"}, "15": {"id": 15, "funcid": 14, "lineno": 30, "end_lineno": 32, "type": "child"}, "16": {"id": 16, "funcid": 14, "lineno": 33, "end_lineno": 33, "type": "child"}, "17": {"id": 17, "funcid": 14, "lineno": 34, "end_lineno": 39, "type": "child"}, "18": {"id": 18, "funcid": 14, "lineno": 35, "end_lineno": 35, "type": "child"}, "19": {"id": 19, "funcid": 14, "lineno": 36, "end_lineno": 36, "type": "child"}, "20": {"id": 20, "funcid": 14, "lineno": 37, "end_lineno": 39, "type": "child"}, "21": {"id": 21, "funcid": 14, "lineno": 38, "end_lineno": 38, "type": "child"}, "22": {"id": 22, "funcid": 14, "lineno": 39, "end_lineno": 39, "type": "child"}, "23": {"id": 23, "funcid": 23, "lineno": 41, "end_lineno": 50, "type": "function", "name": "handle_request"}, "24": {"id": 24, "funcid": 23, "lineno": 42, "end_lineno": 44, "type": "child"}, "25": {"id": 25, "funcid": 23, "lineno": 45, "end_lineno": 50, "type": "child"}, "26": {"id": 26, "funcid": 23, "lineno": 46, "end_lineno": 46, "type": "child"}, "27": {"id": 27, "funcid": 23, "lineno": 48, "end_lineno": 48, "type": "child"}, "28": {"id": 28, "funcid": 23, "lineno": 49, "end_lineno": 49, "type": "child"}, "29": {"id": 29, "funcid": 23, "lineno": 50, "end_lineno": 50, "type": "child"}, "30": {"id": 30, "funcid": 30, "lineno": 52, "end_lineno": 62, "type": "function", "name": "handle_response"}, "31": {"id": 31, "funcid": 30, "lineno": 53, "end_lineno": 55, "type": "child"}, "32": {"id": 32, "funcid": 30, "lineno": 56, "end_lineno": 56, "type": "child"}, "33": {"id": 33, "funcid": 30, "lineno": 57, "end_lineno": 62, "type": "child"}, "34": {"id": 34, "funcid": 30, "lineno": 58, "end_lineno": 58, "type": "child"}, "35": {"id": 35, "funcid": 30, "lineno": 60, "end_lineno": 60, "type": "child"}, "36": {"id": 36, "funcid": 30, "lineno": 61, "end_lineno": 61, "type": "child"}, "37": {"id": 37, "funcid": 30, "lineno": 62, "end_lineno": 62, "type": "child"}, "38": {"id": 38, "funcid": 38, "lineno": 64, "end_lineno": 77, "type": "function", "name": "handle_message"}, "39": {"id": 39, "funcid": 38, "lineno": 65, "end_lineno": 67, "type": "child"}, "40": {"id": 40, "funcid": 38, "lineno": 68, "end_lineno": 68, "type": "child"}, "41": {"id": 41, "funcid": 38, "lineno": 69, "end_lineno": 69, "type": "child"}, "42": {"id": 42, "funcid": 38, "lineno": 70, "end_lineno": 70, "type": "child"}, "43": {"id": 43, "funcid": 38, "lineno": 72, "end_lineno": 77, "type": "child"}, "44": {"id": 44, "funcid": 38, "lineno": 73, "end_lineno": 73, "type": "child"}, "45": {"id": 45, "funcid": 38, "lineno": 74, "end_lineno": 77, "type": "child"}, "46": {"id": 46, "funcid": 38, "lineno": 75, "end_lineno": 75, "type": "child"}, "47": {"id": 47, "funcid": 38, "lineno": 76, "end_lineno": 77, "type": "child"}, "48": {"id": 48, "funcid": 38, "lineno": 77, "end_lineno": 77, "type": "child"}, "49": {"id": 49, "funcid": 49, "lineno": 79, "end_lineno": 105, "type": "function", "name": "receieve_message"}, "50": {"id": 50, "funcid": 49, "lineno": 80, "end_lineno": 103, "type": "child"}, "51": {"id": 51, "funcid": 49, "lineno": 104, "end_lineno": 105, "type": "child"}, "52": {"id": 52, "funcid": 49, "lineno": 105, "end_lineno": 105, "type": "child"}, "53": {"id": 53, "funcid": 53, "lineno": 108, "end_lineno": 128, "type": "function", "name": "main"}, "54": {"id": 54, "funcid": 53, "lineno": 109, "end_lineno": 112, "type": "child"}, "55": {"id": 55, "funcid": 53, "lineno": 113, "end_lineno": 113, "type": "child"}, "56": {"id": 56, "funcid": 53, "lineno": 115, "end_lineno": 117, "type": "child"}, "57": {"id": 57, "funcid": 53, "lineno": 119, "end_lineno": 122, "type": "child"}, "58": {"id": 58, "funcid": 53, "lineno": 124, "end_lineno": 124, "type": "child"}, "59": {"id": 59, "funcid": 53, "lineno": 126, "end_lineno": 126, "type": "child"}, "60": {"id": 60, "funcid": 53, "lineno": 127, "end_lineno": 128, "type": "child"}, "61": {"id": 61, "funcid": 53, "lineno": 128, "end_lineno": 128, "type": "child"}, "62": {"id": 62, "funcid": 0, "lineno": 130, "end_lineno": 131, "type": "child"}, "63": {"id": 63, "funcid": 0, "lineno": 131, "end_lineno": 131, "type": "child"}}, "varMap": {"1": {"varId": 1, "name": "workers", "keys": [], "logType": 5, "funcId": 0, "isTemp": false, "global": true}, "2": {"varId": 2, "name": "client", "keys": [], "logType": 6, "funcId": 0, "isTemp": false, "global": true}, "3": {"varId": 3, "name": "MSG_TYPE", "keys": [], "logType": 7, "funcId": 0, "isTemp": false, "global": true}, "4": {"varId": 4, "name": "websocket", "keys": [], "logType": 10, "funcId": 8, "isTemp": false, "global": false}, "5": {"varId": 5, "name": "message", "keys": [], "logType": 10, "funcId": 8, "isTemp": false, "global": false}, "6": {"varId": 6, "name": "websocket", "keys": [], "logType": 13, "funcId": 11, "isTemp": false, "global": false}, "7": {"varId": 7, "name": "websocket", "keys": [], "logType": 13, "funcId": 11, "isTemp": false, "global": false}, "8": {"varId": 8, "name": "message", "keys": [], "logType": 13, "funcId": 11, "isTemp": false, "global": false}, "9": {"varId": 9, "name": "client", "keys": [], "logType": 18, "funcId": 14, "isTemp": false, "global": true}, "10": {"varId": 10, "name": "asp_temp_var_89bd4d16099b11f0aaa963f0c00b7079", "keys": [], "logType": 21, "funcId": 14, "isTemp": true, "global": false}, "11": {"varId": 11, "name": "workers", "keys": [{"type": "temp_variable", "value": "asp_temp_var_89bd4d16099b11f0aaa963f0c00b7079"}], "logType": 21, "funcId": 14, "isTemp": false, "global": true}, "12": {"varId": 12, "name": "websocket", "keys": [], "logType": 22, "funcId": 14, "isTemp": false, "global": false}, "13": {"varId": 13, "name": "message", "keys": [], "logType": 22, "funcId": 14, "isTemp": false, "global": false}, "14": {"varId": 14, "name": "asp_temp_var_89bd4d17099b11f0aaa963f0c00b7079", "keys": [], "logType": 26, "funcId": 23, "isTemp": true, "global": false}, "15": {"varId": 15, "name": "workers", "keys": [{"type": "variable", "value": "json"}], "logType": 26, "funcId": 23, "isTemp": false, "global": false}, "16": {"varId": 16, "name": "message", "keys": [{"type": "key", "value": "response"}], "logType": 27, "funcId": 23, "isTemp": false, "global": false}, "17": {"varId": 17, "name": "websocket", "keys": [], "logType": 29, "funcId": 23, "isTemp": false, "global": false}, "18": {"varId": 18, "name": "websocket", "keys": [], "logType": 29, "funcId": 23, "isTemp": false, "global": false}, "19": {"varId": 19, "name": "message", "keys": [], "logType": 29, "funcId": 23, "isTemp": false, "global": false}, "20": {"varId": 20, "name": "message", "keys": [{"type": "key", "value": "response"}], "logType": 35, "funcId": 30, "isTemp": false, "global": false}, "21": {"varId": 21, "name": "message", "keys": [], "logType": 37, "funcId": 30, "isTemp": false, "global": false}, "22": {"varId": 22, "name": "message", "keys": [], "logType": 40, "funcId": 38, "isTemp": false, "global": false}, "23": {"varId": 23, "name": "asp_uid", "keys": [], "logType": 41, "funcId": 38, "isTemp": false, "global": false}, "24": {"varId": 24, "name": "websocket", "keys": [], "logType": 48, "funcId": 38, "isTemp": false, "global": false}, "25": {"varId": 25, "name": "message", "keys": [], "logType": 48, "funcId": 38, "isTemp": false, "global": false}, "26": {"varId": 26, "name": "message", "keys": [], "logType": 52, "funcId": 49, "isTemp": false, "global": false}, "27": {"varId": 27, "name": "websocket", "keys": [], "logType": 52, "funcId": 49, "isTemp": false, "global": false}, "28": {"varId": 28, "name": "parser", "keys": [], "logType": 55, "funcId": 53, "isTemp": false, "global": false}, "29": {"varId": 29, "name": "parser", "keys": [], "logType": 56, "funcId": 53, "isTemp": false, "global": false}, "30": {"varId": 30, "name": "parser", "keys": [], "logType": 57, "funcId": 53, "isTemp": false, "global": false}, "31": {"varId": 31, "name": "args", "keys": [], "logType": 58, "funcId": 53, "isTemp": false, "global": false}, "32": {"varId": 32, "name": "parser", "keys": [], "logType": 58, "funcId": 53, "isTemp": false, "global": false}, "33": {"varId": 33, "name": "server", "keys": [], "logType": 61, "funcId": 53, "isTemp": false, "global": false}}}')
try:
    logger.info(1)
    import asyncio
    logger.info(2)
    import argparse
    logger.info(3)
    import json
    logger.info(4)
    from websockets.asyncio.server import serve
    logger.info(5)
    workers = {}
    aspAdliVarLog(workers, 1)
    logger.info(6)
    client = None
    aspAdliVarLog(client, 2)
    logger.info(7)
    MSG_TYPE = {'REGISTER': 1, 'REQUEST': 2, 'RESPONSE': 3}
    aspAdliVarLog(MSG_TYPE, 3)

    async def send_to_worker(websocket, message):
        logger.info(8)
        aspAdliVarLog(websocket, 4)
        aspAdliVarLog(message, 5)
        logger.info(9)
        '\n        Send message to the given worker.\n    '
        logger.info(10)
        await websocket.send(json.dumps(message))

    async def send_to_client(websocket, message):
        logger.info(11)
        aspAdliVarLog(websocket, 7)
        aspAdliVarLog(message, 8)
        logger.info(12)
        '\n        Send message to the given client.\n    '
        logger.info(13)
        await websocket.send(json.dumps(message))
        aspAdliVarLog(websocket, 6)

    async def handle_register(websocket, message):
        logger.info(14)
        aspAdliVarLog(websocket, 12)
        aspAdliVarLog(message, 13)
        logger.info(15)
        '\n        Handle register operations.\n    '
        logger.info(16)
        global client, workers
        logger.info(17)
        if 'client' in message:
            logger.info(18)
            client = websocket
            aspAdliVarLog(client, 9)
            logger.info(19)
            await send_to_client(client, message)
        else:
            logger.info(20)
            if 'worker' in message:
                asp_temp_var_89bd4d16099b11f0aaa963f0c00b7079 = message['type']
                aspAdliVarLog(asp_temp_var_89bd4d16099b11f0aaa963f0c00b7079, 10)
                logger.info(21)
                workers[asp_temp_var_89bd4d16099b11f0aaa963f0c00b7079] = websocket
                aspAdliVarLog(workers[asp_temp_var_89bd4d16099b11f0aaa963f0c00b7079], 11)
                logger.info(22)
                await send_to_worker(workers[message['type']], message)

    async def handle_request(websocket, message):
        logger.info(23)
        aspAdliVarLog(websocket, 18)
        aspAdliVarLog(message, 19)
        logger.info(24)
        '\n        Handle incoming requests and pass to relevant worker.\n    '
        logger.info(25)
        if message['type'] in workers:
            asp_temp_var_89bd4d17099b11f0aaa963f0c00b7079 = message['type']
            aspAdliVarLog(asp_temp_var_89bd4d17099b11f0aaa963f0c00b7079, 14)
            logger.info(26)
            await workers[asp_temp_var_89bd4d17099b11f0aaa963f0c00b7079].send(json.dumps(message))
            aspAdliVarLog(workers[asp_temp_var_89bd4d17099b11f0aaa963f0c00b7079], 15)
        else:
            logger.info(27)
            message['response'] = f"message['type'] worker isn't initialized"
            aspAdliVarLog(message['response'], 16)
            logger.info(28)
            print(f"{message['type']} worker isn't initialized")
            logger.info(29)
            await websocket.send(json.dumps(message))
            aspAdliVarLog(websocket, 17)

    async def handle_response(message):
        logger.info(30)
        aspAdliVarLog(message, 21)
        logger.info(31)
        '\n        Handle response from worker and pass to client.\n    '
        logger.info(32)
        global client, workers
        logger.info(33)
        if client:
            logger.info(34)
            await send_to_client(client, message)
        else:
            logger.info(35)
            message['response'] = "Client isn't initialized"
            aspAdliVarLog(message['response'], 20)
            logger.info(36)
            print(f"client isn't initialized")
            logger.info(37)
            await send_to_client(client, message)

    async def handle_message(websocket, message):
        logger.info(38)
        aspAdliVarLog(websocket, 24)
        aspAdliVarLog(message, 25)
        logger.info(39)
        '\n        Handle message received by client.\n    '
        logger.info(40)
        message = json.loads(message)
        aspAdliVarLog(message, 22)
        logger.info(41)
        asp_uid = message['asp_uid']
        aspAdliVarLog(asp_uid, 23)
        logger.info(42)
        print(f'\nReceived message: {message}')
        logger.info(43)
        if message['code'] == MSG_TYPE['REGISTER']:
            logger.info(44)
            await handle_register(websocket, message)
        else:
            logger.info(45)
            if message['code'] == MSG_TYPE['REQUEST']:
                logger.info(46)
                await handle_request(websocket, message)
            else:
                logger.info(47)
                if message['code'] == MSG_TYPE['RESPONSE']:
                    logger.info(48)
                    await handle_response(message)

    async def receieve_message(websocket):
        logger.info(49)
        aspAdliVarLog(websocket, 27)
        logger.info(50)
        '\n        Handles messages from websocket.\n\n        1. Workers register using \n        {\n            "code": 1,\n            "type": "bubbleSort"\n            "worker": True\n        }\n\n        2. Client Registers using\n        {\n            "code": 1,\n            "client": True\n        }\n\n        3. Client runs job using\n        {\n            "code": 2,\n            "client": True,\n            "type": "bubbleSort",\n            "data": [13,6,3,12,3]\n        }\n    '
        logger.info(51)
        async for message in websocket:
            aspAdliVarLog(message, 26)
            logger.info(52)
            await handle_message(websocket=websocket, message=message)
            logger.info(51)

    async def main():
        logger.info(53)
        logger.info(54)
        '\n        Creates a websocket at the provided port and initializes\n        the query handler. \n    '
        logger.info(55)
        parser = argparse.ArgumentParser(description='WebSocket server for sample system queries')
        aspAdliVarLog(parser, 28)
        logger.info(56)
        parser.add_argument('--host', default='localhost', help='Host to bind the server to')
        aspAdliVarLog(parser, 29)
        logger.info(57)
        parser.add_argument('--port', type=int, default=8765, help='Port to bind the server to')
        aspAdliVarLog(parser, 30)
        logger.info(58)
        args = parser.parse_args()
        aspAdliVarLog(args, 31)
        aspAdliVarLog(parser, 32)
        logger.info(59)
        print(f'Starting WebSocket server on {args.host}:{args.port}')
        logger.info(60)
        async with serve(receieve_message, args.host, args.port) as server:
            aspAdliVarLog(server, 33)
            logger.info(61)
            await server.serve_forever()
    logger.info(62)
    if __name__ == '__main__':
        logger.info(63)
        asyncio.run(main())
except Exception as e:
    logger.error(f'? {traceback.format_exc()}')
    raise