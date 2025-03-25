import traceback
import logging
import json
import sys
from pathlib import Path
from clp_logging.handlers import CLPFileHandler
clp_handler = CLPFileHandler(Path('./mergeSortWorker.clp.zst'))
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
logger.info('{"fileTree": {"mergeSortWorker.py": {"source": "\\nimport websockets\\nimport asyncio\\nimport json\\nfrom mergeSort import mergeSort\\nimport uuid\\n\\nconnection = websockets.connect(uri=\'ws://localhost:8765\', ping_interval=None)\\n\\nMSG_TYPE = {\\n    \\"REGISTER\\": 1,\\n    \\"REQUEST\\": 2,\\n    \\"RESPONSE\\": 3\\n}\\n\\nIS_REGISTERED = False\\n\\nasync def send_response(websocket, response):\\n    \'\'\'\\n        Send response to job handler.\\n    \'\'\'\\n    await websocket.send(json.dumps(response))\\n\\nasync def handle_request(message):\\n    \'\'\'\\n        Handle request from job handler.\\n    \'\'\'\\n    # Print task info\\n    print(f\\"\\\\nTask: {message[\'type\']}\\")\\n    print(f\\"UID: {message[\'asp_uid\']}\\")\\n    print(f\\"Val: {message[\'data\']}\\")\\n    print(f\\"User: {message[\'user\']}\\")\\n\\n    # Execute Task   \\n    n = len(message[\\"data\\"])\\n    sortedList = mergeSort(message[\\"data\\"], 0, n - 1)\\n    resp = {\\n        \\"code\\": MSG_TYPE[\\"RESPONSE\\"],\\n        \\"worker\\": True,\\n        \\"type\\": \\"mergeSort\\",\\n        \\"value\\": sortedList,\\n        \\"asp_uid\\": message[\\"asp_uid\\"],\\n        \\"user\\": message[\\"user\\"]\\n    }\\n    return resp\\n\\nasync def handle_message(websocket, message):\\n    \'\'\'\\n        Handle the received message.\\n    \'\'\'\\n    message = json.loads(message)\\n    asp_uid = message[\\"asp_uid\\"]\\n\\n    if message[\\"code\\"] == MSG_TYPE[\\"REQUEST\\"]:\\n        response = await handle_request(message=message)\\n        await send_response(websocket=websocket, response=response)\\n\\n\\nasync def register(websocket):\\n    \'\'\'\\n        Register the worker with the job handler.\\n    \'\'\'\\n    asp_uid = str(uuid.uuid4())\\n\\n    # Send message to register the worker.\\n    await websocket.send(json.dumps({\\n        \\"code\\": MSG_TYPE[\\"REGISTER\\"],\\n        \\"worker\\": True,\\n        \\"type\\": \\"mergeSort\\",\\n        \\"asp_uid\\": asp_uid\\n    }))\\n\\nasync def receieve_message():\\n    \'\'\'\\n        Main loop receives jobs, executes them and responds.\\n    \'\'\'\\n    async with connection as websocket:\\n        await register(websocket=websocket)\\n            \\n        try:\\n            # Listen for messages\\n            async for message in websocket:\\n                await handle_message(websocket=websocket, message=message)\\n        except KeyboardInterrupt:\\n            await websocket.close()\\n            return\\n\\n        await websocket.close()\\n\\nif __name__ == \\"__main__\\":\\n    asyncio.run(receieve_message())", "minLt": 0, "maxLt": 45}, "mergeSort.py": {"source": "def merge(arr, l, m, r):\\n    \'\'\'\\n        Reference: https://www.geeksforgeeks.org/python-program-for-merge-sort/\\n    \'\'\'\\n    n1 = m - l + 1\\n    n2 = r - m\\n\\n    # create temp arrays\\n    L = [0] * (n1)\\n    R = [0] * (n2)\\n\\n    # Copy data to temp arrays L[] and R[]\\n    for i in range(0, n1):\\n        L[i] = arr[l + i]\\n\\n    for j in range(0, n2):\\n        R[j] = arr[m + 1 + j]\\n\\n    # Merge the temp arrays back into arr[l..r]\\n    i = 0     # Initial index of first subarray\\n    j = 0     # Initial index of second subarray\\n    k = l     # Initial index of merged subarray\\n\\n    while i < n1 and j < n2:\\n        if L[i] <= R[j]:\\n            arr[k] = L[i]\\n            i += 1\\n        else:\\n            arr[k] = R[j]\\n            j += 1\\n        k += 1\\n\\n    # Copy the remaining elements of L[], if there\\n    # are any\\n    while i < n1:\\n        arr[k] = L[i]\\n        i += 1\\n        k += 1\\n\\n    # Copy the remaining elements of R[], if there\\n    # are any\\n    while j < n2:\\n        arr[k] = R[j]\\n        j += 1\\n        k += 1\\n\\n# l is for left index and r is right index of the\\n# sub-array of arr to be sorted\\n\\n\\ndef mergeSort(arr, l, r):\\n    \'\'\'\\n        Reference: https://www.geeksforgeeks.org/python-program-for-merge-sort/\\n    \'\'\'\\n    if l < r:\\n\\n        # Same as (l+r)//2, but avoids overflow for\\n        # large l and h\\n        m = l+(r-l)//2\\n\\n        # Sort first and second halves\\n        mergeSort(arr, l, m)\\n        mergeSort(arr, m+1, r)\\n        merge(arr, l, m, r)\\n\\n    return arr", "minLt": 45, "maxLt": 81}}, "ltMap": {"1": {"id": 1, "funcid": 0, "lineno": 2, "end_lineno": 2, "type": "child"}, "2": {"id": 2, "funcid": 0, "lineno": 3, "end_lineno": 3, "type": "child"}, "3": {"id": 3, "funcid": 0, "lineno": 4, "end_lineno": 4, "type": "child"}, "4": {"id": 4, "funcid": 0, "lineno": 5, "end_lineno": 5, "type": "child"}, "5": {"id": 5, "funcid": 0, "lineno": 6, "end_lineno": 6, "type": "child"}, "6": {"id": 6, "funcid": 0, "lineno": 8, "end_lineno": 8, "type": "child"}, "7": {"id": 7, "funcid": 0, "lineno": 10, "end_lineno": 14, "type": "child"}, "8": {"id": 8, "funcid": 0, "lineno": 16, "end_lineno": 16, "type": "child"}, "9": {"id": 9, "funcid": 9, "lineno": 18, "end_lineno": 22, "type": "function", "name": "send_response"}, "10": {"id": 10, "funcid": 9, "lineno": 19, "end_lineno": 21, "type": "child"}, "11": {"id": 11, "funcid": 9, "lineno": 22, "end_lineno": 22, "type": "child"}, "12": {"id": 12, "funcid": 12, "lineno": 24, "end_lineno": 45, "type": "function", "name": "handle_request"}, "13": {"id": 13, "funcid": 12, "lineno": 25, "end_lineno": 27, "type": "child"}, "14": {"id": 14, "funcid": 12, "lineno": 29, "end_lineno": 29, "type": "child"}, "15": {"id": 15, "funcid": 12, "lineno": 30, "end_lineno": 30, "type": "child"}, "16": {"id": 16, "funcid": 12, "lineno": 31, "end_lineno": 31, "type": "child"}, "17": {"id": 17, "funcid": 12, "lineno": 32, "end_lineno": 32, "type": "child"}, "18": {"id": 18, "funcid": 12, "lineno": 35, "end_lineno": 35, "type": "child"}, "19": {"id": 19, "funcid": 12, "lineno": 36, "end_lineno": 36, "type": "child"}, "20": {"id": 20, "funcid": 12, "lineno": 37, "end_lineno": 44, "type": "child"}, "21": {"id": 21, "funcid": 12, "lineno": 45, "end_lineno": 45, "type": "child"}, "22": {"id": 22, "funcid": 22, "lineno": 47, "end_lineno": 56, "type": "function", "name": "handle_message"}, "23": {"id": 23, "funcid": 22, "lineno": 48, "end_lineno": 50, "type": "child"}, "24": {"id": 24, "funcid": 22, "lineno": 51, "end_lineno": 51, "type": "child"}, "25": {"id": 25, "funcid": 22, "lineno": 52, "end_lineno": 52, "type": "child"}, "26": {"id": 26, "funcid": 22, "lineno": 54, "end_lineno": 56, "type": "child"}, "27": {"id": 27, "funcid": 22, "lineno": 55, "end_lineno": 55, "type": "child"}, "28": {"id": 28, "funcid": 22, "lineno": 56, "end_lineno": 56, "type": "child"}, "29": {"id": 29, "funcid": 29, "lineno": 59, "end_lineno": 71, "type": "function", "name": "register"}, "30": {"id": 30, "funcid": 29, "lineno": 60, "end_lineno": 62, "type": "child"}, "31": {"id": 31, "funcid": 29, "lineno": 63, "end_lineno": 63, "type": "child"}, "32": {"id": 32, "funcid": 29, "lineno": 66, "end_lineno": 71, "type": "child"}, "33": {"id": 33, "funcid": 33, "lineno": 73, "end_lineno": 88, "type": "function", "name": "receieve_message"}, "34": {"id": 34, "funcid": 33, "lineno": 74, "end_lineno": 76, "type": "child"}, "35": {"id": 35, "funcid": 33, "lineno": 77, "end_lineno": 88, "type": "child"}, "36": {"id": 36, "funcid": 33, "lineno": 78, "end_lineno": 78, "type": "child"}, "37": {"id": 37, "funcid": 33, "lineno": 80, "end_lineno": 86, "type": "child"}, "38": {"id": 38, "funcid": 33, "lineno": 82, "end_lineno": 83, "type": "child"}, "39": {"id": 39, "funcid": 33, "lineno": 83, "end_lineno": 83, "type": "child"}, "40": {"id": 40, "funcid": 33, "lineno": 84, "end_lineno": 86, "type": "child"}, "41": {"id": 41, "funcid": 33, "lineno": 85, "end_lineno": 85, "type": "child"}, "42": {"id": 42, "funcid": 33, "lineno": 86, "end_lineno": 86, "type": "child"}, "43": {"id": 43, "funcid": 33, "lineno": 88, "end_lineno": 88, "type": "child"}, "44": {"id": 44, "funcid": 0, "lineno": 90, "end_lineno": 91, "type": "child"}, "45": {"id": 45, "funcid": 0, "lineno": 91, "end_lineno": 91, "type": "child"}, "46": {"id": 46, "funcid": 46, "lineno": 1, "end_lineno": 45, "type": "function", "name": "merge"}, "47": {"id": 47, "funcid": 46, "lineno": 2, "end_lineno": 4, "type": "child"}, "48": {"id": 48, "funcid": 46, "lineno": 5, "end_lineno": 5, "type": "child"}, "49": {"id": 49, "funcid": 46, "lineno": 6, "end_lineno": 6, "type": "child"}, "50": {"id": 50, "funcid": 46, "lineno": 9, "end_lineno": 9, "type": "child"}, "51": {"id": 51, "funcid": 46, "lineno": 10, "end_lineno": 10, "type": "child"}, "52": {"id": 52, "funcid": 46, "lineno": 13, "end_lineno": 14, "type": "child"}, "53": {"id": 53, "funcid": 46, "lineno": 14, "end_lineno": 14, "type": "child"}, "54": {"id": 54, "funcid": 46, "lineno": 16, "end_lineno": 17, "type": "child"}, "55": {"id": 55, "funcid": 46, "lineno": 17, "end_lineno": 17, "type": "child"}, "56": {"id": 56, "funcid": 46, "lineno": 20, "end_lineno": 20, "type": "child"}, "57": {"id": 57, "funcid": 46, "lineno": 21, "end_lineno": 21, "type": "child"}, "58": {"id": 58, "funcid": 46, "lineno": 22, "end_lineno": 22, "type": "child"}, "59": {"id": 59, "funcid": 46, "lineno": 24, "end_lineno": 31, "type": "child"}, "60": {"id": 60, "funcid": 46, "lineno": 25, "end_lineno": 30, "type": "child"}, "61": {"id": 61, "funcid": 46, "lineno": 26, "end_lineno": 26, "type": "child"}, "62": {"id": 62, "funcid": 46, "lineno": 27, "end_lineno": 27, "type": "child"}, "63": {"id": 63, "funcid": 46, "lineno": 29, "end_lineno": 29, "type": "child"}, "64": {"id": 64, "funcid": 46, "lineno": 30, "end_lineno": 30, "type": "child"}, "65": {"id": 65, "funcid": 46, "lineno": 31, "end_lineno": 31, "type": "child"}, "66": {"id": 66, "funcid": 46, "lineno": 35, "end_lineno": 38, "type": "child"}, "67": {"id": 67, "funcid": 46, "lineno": 36, "end_lineno": 36, "type": "child"}, "68": {"id": 68, "funcid": 46, "lineno": 37, "end_lineno": 37, "type": "child"}, "69": {"id": 69, "funcid": 46, "lineno": 38, "end_lineno": 38, "type": "child"}, "70": {"id": 70, "funcid": 46, "lineno": 42, "end_lineno": 45, "type": "child"}, "71": {"id": 71, "funcid": 46, "lineno": 43, "end_lineno": 43, "type": "child"}, "72": {"id": 72, "funcid": 46, "lineno": 44, "end_lineno": 44, "type": "child"}, "73": {"id": 73, "funcid": 46, "lineno": 45, "end_lineno": 45, "type": "child"}, "74": {"id": 74, "funcid": 74, "lineno": 51, "end_lineno": 66, "type": "function", "name": "mergeSort"}, "75": {"id": 75, "funcid": 74, "lineno": 52, "end_lineno": 54, "type": "child"}, "76": {"id": 76, "funcid": 74, "lineno": 55, "end_lineno": 64, "type": "child"}, "77": {"id": 77, "funcid": 74, "lineno": 59, "end_lineno": 59, "type": "child"}, "78": {"id": 78, "funcid": 74, "lineno": 62, "end_lineno": 62, "type": "child"}, "79": {"id": 79, "funcid": 74, "lineno": 63, "end_lineno": 63, "type": "child"}, "80": {"id": 80, "funcid": 74, "lineno": 64, "end_lineno": 64, "type": "child"}, "81": {"id": 81, "funcid": 74, "lineno": 66, "end_lineno": 66, "type": "child"}}, "varMap": {"1": {"varId": 1, "name": "connection", "keys": [], "logType": 6, "funcId": 0, "isTemp": false, "global": true}, "2": {"varId": 2, "name": "MSG_TYPE", "keys": [], "logType": 7, "funcId": 0, "isTemp": false, "global": true}, "3": {"varId": 3, "name": "IS_REGISTERED", "keys": [], "logType": 8, "funcId": 0, "isTemp": false, "global": true}, "4": {"varId": 4, "name": "websocket", "keys": [], "logType": 11, "funcId": 9, "isTemp": false, "global": false}, "5": {"varId": 5, "name": "response", "keys": [], "logType": 11, "funcId": 9, "isTemp": false, "global": false}, "6": {"varId": 6, "name": "n", "keys": [], "logType": 18, "funcId": 12, "isTemp": false, "global": false}, "7": {"varId": 7, "name": "sortedList", "keys": [], "logType": 19, "funcId": 12, "isTemp": false, "global": false}, "8": {"varId": 8, "name": "resp", "keys": [], "logType": 20, "funcId": 12, "isTemp": false, "global": false}, "9": {"varId": 9, "name": "message", "keys": [], "logType": 21, "funcId": 12, "isTemp": false, "global": false}, "10": {"varId": 10, "name": "message", "keys": [], "logType": 24, "funcId": 22, "isTemp": false, "global": false}, "11": {"varId": 11, "name": "asp_uid", "keys": [], "logType": 25, "funcId": 22, "isTemp": false, "global": false}, "12": {"varId": 12, "name": "response", "keys": [], "logType": 27, "funcId": 22, "isTemp": false, "global": false}, "13": {"varId": 13, "name": "websocket", "keys": [], "logType": 28, "funcId": 22, "isTemp": false, "global": false}, "14": {"varId": 14, "name": "message", "keys": [], "logType": 28, "funcId": 22, "isTemp": false, "global": false}, "15": {"varId": 15, "name": "asp_uid", "keys": [], "logType": 31, "funcId": 29, "isTemp": false, "global": false}, "16": {"varId": 16, "name": "websocket", "keys": [], "logType": 32, "funcId": 29, "isTemp": false, "global": false}, "17": {"varId": 17, "name": "websocket", "keys": [], "logType": 32, "funcId": 29, "isTemp": false, "global": false}, "18": {"varId": 18, "name": "message", "keys": [], "logType": 39, "funcId": 33, "isTemp": false, "global": false}, "19": {"varId": 19, "name": "websocket", "keys": [], "logType": 41, "funcId": 33, "isTemp": false, "global": false}, "20": {"varId": 20, "name": "websocket", "keys": [], "logType": 43, "funcId": 33, "isTemp": false, "global": false}, "21": {"varId": 21, "name": "websocket", "keys": [], "logType": 43, "funcId": 33, "isTemp": false, "global": false}, "22": {"varId": 22, "name": "n1", "keys": [], "logType": 48, "funcId": 46, "isTemp": false, "global": false}, "23": {"varId": 23, "name": "n2", "keys": [], "logType": 49, "funcId": 46, "isTemp": false, "global": false}, "24": {"varId": 24, "name": "L", "keys": [], "logType": 50, "funcId": 46, "isTemp": false, "global": false}, "25": {"varId": 25, "name": "R", "keys": [], "logType": 51, "funcId": 46, "isTemp": false, "global": false}, "26": {"varId": 26, "name": "L", "keys": [{"type": "variable", "value": "i"}], "logType": 53, "funcId": 46, "isTemp": false, "global": false}, "27": {"varId": 27, "name": "i", "keys": [], "logType": 53, "funcId": 46, "isTemp": false, "global": false}, "28": {"varId": 28, "name": "R", "keys": [{"type": "variable", "value": "j"}], "logType": 55, "funcId": 46, "isTemp": false, "global": false}, "29": {"varId": 29, "name": "j", "keys": [], "logType": 55, "funcId": 46, "isTemp": false, "global": false}, "30": {"varId": 30, "name": "i", "keys": [], "logType": 56, "funcId": 46, "isTemp": false, "global": false}, "31": {"varId": 31, "name": "j", "keys": [], "logType": 57, "funcId": 46, "isTemp": false, "global": false}, "32": {"varId": 32, "name": "k", "keys": [], "logType": 58, "funcId": 46, "isTemp": false, "global": false}, "33": {"varId": 33, "name": "arr", "keys": [{"type": "variable", "value": "k"}], "logType": 61, "funcId": 46, "isTemp": false, "global": false}, "34": {"varId": 34, "name": "i", "keys": [], "logType": 62, "funcId": 46, "isTemp": false, "global": false}, "35": {"varId": 35, "name": "arr", "keys": [{"type": "variable", "value": "k"}], "logType": 63, "funcId": 46, "isTemp": false, "global": false}, "36": {"varId": 36, "name": "j", "keys": [], "logType": 64, "funcId": 46, "isTemp": false, "global": false}, "37": {"varId": 37, "name": "k", "keys": [], "logType": 65, "funcId": 46, "isTemp": false, "global": false}, "38": {"varId": 38, "name": "arr", "keys": [{"type": "variable", "value": "k"}], "logType": 67, "funcId": 46, "isTemp": false, "global": false}, "39": {"varId": 39, "name": "i", "keys": [], "logType": 68, "funcId": 46, "isTemp": false, "global": false}, "40": {"varId": 40, "name": "k", "keys": [], "logType": 69, "funcId": 46, "isTemp": false, "global": false}, "41": {"varId": 41, "name": "arr", "keys": [{"type": "variable", "value": "k"}], "logType": 71, "funcId": 46, "isTemp": false, "global": false}, "42": {"varId": 42, "name": "j", "keys": [], "logType": 72, "funcId": 46, "isTemp": false, "global": false}, "43": {"varId": 43, "name": "k", "keys": [], "logType": 73, "funcId": 46, "isTemp": false, "global": false}, "44": {"varId": 44, "name": "arr", "keys": [], "logType": 73, "funcId": 46, "isTemp": false, "global": false}, "45": {"varId": 45, "name": "l", "keys": [], "logType": 73, "funcId": 46, "isTemp": false, "global": false}, "46": {"varId": 46, "name": "m", "keys": [], "logType": 73, "funcId": 46, "isTemp": false, "global": false}, "47": {"varId": 47, "name": "r", "keys": [], "logType": 73, "funcId": 46, "isTemp": false, "global": false}, "48": {"varId": 48, "name": "m", "keys": [], "logType": 77, "funcId": 74, "isTemp": false, "global": false}, "49": {"varId": 49, "name": "arr", "keys": [], "logType": 81, "funcId": 74, "isTemp": false, "global": false}, "50": {"varId": 50, "name": "l", "keys": [], "logType": 81, "funcId": 74, "isTemp": false, "global": false}, "51": {"varId": 51, "name": "r", "keys": [], "logType": 81, "funcId": 74, "isTemp": false, "global": false}}}')
try:
    logger.info(1)
    import websockets
    logger.info(2)
    import asyncio
    logger.info(3)
    import json
    logger.info(4)
    from mergeSort import mergeSort
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
        aspAdliVarLog(message, 9)
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
        n = len(message['data'])
        aspAdliVarLog(n, 6)
        logger.info(19)
        sortedList = mergeSort(message['data'], 0, n - 1)
        aspAdliVarLog(sortedList, 7)
        logger.info(20)
        resp = {'code': MSG_TYPE['RESPONSE'], 'worker': True, 'type': 'mergeSort', 'value': sortedList, 'asp_uid': message['asp_uid'], 'user': message['user']}
        aspAdliVarLog(resp, 8)
        logger.info(21)
        return resp

    async def handle_message(websocket, message):
        logger.info(22)
        aspAdliVarLog(websocket, 13)
        aspAdliVarLog(message, 14)
        logger.info(23)
        '\n        Handle the received message.\n    '
        logger.info(24)
        message = json.loads(message)
        aspAdliVarLog(message, 10)
        logger.info(25)
        asp_uid = message['asp_uid']
        aspAdliVarLog(asp_uid, 11)
        logger.info(26)
        if message['code'] == MSG_TYPE['REQUEST']:
            logger.info(27)
            response = await handle_request(message=message)
            aspAdliVarLog(response, 12)
            logger.info(28)
            await send_response(websocket=websocket, response=response)

    async def register(websocket):
        logger.info(29)
        aspAdliVarLog(websocket, 17)
        logger.info(30)
        '\n        Register the worker with the job handler.\n    '
        logger.info(31)
        asp_uid = str(uuid.uuid4())
        aspAdliVarLog(asp_uid, 15)
        logger.info(32)
        await websocket.send(json.dumps({'code': MSG_TYPE['REGISTER'], 'worker': True, 'type': 'mergeSort', 'asp_uid': asp_uid}))
        aspAdliVarLog(websocket, 16)

    async def receieve_message():
        logger.info(33)
        logger.info(34)
        '\n        Main loop receives jobs, executes them and responds.\n    '
        logger.info(35)
        async with connection as websocket:
            aspAdliVarLog(websocket, 21)
            logger.info(36)
            await register(websocket=websocket)
            try:
                logger.info(37)
                logger.info(38)
                async for message in websocket:
                    aspAdliVarLog(message, 18)
                    logger.info(39)
                    await handle_message(websocket=websocket, message=message)
                    logger.info(38)
            except KeyboardInterrupt:
                logger.info(40)
                logger.info(41)
                await websocket.close()
                aspAdliVarLog(websocket, 19)
                logger.info(42)
                return
            logger.info(43)
            await websocket.close()
            aspAdliVarLog(websocket, 20)
    logger.info(44)
    if __name__ == '__main__':
        logger.info(45)
        asyncio.run(receieve_message())
except Exception as e:
    logger.error(f'? {traceback.format_exc()}')
    raise