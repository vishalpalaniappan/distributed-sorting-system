import traceback
import logging
import json
import sys
from pathlib import Path
from clp_logging.handlers import CLPFileHandler
clp_handler = CLPFileHandler(Path('./bubbleSortWorker.clp.zst'))
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
logger.info('{"fileTree": {"bubbleSortWorker.py": {"source": "\\nimport websockets\\nimport asyncio\\nimport json\\nfrom bubbleSort import bubble_sort\\nimport uuid\\n\\nconnection = websockets.connect(uri=\'ws://localhost:8765\', ping_interval=None)\\n\\nMSG_TYPE = {\\n    \\"REGISTER\\": 1,\\n    \\"REQUEST\\": 2,\\n    \\"RESPONSE\\": 3\\n}\\n\\nIS_REGISTERED = False\\n\\n\\nasync def send_response(websocket, response):\\n    \'\'\'\\n        Send response to job handler.\\n    \'\'\'\\n    await websocket.send(json.dumps(response))\\n\\nasync def handle_request(message):\\n    \'\'\'\\n        Handle request from job handler.\\n    \'\'\'\\n    # Print task info\\n    print(f\\"\\\\nTask: {message[\'type\']}\\")\\n    print(f\\"UID: {message[\'asp_uid\']}\\")\\n    print(f\\"Val: {message[\'data\']}\\")\\n    print(f\\"User: {message[\'user\']}\\")\\n\\n    # Execute Task\\n    sortedList = bubble_sort(message[\\"data\\"])\\n    resp = {\\n        \\"code\\": MSG_TYPE[\\"RESPONSE\\"],\\n        \\"worker\\": True,\\n        \\"type\\": \\"bubbleSort\\",\\n        \\"value\\": sortedList,\\n        \\"asp_uid\\": message[\\"asp_uid\\"],\\n        \\"user\\": message[\\"user\\"]\\n    }\\n    return resp\\n\\nasync def handle_message(websocket, message):\\n    \'\'\'\\n        Handle the received message.\\n    \'\'\'\\n    message = json.loads(message)\\n    asp_uid = message[\\"asp_uid\\"]\\n\\n    if message[\\"code\\"] == MSG_TYPE[\\"REQUEST\\"]:\\n        response = await handle_request(message=message)\\n        await send_response(websocket=websocket, response=response)\\n\\n\\nasync def register(websocket):\\n    \'\'\'\\n        Register the worker with the job handler.\\n    \'\'\'\\n    asp_uid = str(uuid.uuid4())\\n\\n    # Send message to register the worker.\\n    await websocket.send(json.dumps({\\n        \\"code\\": MSG_TYPE[\\"REGISTER\\"],\\n        \\"worker\\": True,\\n        \\"type\\": \\"bubbleSort\\",\\n        \\"asp_uid\\": asp_uid\\n    }))\\n\\nasync def receieve_message():\\n    \'\'\'\\n        Main loop receives jobs, executes them and responds.\\n    \'\'\'\\n    async with connection as websocket:\\n        await register(websocket=websocket)\\n            \\n        try:\\n            # Listen for messages\\n            async for message in websocket:\\n                await handle_message(websocket=websocket, message=message)\\n        except KeyboardInterrupt:\\n            await websocket.close()\\n            return\\n\\n        await websocket.close()\\n\\nif __name__ == \\"__main__\\":\\n    asyncio.run(receieve_message())", "minLt": 0, "maxLt": 44}, "bubbleSort.py": {"source": "def bubble_sort(arr):\\n    # Taken from here: https://www.geeksforgeeks.org/python-program-for-bubble-sort/\\n    \\n    # Outer loop to iterate through the list n times\\n    for n in range(len(arr) - 1, 0, -1):\\n        swapped = False  \\n        for i in range(n):\\n            if arr[i] > arr[i + 1]:\\n\\n                # Swap elements if they are in the wrong order\\n                arr[i], arr[i + 1] = arr[i + 1], arr[i]\\n                swapped = True\\n        \\n        if not swapped:\\n            break\\n\\n    return arr\\n    ", "minLt": 44, "maxLt": 54}}, "ltMap": {"1": {"id": 1, "funcid": 0, "lineno": 2, "end_lineno": 2, "type": "child"}, "2": {"id": 2, "funcid": 0, "lineno": 3, "end_lineno": 3, "type": "child"}, "3": {"id": 3, "funcid": 0, "lineno": 4, "end_lineno": 4, "type": "child"}, "4": {"id": 4, "funcid": 0, "lineno": 5, "end_lineno": 5, "type": "child"}, "5": {"id": 5, "funcid": 0, "lineno": 6, "end_lineno": 6, "type": "child"}, "6": {"id": 6, "funcid": 0, "lineno": 8, "end_lineno": 8, "type": "child"}, "7": {"id": 7, "funcid": 0, "lineno": 10, "end_lineno": 14, "type": "child"}, "8": {"id": 8, "funcid": 0, "lineno": 16, "end_lineno": 16, "type": "child"}, "9": {"id": 9, "funcid": 9, "lineno": 19, "end_lineno": 23, "type": "function", "name": "send_response"}, "10": {"id": 10, "funcid": 9, "lineno": 20, "end_lineno": 22, "type": "child"}, "11": {"id": 11, "funcid": 9, "lineno": 23, "end_lineno": 23, "type": "child"}, "12": {"id": 12, "funcid": 12, "lineno": 25, "end_lineno": 45, "type": "function", "name": "handle_request"}, "13": {"id": 13, "funcid": 12, "lineno": 26, "end_lineno": 28, "type": "child"}, "14": {"id": 14, "funcid": 12, "lineno": 30, "end_lineno": 30, "type": "child"}, "15": {"id": 15, "funcid": 12, "lineno": 31, "end_lineno": 31, "type": "child"}, "16": {"id": 16, "funcid": 12, "lineno": 32, "end_lineno": 32, "type": "child"}, "17": {"id": 17, "funcid": 12, "lineno": 33, "end_lineno": 33, "type": "child"}, "18": {"id": 18, "funcid": 12, "lineno": 36, "end_lineno": 36, "type": "child"}, "19": {"id": 19, "funcid": 12, "lineno": 37, "end_lineno": 44, "type": "child"}, "20": {"id": 20, "funcid": 12, "lineno": 45, "end_lineno": 45, "type": "child"}, "21": {"id": 21, "funcid": 21, "lineno": 47, "end_lineno": 56, "type": "function", "name": "handle_message"}, "22": {"id": 22, "funcid": 21, "lineno": 48, "end_lineno": 50, "type": "child"}, "23": {"id": 23, "funcid": 21, "lineno": 51, "end_lineno": 51, "type": "child"}, "24": {"id": 24, "funcid": 21, "lineno": 52, "end_lineno": 52, "type": "child"}, "25": {"id": 25, "funcid": 21, "lineno": 54, "end_lineno": 56, "type": "child"}, "26": {"id": 26, "funcid": 21, "lineno": 55, "end_lineno": 55, "type": "child"}, "27": {"id": 27, "funcid": 21, "lineno": 56, "end_lineno": 56, "type": "child"}, "28": {"id": 28, "funcid": 28, "lineno": 59, "end_lineno": 71, "type": "function", "name": "register"}, "29": {"id": 29, "funcid": 28, "lineno": 60, "end_lineno": 62, "type": "child"}, "30": {"id": 30, "funcid": 28, "lineno": 63, "end_lineno": 63, "type": "child"}, "31": {"id": 31, "funcid": 28, "lineno": 66, "end_lineno": 71, "type": "child"}, "32": {"id": 32, "funcid": 32, "lineno": 73, "end_lineno": 88, "type": "function", "name": "receieve_message"}, "33": {"id": 33, "funcid": 32, "lineno": 74, "end_lineno": 76, "type": "child"}, "34": {"id": 34, "funcid": 32, "lineno": 77, "end_lineno": 88, "type": "child"}, "35": {"id": 35, "funcid": 32, "lineno": 78, "end_lineno": 78, "type": "child"}, "36": {"id": 36, "funcid": 32, "lineno": 80, "end_lineno": 86, "type": "child"}, "37": {"id": 37, "funcid": 32, "lineno": 82, "end_lineno": 83, "type": "child"}, "38": {"id": 38, "funcid": 32, "lineno": 83, "end_lineno": 83, "type": "child"}, "39": {"id": 39, "funcid": 32, "lineno": 84, "end_lineno": 86, "type": "child"}, "40": {"id": 40, "funcid": 32, "lineno": 85, "end_lineno": 85, "type": "child"}, "41": {"id": 41, "funcid": 32, "lineno": 86, "end_lineno": 86, "type": "child"}, "42": {"id": 42, "funcid": 32, "lineno": 88, "end_lineno": 88, "type": "child"}, "43": {"id": 43, "funcid": 0, "lineno": 90, "end_lineno": 91, "type": "child"}, "44": {"id": 44, "funcid": 0, "lineno": 91, "end_lineno": 91, "type": "child"}, "45": {"id": 45, "funcid": 45, "lineno": 1, "end_lineno": 17, "type": "function", "name": "bubble_sort"}, "46": {"id": 46, "funcid": 45, "lineno": 5, "end_lineno": 15, "type": "child"}, "47": {"id": 47, "funcid": 45, "lineno": 6, "end_lineno": 6, "type": "child"}, "48": {"id": 48, "funcid": 45, "lineno": 7, "end_lineno": 12, "type": "child"}, "49": {"id": 49, "funcid": 45, "lineno": 8, "end_lineno": 12, "type": "child"}, "50": {"id": 50, "funcid": 45, "lineno": 11, "end_lineno": 11, "type": "child"}, "51": {"id": 51, "funcid": 45, "lineno": 12, "end_lineno": 12, "type": "child"}, "52": {"id": 52, "funcid": 45, "lineno": 14, "end_lineno": 15, "type": "child"}, "53": {"id": 53, "funcid": 45, "lineno": 15, "end_lineno": 15, "type": "child"}, "54": {"id": 54, "funcid": 45, "lineno": 17, "end_lineno": 17, "type": "child"}}, "varMap": {"1": {"varId": 1, "name": "connection", "keys": [], "logType": 6, "funcId": 0, "isTemp": false, "global": true}, "2": {"varId": 2, "name": "MSG_TYPE", "keys": [], "logType": 7, "funcId": 0, "isTemp": false, "global": true}, "3": {"varId": 3, "name": "IS_REGISTERED", "keys": [], "logType": 8, "funcId": 0, "isTemp": false, "global": true}, "4": {"varId": 4, "name": "websocket", "keys": [], "logType": 11, "funcId": 9, "isTemp": false, "global": false}, "5": {"varId": 5, "name": "response", "keys": [], "logType": 11, "funcId": 9, "isTemp": false, "global": false}, "6": {"varId": 6, "name": "sortedList", "keys": [], "logType": 18, "funcId": 12, "isTemp": false, "global": false}, "7": {"varId": 7, "name": "resp", "keys": [], "logType": 19, "funcId": 12, "isTemp": false, "global": false}, "8": {"varId": 8, "name": "message", "keys": [], "logType": 20, "funcId": 12, "isTemp": false, "global": false}, "9": {"varId": 9, "name": "message", "keys": [], "logType": 23, "funcId": 21, "isTemp": false, "global": false}, "10": {"varId": 10, "name": "asp_uid", "keys": [], "logType": 24, "funcId": 21, "isTemp": false, "global": false}, "11": {"varId": 11, "name": "response", "keys": [], "logType": 26, "funcId": 21, "isTemp": false, "global": false}, "12": {"varId": 12, "name": "websocket", "keys": [], "logType": 27, "funcId": 21, "isTemp": false, "global": false}, "13": {"varId": 13, "name": "message", "keys": [], "logType": 27, "funcId": 21, "isTemp": false, "global": false}, "14": {"varId": 14, "name": "asp_uid", "keys": [], "logType": 30, "funcId": 28, "isTemp": false, "global": false}, "15": {"varId": 15, "name": "websocket", "keys": [], "logType": 31, "funcId": 28, "isTemp": false, "global": false}, "16": {"varId": 16, "name": "websocket", "keys": [], "logType": 31, "funcId": 28, "isTemp": false, "global": false}, "17": {"varId": 17, "name": "message", "keys": [], "logType": 38, "funcId": 32, "isTemp": false, "global": false}, "18": {"varId": 18, "name": "websocket", "keys": [], "logType": 40, "funcId": 32, "isTemp": false, "global": false}, "19": {"varId": 19, "name": "websocket", "keys": [], "logType": 42, "funcId": 32, "isTemp": false, "global": false}, "20": {"varId": 20, "name": "websocket", "keys": [], "logType": 42, "funcId": 32, "isTemp": false, "global": false}, "21": {"varId": 21, "name": "swapped", "keys": [], "logType": 47, "funcId": 45, "isTemp": false, "global": false}, "22": {"varId": 22, "name": "asp_temp_var_9ba3b150099b11f0aaa963f0c00b7079", "keys": [], "logType": 50, "funcId": 45, "isTemp": true, "global": false}, "23": {"varId": 23, "name": "arr", "keys": [{"type": "variable", "value": "i"}, {"type": "variable", "value": "arr"}, {"type": "temp_variable", "value": "asp_temp_var_9ba3b150099b11f0aaa963f0c00b7079"}], "logType": 50, "funcId": 45, "isTemp": false, "global": false}, "24": {"varId": 24, "name": "swapped", "keys": [], "logType": 51, "funcId": 45, "isTemp": false, "global": false}, "25": {"varId": 25, "name": "i", "keys": [], "logType": 51, "funcId": 45, "isTemp": false, "global": false}, "26": {"varId": 26, "name": "n", "keys": [], "logType": 53, "funcId": 45, "isTemp": false, "global": false}, "27": {"varId": 27, "name": "arr", "keys": [], "logType": 54, "funcId": 45, "isTemp": false, "global": false}}}')
try:
    logger.info(1)
    import websockets
    logger.info(2)
    import asyncio
    logger.info(3)
    import json
    logger.info(4)
    from bubbleSort import bubble_sort
    logger.info(5)
    import uuid
    logger.info(6)
    connection = websockets.connect(uri='ws://localhost:8765', ping_interval=None)
    aspAdliVarLog(connection, 1)
    logger.info(7)
    MSG_TYPE = {'REGISTER': 1, 'REQUEST': 2, 'RESPONSE': 3}
    aspAdliVarLog(MSG_TYPE, 2)
    logger.info(8)
    IS_REGISTERED = False
    aspAdliVarLog(IS_REGISTERED, 3)

    async def send_response(websocket, response):
        logger.info(9)
        aspAdliVarLog(websocket, 4)
        aspAdliVarLog(response, 5)
        logger.info(10)
        '\n        Send response to job handler.\n    '
        logger.info(11)
        await websocket.send(json.dumps(response))

    async def handle_request(message):
        logger.info(12)
        aspAdliVarLog(message, 8)
        logger.info(13)
        '\n        Handle request from job handler.\n    '
        logger.info(14)
        print(f"\nTask: {message['type']}")
        logger.info(15)
        print(f"UID: {message['asp_uid']}")
        logger.info(16)
        print(f"Val: {message['data']}")
        logger.info(17)
        print(f"User: {message['user']}")
        logger.info(18)
        sortedList = bubble_sort(message['data'])
        aspAdliVarLog(sortedList, 6)
        logger.info(19)
        resp = {'code': MSG_TYPE['RESPONSE'], 'worker': True, 'type': 'bubbleSort', 'value': sortedList, 'asp_uid': message['asp_uid'], 'user': message['user']}
        aspAdliVarLog(resp, 7)
        logger.info(20)
        return resp

    async def handle_message(websocket, message):
        logger.info(21)
        aspAdliVarLog(websocket, 12)
        aspAdliVarLog(message, 13)
        logger.info(22)
        '\n        Handle the received message.\n    '
        logger.info(23)
        message = json.loads(message)
        aspAdliVarLog(message, 9)
        logger.info(24)
        asp_uid = message['asp_uid']
        aspAdliVarLog(asp_uid, 10)
        logger.info(25)
        if message['code'] == MSG_TYPE['REQUEST']:
            logger.info(26)
            response = await handle_request(message=message)
            aspAdliVarLog(response, 11)
            logger.info(27)
            await send_response(websocket=websocket, response=response)

    async def register(websocket):
        logger.info(28)
        aspAdliVarLog(websocket, 16)
        logger.info(29)
        '\n        Register the worker with the job handler.\n    '
        logger.info(30)
        asp_uid = str(uuid.uuid4())
        aspAdliVarLog(asp_uid, 14)
        logger.info(31)
        await websocket.send(json.dumps({'code': MSG_TYPE['REGISTER'], 'worker': True, 'type': 'bubbleSort', 'asp_uid': asp_uid}))
        aspAdliVarLog(websocket, 15)

    async def receieve_message():
        logger.info(32)
        logger.info(33)
        '\n        Main loop receives jobs, executes them and responds.\n    '
        logger.info(34)
        async with connection as websocket:
            aspAdliVarLog(websocket, 20)
            logger.info(35)
            await register(websocket=websocket)
            try:
                logger.info(36)
                logger.info(37)
                async for message in websocket:
                    aspAdliVarLog(message, 17)
                    logger.info(38)
                    await handle_message(websocket=websocket, message=message)
                    logger.info(37)
            except KeyboardInterrupt:
                logger.info(39)
                logger.info(40)
                await websocket.close()
                aspAdliVarLog(websocket, 18)
                logger.info(41)
                return
            logger.info(42)
            await websocket.close()
            aspAdliVarLog(websocket, 19)
    logger.info(43)
    if __name__ == '__main__':
        logger.info(44)
        asyncio.run(receieve_message())
except Exception as e:
    logger.error(f'? {traceback.format_exc()}')
    raise