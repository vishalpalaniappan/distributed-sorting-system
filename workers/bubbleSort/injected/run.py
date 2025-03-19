import traceback
import logging
import json
import sys
from pathlib import Path
from clp_logging.handlers import CLPFileHandler
clp_handler = CLPFileHandler(Path('./run.clp.zst'))
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
logger.info('{"fileTree": {"run.py": {"source": "\\nimport websockets\\nimport asyncio\\nimport json\\nfrom bubbleSort import bubble_sort\\nimport uuid\\n\\nconnection = websockets.connect(uri=\'ws://localhost:8765\', ping_interval=None)\\n\\nMSG_TYPE = {\\n    \\"REGISTER\\": 1,\\n    \\"REQUEST\\": 2,\\n    \\"RESPONSE\\": 3\\n}\\n\\nIS_REGISTERED = False\\n\\n\\nasync def send_response(websocket, response):\\n    await websocket.send(json.dumps(response))\\n\\nasync def handle_request(message):\\n    # Receieve Task\\n    print(f\\"\\\\nTask: {message[\'type\']}\\")\\n    print(f\\"UID: {message[\'asp_uid\']}\\")\\n    print(f\\"Val: {message[\'data\']}\\")\\n\\n    # Execute Task\\n    sortedList = bubble_sort(message[\\"data\\"])\\n    resp = {\\n        \\"code\\": MSG_TYPE[\\"RESPONSE\\"],\\n        \\"worker\\": True,\\n        \\"type\\": \\"bubbleSort\\",\\n        \\"value\\": sortedList,\\n        \\"asp_uid\\": message[\\"asp_uid\\"]\\n    }\\n    return resp\\n\\nasync def handle_message(websocket, message):\\n\\n    if message[\\"code\\"] == MSG_TYPE[\\"REQUEST\\"]:\\n        response = await handle_request(message=message)\\n        await send_response(websocket=websocket, response=response)\\n\\n\\nasync def receieve_message():\\n    \'\'\'\\n        Main loop receives jobs, executes them and responds.\\n    \'\'\'\\n    async with connection as websocket:\\n        asp_uid = str(uuid.uuid4())\\n\\n        # Send message to register the worker.\\n        await websocket.send(json.dumps({\\n            \\"code\\": MSG_TYPE[\\"REGISTER\\"],\\n            \\"worker\\": True,\\n            \\"type\\": \\"bubbleSort\\",\\n            \\"asp_uid\\": asp_uid\\n        }))\\n            \\n        # Listen for messages\\n        async for message in websocket:\\n            message = json.loads(message)\\n            asp_uid = message[\\"asp_uid\\"]\\n            \'\'\'adli-trace-id-start message[\\"asp_uid\\"]\'\'\'\\n            await handle_message(websocket=websocket, message=message)\\n            \'\'\'adli-trace-id-end message[\\"asp_uid\\"]\'\'\'\\n\\n        await websocket.close()\\n\\nif __name__ == \\"__main__\\":\\n    asyncio.run(receieve_message())", "minLt": 0, "maxLt": 33}, "bubbleSort.py": {"source": "def bubble_sort(arr):\\n    # Taken from here: https://www.geeksforgeeks.org/python-program-for-bubble-sort/\\n    \\n    # Outer loop to iterate through the list n times\\n    for n in range(len(arr) - 1, 0, -1):\\n        swapped = False  \\n        for i in range(n):\\n            if arr[i] > arr[i + 1]:\\n\\n                # Swap elements if they are in the wrong order\\n                arr[i], arr[i + 1] = arr[i + 1], arr[i]\\n                swapped = True\\n        \\n        if not swapped:\\n            break\\n\\n    return arr\\n    ", "minLt": 33, "maxLt": 43}}, "ltMap": {"1": {"id": 1, "funcid": 0, "lineno": 2, "end_lineno": 2, "type": "child"}, "2": {"id": 2, "funcid": 0, "lineno": 3, "end_lineno": 3, "type": "child"}, "3": {"id": 3, "funcid": 0, "lineno": 4, "end_lineno": 4, "type": "child"}, "4": {"id": 4, "funcid": 0, "lineno": 5, "end_lineno": 5, "type": "child"}, "5": {"id": 5, "funcid": 0, "lineno": 6, "end_lineno": 6, "type": "child"}, "6": {"id": 6, "funcid": 0, "lineno": 8, "end_lineno": 8, "type": "child"}, "7": {"id": 7, "funcid": 0, "lineno": 10, "end_lineno": 14, "type": "child"}, "8": {"id": 8, "funcid": 0, "lineno": 16, "end_lineno": 16, "type": "child"}, "9": {"id": 9, "funcid": 9, "lineno": 19, "end_lineno": 20, "type": "function", "name": "send_response"}, "10": {"id": 10, "funcid": 9, "lineno": 20, "end_lineno": 20, "type": "child"}, "11": {"id": 11, "funcid": 11, "lineno": 22, "end_lineno": 37, "type": "function", "name": "handle_request"}, "12": {"id": 12, "funcid": 11, "lineno": 24, "end_lineno": 24, "type": "child"}, "13": {"id": 13, "funcid": 11, "lineno": 25, "end_lineno": 25, "type": "child"}, "14": {"id": 14, "funcid": 11, "lineno": 26, "end_lineno": 26, "type": "child"}, "15": {"id": 15, "funcid": 11, "lineno": 29, "end_lineno": 29, "type": "child"}, "16": {"id": 16, "funcid": 11, "lineno": 30, "end_lineno": 36, "type": "child"}, "17": {"id": 17, "funcid": 11, "lineno": 37, "end_lineno": 37, "type": "child"}, "18": {"id": 18, "funcid": 18, "lineno": 39, "end_lineno": 43, "type": "function", "name": "handle_message"}, "19": {"id": 19, "funcid": 18, "lineno": 41, "end_lineno": 43, "type": "child"}, "20": {"id": 20, "funcid": 18, "lineno": 42, "end_lineno": 42, "type": "child"}, "21": {"id": 21, "funcid": 18, "lineno": 43, "end_lineno": 43, "type": "child"}, "22": {"id": 22, "funcid": 22, "lineno": 46, "end_lineno": 69, "type": "function", "name": "receieve_message"}, "23": {"id": 23, "funcid": 22, "lineno": 47, "end_lineno": 49, "type": "child"}, "24": {"id": 24, "funcid": 22, "lineno": 50, "end_lineno": 69, "type": "child"}, "25": {"id": 25, "funcid": 22, "lineno": 51, "end_lineno": 51, "type": "child"}, "26": {"id": 26, "funcid": 22, "lineno": 54, "end_lineno": 59, "type": "child"}, "27": {"id": 27, "funcid": 22, "lineno": 62, "end_lineno": 67, "type": "child"}, "28": {"id": 28, "funcid": 22, "lineno": 63, "end_lineno": 63, "type": "child"}, "29": {"id": 29, "funcid": 22, "lineno": 64, "end_lineno": 64, "type": "child"}, "30": {"id": 30, "funcid": 22, "lineno": 66, "end_lineno": 66, "type": "child"}, "31": {"id": 31, "funcid": 22, "lineno": 69, "end_lineno": 69, "type": "child"}, "32": {"id": 32, "funcid": 0, "lineno": 71, "end_lineno": 72, "type": "child"}, "33": {"id": 33, "funcid": 0, "lineno": 72, "end_lineno": 72, "type": "child"}, "34": {"id": 34, "funcid": 34, "lineno": 1, "end_lineno": 17, "type": "function", "name": "bubble_sort"}, "35": {"id": 35, "funcid": 34, "lineno": 5, "end_lineno": 15, "type": "child"}, "36": {"id": 36, "funcid": 34, "lineno": 6, "end_lineno": 6, "type": "child"}, "37": {"id": 37, "funcid": 34, "lineno": 7, "end_lineno": 12, "type": "child"}, "38": {"id": 38, "funcid": 34, "lineno": 8, "end_lineno": 12, "type": "child"}, "39": {"id": 39, "funcid": 34, "lineno": 11, "end_lineno": 11, "type": "child"}, "40": {"id": 40, "funcid": 34, "lineno": 12, "end_lineno": 12, "type": "child"}, "41": {"id": 41, "funcid": 34, "lineno": 14, "end_lineno": 15, "type": "child"}, "42": {"id": 42, "funcid": 34, "lineno": 15, "end_lineno": 15, "type": "child"}, "43": {"id": 43, "funcid": 34, "lineno": 17, "end_lineno": 17, "type": "child"}}, "varMap": {"1": {"varId": 1, "name": "connection", "keys": [], "logType": 6, "funcId": 0, "isTemp": false, "global": true}, "2": {"varId": 2, "name": "MSG_TYPE", "keys": [], "logType": 7, "funcId": 0, "isTemp": false, "global": true}, "3": {"varId": 3, "name": "IS_REGISTERED", "keys": [], "logType": 8, "funcId": 0, "isTemp": false, "global": true}, "4": {"varId": 4, "name": "websocket", "keys": [], "logType": 10, "funcId": 9, "isTemp": false, "global": false}, "5": {"varId": 5, "name": "response", "keys": [], "logType": 10, "funcId": 9, "isTemp": false, "global": false}, "6": {"varId": 6, "name": "sortedList", "keys": [], "logType": 15, "funcId": 11, "isTemp": false, "global": false}, "7": {"varId": 7, "name": "resp", "keys": [], "logType": 16, "funcId": 11, "isTemp": false, "global": false}, "8": {"varId": 8, "name": "message", "keys": [], "logType": 17, "funcId": 11, "isTemp": false, "global": false}, "9": {"varId": 9, "name": "response", "keys": [], "logType": 20, "funcId": 18, "isTemp": false, "global": false}, "10": {"varId": 10, "name": "websocket", "keys": [], "logType": 21, "funcId": 18, "isTemp": false, "global": false}, "11": {"varId": 11, "name": "message", "keys": [], "logType": 21, "funcId": 18, "isTemp": false, "global": false}, "12": {"varId": 12, "name": "asp_uid", "keys": [], "logType": 25, "funcId": 22, "isTemp": false, "global": false}, "13": {"varId": 13, "name": "websocket", "keys": [], "logType": 26, "funcId": 22, "isTemp": false, "global": false}, "14": {"varId": 14, "name": "message", "keys": [], "logType": 28, "funcId": 22, "isTemp": false, "global": false}, "15": {"varId": 15, "name": "asp_uid", "keys": [], "logType": 29, "funcId": 22, "isTemp": false, "global": false}, "16": {"varId": 16, "name": "message", "keys": [], "logType": 30, "funcId": 22, "isTemp": false, "global": false}, "17": {"varId": 17, "name": "websocket", "keys": [], "logType": 31, "funcId": 22, "isTemp": false, "global": false}, "18": {"varId": 18, "name": "websocket", "keys": [], "logType": 31, "funcId": 22, "isTemp": false, "global": false}, "19": {"varId": 19, "name": "swapped", "keys": [], "logType": 36, "funcId": 34, "isTemp": false, "global": false}, "20": {"varId": 20, "name": "asp_temp_var_bcdaf700046111f0b89d9f0ee9e28e0e", "keys": [], "logType": 39, "funcId": 34, "isTemp": true, "global": false}, "21": {"varId": 21, "name": "arr", "keys": [{"type": "variable", "value": "i"}, {"type": "variable", "value": "arr"}, {"type": "temp_variable", "value": "asp_temp_var_bcdaf700046111f0b89d9f0ee9e28e0e"}], "logType": 39, "funcId": 34, "isTemp": false, "global": false}, "22": {"varId": 22, "name": "swapped", "keys": [], "logType": 40, "funcId": 34, "isTemp": false, "global": false}, "23": {"varId": 23, "name": "i", "keys": [], "logType": 40, "funcId": 34, "isTemp": false, "global": false}, "24": {"varId": 24, "name": "n", "keys": [], "logType": 42, "funcId": 34, "isTemp": false, "global": false}, "25": {"varId": 25, "name": "arr", "keys": [], "logType": 43, "funcId": 34, "isTemp": false, "global": false}}}')
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
        await websocket.send(json.dumps(response))

    async def handle_request(message):
        logger.info(11)
        aspAdliVarLog(message, 8)
        logger.info(12)
        print(f"\nTask: {message['type']}")
        logger.info(13)
        print(f"UID: {message['asp_uid']}")
        logger.info(14)
        print(f"Val: {message['data']}")
        logger.info(15)
        sortedList = bubble_sort(message['data'])
        aspAdliVarLog(sortedList, 6)
        logger.info(16)
        resp = {'code': MSG_TYPE['RESPONSE'], 'worker': True, 'type': 'bubbleSort', 'value': sortedList, 'asp_uid': message['asp_uid']}
        aspAdliVarLog(resp, 7)
        logger.info(17)
        return resp

    async def handle_message(websocket, message):
        logger.info(18)
        aspAdliVarLog(websocket, 10)
        aspAdliVarLog(message, 11)
        logger.info(19)
        if message['code'] == MSG_TYPE['REQUEST']:
            logger.info(20)
            response = await handle_request(message=message)
            aspAdliVarLog(response, 9)
            logger.info(21)
            await send_response(websocket=websocket, response=response)

    async def receieve_message():
        logger.info(22)
        logger.info(23)
        '\n        Main loop receives jobs, executes them and responds.\n    '
        logger.info(24)
        async with connection as websocket:
            aspAdliVarLog(websocket, 18)
            logger.info(25)
            asp_uid = str(uuid.uuid4())
            aspAdliVarLog(asp_uid, 12)
            logger.info(26)
            await websocket.send(json.dumps({'code': MSG_TYPE['REGISTER'], 'worker': True, 'type': 'bubbleSort', 'asp_uid': asp_uid}))
            aspAdliVarLog(websocket, 13)
            logger.info(27)
            async for message in websocket:
                aspAdliVarLog(message, 16)
                logger.info(28)
                message = json.loads(message)
                aspAdliVarLog(message, 14)
                logger.info(29)
                asp_uid = message['asp_uid']
                aspAdliVarLog(asp_uid, 15)
                aspTraceLog('start', message["asp_uid"])
                logger.info(30)
                await handle_message(websocket=websocket, message=message)
                aspTraceLog('end', message["asp_uid"])
                logger.info(27)
            logger.info(31)
            await websocket.close()
            aspAdliVarLog(websocket, 17)
    logger.info(32)
    if __name__ == '__main__':
        logger.info(33)
        asyncio.run(receieve_message())
except Exception as e:
    logger.error(f'? {traceback.format_exc()}')
    raise