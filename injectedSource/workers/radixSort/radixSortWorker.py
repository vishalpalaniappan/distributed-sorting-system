import traceback
import logging
import json
import sys
from pathlib import Path
from clp_logging.handlers import CLPFileHandler
clp_handler = CLPFileHandler(Path('./radixSortWorker.clp.zst'))
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
logger.info('{"fileTree": {"radixSortWorker.py": {"source": "\\nimport websockets\\nimport asyncio\\nimport json\\nfrom radixSort import radixSort\\nimport uuid\\n\\nconnection = websockets.connect(uri=\'ws://localhost:8765\', ping_interval=None)\\n\\nMSG_TYPE = {\\n    \\"REGISTER\\": 1,\\n    \\"REQUEST\\": 2,\\n    \\"RESPONSE\\": 3\\n}\\n\\nIS_REGISTERED = False\\n\\n\\nasync def send_response(websocket, response):\\n    \'\'\'\\n        Send response to job handler.\\n    \'\'\'\\n    await websocket.send(json.dumps(response))\\n\\nasync def handle_request(message):\\n    \'\'\'\\n        Handle request from job handler.\\n    \'\'\'\\n    # Print task info\\n    print(f\\"\\\\nTask: {message[\'type\']}\\")\\n    print(f\\"UID: {message[\'asp_uid\']}\\")\\n    print(f\\"Val: {message[\'data\']}\\")\\n    print(f\\"User: {message[\'user\']}\\")\\n\\n    # Execute Task\\n    n = len(message[\\"data\\"])\\n    sortedList = radixSort(message[\\"data\\"])\\n    resp = {\\n        \\"code\\": MSG_TYPE[\\"RESPONSE\\"],\\n        \\"worker\\": True,\\n        \\"type\\": \\"radixSort\\",\\n        \\"value\\": sortedList,\\n        \\"asp_uid\\": message[\\"asp_uid\\"],\\n        \\"user\\": message[\\"user\\"]\\n    }\\n    return resp\\n\\nasync def handle_message(websocket, message):\\n    \'\'\'\\n        Handle the received message.\\n    \'\'\'\\n    message = json.loads(message)\\n    asp_uid = message[\\"asp_uid\\"]\\n\\n    if message[\\"code\\"] == MSG_TYPE[\\"REQUEST\\"]:\\n        response = await handle_request(message=message)\\n        await send_response(websocket=websocket, response=response)\\n\\nasync def register(websocket):\\n    \'\'\'\\n        Register the worker with the job handler.\\n    \'\'\'\\n    asp_uid = str(uuid.uuid4())\\n\\n    # Send message to register the worker.\\n    await websocket.send(json.dumps({\\n        \\"code\\": MSG_TYPE[\\"REGISTER\\"],\\n        \\"worker\\": True,\\n        \\"type\\": \\"radixSort\\",\\n        \\"asp_uid\\": asp_uid\\n    }))\\n\\n\\nasync def receieve_message():\\n    \'\'\'\\n        Main loop receives jobs, executes them and responds.\\n    \'\'\'\\n    async with connection as websocket:\\n        await register(websocket=websocket)\\n        # Listen for messages\\n        async for message in websocket:\\n            await handle_message(websocket=websocket, message=message)\\n\\n        await websocket.close()\\n\\nif __name__ == \\"__main__\\":\\n    asyncio.run(receieve_message())", "minLt": 0, "maxLt": 41}, "radixSort.py": {"source": "\\n\\ndef countingSort(arr, exp1): \\n    \'\'\'\\n        Reference: https://www.geeksforgeeks.org/python-program-for-radix-sort/\\n    \'\'\'\\n  \\n    n = len(arr) \\n  \\n    # The output array elements that will have sorted arr \\n    output = [0] * (n) \\n  \\n    # initialize count array as 0 \\n    count = [0] * (10) \\n  \\n    # Store count of occurrences in count[] \\n    for i in range(0, n): \\n        index = (arr[i]/exp1) \\n        count[int((index)%10)] += 1\\n  \\n    # Change count[i] so that count[i] now contains actual \\n    #  position of this digit in output array \\n    for i in range(1,10): \\n        count[i] += count[i-1] \\n  \\n    # Build the output array \\n    i = n-1\\n    while i>=0: \\n        index = (arr[i]/exp1) \\n        output[ count[ int((index)%10) ] - 1] = arr[i] \\n        count[int((index)%10)] -= 1\\n        i -= 1\\n  \\n    # Copying the output array to arr[], \\n    # so that arr now contains sorted numbers \\n    i = 0\\n    for i in range(0,len(arr)): \\n        arr[i] = output[i] \\n\\ndef radixSort(arr):\\n    \'\'\'\\n        Reference: https://www.geeksforgeeks.org/python-program-for-radix-sort/\\n    \'\'\'\\n\\n    # Find the maximum number to know number of digits\\n    max1 = max(arr)\\n\\n    # Do counting sort for every digit. Note that instead\\n    # of passing digit number, exp is passed. exp is 10^i\\n    # where i is current digit number\\n    exp = 1\\n    while max1 // exp > 0:\\n        countingSort(arr,exp)\\n        exp *= 10\\n\\n    return arr", "minLt": 41, "maxLt": 68}}, "ltMap": {"1": {"id": 1, "funcid": 0, "lineno": 2, "end_lineno": 2, "type": "child"}, "2": {"id": 2, "funcid": 0, "lineno": 3, "end_lineno": 3, "type": "child"}, "3": {"id": 3, "funcid": 0, "lineno": 4, "end_lineno": 4, "type": "child"}, "4": {"id": 4, "funcid": 0, "lineno": 5, "end_lineno": 5, "type": "child"}, "5": {"id": 5, "funcid": 0, "lineno": 6, "end_lineno": 6, "type": "child"}, "6": {"id": 6, "funcid": 0, "lineno": 8, "end_lineno": 8, "type": "child"}, "7": {"id": 7, "funcid": 0, "lineno": 10, "end_lineno": 14, "type": "child"}, "8": {"id": 8, "funcid": 0, "lineno": 16, "end_lineno": 16, "type": "child"}, "9": {"id": 9, "funcid": 9, "lineno": 19, "end_lineno": 23, "type": "function", "name": "send_response"}, "10": {"id": 10, "funcid": 9, "lineno": 20, "end_lineno": 22, "type": "child"}, "11": {"id": 11, "funcid": 9, "lineno": 23, "end_lineno": 23, "type": "child"}, "12": {"id": 12, "funcid": 12, "lineno": 25, "end_lineno": 46, "type": "function", "name": "handle_request"}, "13": {"id": 13, "funcid": 12, "lineno": 26, "end_lineno": 28, "type": "child"}, "14": {"id": 14, "funcid": 12, "lineno": 30, "end_lineno": 30, "type": "child"}, "15": {"id": 15, "funcid": 12, "lineno": 31, "end_lineno": 31, "type": "child"}, "16": {"id": 16, "funcid": 12, "lineno": 32, "end_lineno": 32, "type": "child"}, "17": {"id": 17, "funcid": 12, "lineno": 33, "end_lineno": 33, "type": "child"}, "18": {"id": 18, "funcid": 12, "lineno": 36, "end_lineno": 36, "type": "child"}, "19": {"id": 19, "funcid": 12, "lineno": 37, "end_lineno": 37, "type": "child"}, "20": {"id": 20, "funcid": 12, "lineno": 38, "end_lineno": 45, "type": "child"}, "21": {"id": 21, "funcid": 12, "lineno": 46, "end_lineno": 46, "type": "child"}, "22": {"id": 22, "funcid": 22, "lineno": 48, "end_lineno": 57, "type": "function", "name": "handle_message"}, "23": {"id": 23, "funcid": 22, "lineno": 49, "end_lineno": 51, "type": "child"}, "24": {"id": 24, "funcid": 22, "lineno": 52, "end_lineno": 52, "type": "child"}, "25": {"id": 25, "funcid": 22, "lineno": 53, "end_lineno": 53, "type": "child"}, "26": {"id": 26, "funcid": 22, "lineno": 55, "end_lineno": 57, "type": "child"}, "27": {"id": 27, "funcid": 22, "lineno": 56, "end_lineno": 56, "type": "child"}, "28": {"id": 28, "funcid": 22, "lineno": 57, "end_lineno": 57, "type": "child"}, "29": {"id": 29, "funcid": 29, "lineno": 59, "end_lineno": 71, "type": "function", "name": "register"}, "30": {"id": 30, "funcid": 29, "lineno": 60, "end_lineno": 62, "type": "child"}, "31": {"id": 31, "funcid": 29, "lineno": 63, "end_lineno": 63, "type": "child"}, "32": {"id": 32, "funcid": 29, "lineno": 66, "end_lineno": 71, "type": "child"}, "33": {"id": 33, "funcid": 33, "lineno": 74, "end_lineno": 84, "type": "function", "name": "receieve_message"}, "34": {"id": 34, "funcid": 33, "lineno": 75, "end_lineno": 77, "type": "child"}, "35": {"id": 35, "funcid": 33, "lineno": 78, "end_lineno": 84, "type": "child"}, "36": {"id": 36, "funcid": 33, "lineno": 79, "end_lineno": 79, "type": "child"}, "37": {"id": 37, "funcid": 33, "lineno": 81, "end_lineno": 82, "type": "child"}, "38": {"id": 38, "funcid": 33, "lineno": 82, "end_lineno": 82, "type": "child"}, "39": {"id": 39, "funcid": 33, "lineno": 84, "end_lineno": 84, "type": "child"}, "40": {"id": 40, "funcid": 0, "lineno": 86, "end_lineno": 87, "type": "child"}, "41": {"id": 41, "funcid": 0, "lineno": 87, "end_lineno": 87, "type": "child"}, "42": {"id": 42, "funcid": 42, "lineno": 3, "end_lineno": 38, "type": "function", "name": "countingSort"}, "43": {"id": 43, "funcid": 42, "lineno": 4, "end_lineno": 6, "type": "child"}, "44": {"id": 44, "funcid": 42, "lineno": 8, "end_lineno": 8, "type": "child"}, "45": {"id": 45, "funcid": 42, "lineno": 11, "end_lineno": 11, "type": "child"}, "46": {"id": 46, "funcid": 42, "lineno": 14, "end_lineno": 14, "type": "child"}, "47": {"id": 47, "funcid": 42, "lineno": 17, "end_lineno": 19, "type": "child"}, "48": {"id": 48, "funcid": 42, "lineno": 18, "end_lineno": 18, "type": "child"}, "49": {"id": 49, "funcid": 42, "lineno": 19, "end_lineno": 19, "type": "child"}, "50": {"id": 50, "funcid": 42, "lineno": 23, "end_lineno": 24, "type": "child"}, "51": {"id": 51, "funcid": 42, "lineno": 24, "end_lineno": 24, "type": "child"}, "52": {"id": 52, "funcid": 42, "lineno": 27, "end_lineno": 27, "type": "child"}, "53": {"id": 53, "funcid": 42, "lineno": 28, "end_lineno": 32, "type": "child"}, "54": {"id": 54, "funcid": 42, "lineno": 29, "end_lineno": 29, "type": "child"}, "55": {"id": 55, "funcid": 42, "lineno": 30, "end_lineno": 30, "type": "child"}, "56": {"id": 56, "funcid": 42, "lineno": 31, "end_lineno": 31, "type": "child"}, "57": {"id": 57, "funcid": 42, "lineno": 32, "end_lineno": 32, "type": "child"}, "58": {"id": 58, "funcid": 42, "lineno": 36, "end_lineno": 36, "type": "child"}, "59": {"id": 59, "funcid": 42, "lineno": 37, "end_lineno": 38, "type": "child"}, "60": {"id": 60, "funcid": 42, "lineno": 38, "end_lineno": 38, "type": "child"}, "61": {"id": 61, "funcid": 61, "lineno": 40, "end_lineno": 56, "type": "function", "name": "radixSort"}, "62": {"id": 62, "funcid": 61, "lineno": 41, "end_lineno": 43, "type": "child"}, "63": {"id": 63, "funcid": 61, "lineno": 46, "end_lineno": 46, "type": "child"}, "64": {"id": 64, "funcid": 61, "lineno": 51, "end_lineno": 51, "type": "child"}, "65": {"id": 65, "funcid": 61, "lineno": 52, "end_lineno": 54, "type": "child"}, "66": {"id": 66, "funcid": 61, "lineno": 53, "end_lineno": 53, "type": "child"}, "67": {"id": 67, "funcid": 61, "lineno": 54, "end_lineno": 54, "type": "child"}, "68": {"id": 68, "funcid": 61, "lineno": 56, "end_lineno": 56, "type": "child"}}, "varMap": {"1": {"varId": 1, "name": "connection", "keys": [], "logType": 6, "funcId": 0, "isTemp": false, "global": true}, "2": {"varId": 2, "name": "MSG_TYPE", "keys": [], "logType": 7, "funcId": 0, "isTemp": false, "global": true}, "3": {"varId": 3, "name": "IS_REGISTERED", "keys": [], "logType": 8, "funcId": 0, "isTemp": false, "global": true}, "4": {"varId": 4, "name": "websocket", "keys": [], "logType": 11, "funcId": 9, "isTemp": false, "global": false}, "5": {"varId": 5, "name": "response", "keys": [], "logType": 11, "funcId": 9, "isTemp": false, "global": false}, "6": {"varId": 6, "name": "n", "keys": [], "logType": 18, "funcId": 12, "isTemp": false, "global": false}, "7": {"varId": 7, "name": "sortedList", "keys": [], "logType": 19, "funcId": 12, "isTemp": false, "global": false}, "8": {"varId": 8, "name": "resp", "keys": [], "logType": 20, "funcId": 12, "isTemp": false, "global": false}, "9": {"varId": 9, "name": "message", "keys": [], "logType": 21, "funcId": 12, "isTemp": false, "global": false}, "10": {"varId": 10, "name": "message", "keys": [], "logType": 24, "funcId": 22, "isTemp": false, "global": false}, "11": {"varId": 11, "name": "asp_uid", "keys": [], "logType": 25, "funcId": 22, "isTemp": false, "global": false}, "12": {"varId": 12, "name": "response", "keys": [], "logType": 27, "funcId": 22, "isTemp": false, "global": false}, "13": {"varId": 13, "name": "websocket", "keys": [], "logType": 28, "funcId": 22, "isTemp": false, "global": false}, "14": {"varId": 14, "name": "message", "keys": [], "logType": 28, "funcId": 22, "isTemp": false, "global": false}, "15": {"varId": 15, "name": "asp_uid", "keys": [], "logType": 31, "funcId": 29, "isTemp": false, "global": false}, "16": {"varId": 16, "name": "websocket", "keys": [], "logType": 32, "funcId": 29, "isTemp": false, "global": false}, "17": {"varId": 17, "name": "websocket", "keys": [], "logType": 32, "funcId": 29, "isTemp": false, "global": false}, "18": {"varId": 18, "name": "message", "keys": [], "logType": 38, "funcId": 33, "isTemp": false, "global": false}, "19": {"varId": 19, "name": "websocket", "keys": [], "logType": 39, "funcId": 33, "isTemp": false, "global": false}, "20": {"varId": 20, "name": "websocket", "keys": [], "logType": 39, "funcId": 33, "isTemp": false, "global": false}, "21": {"varId": 21, "name": "n", "keys": [], "logType": 44, "funcId": 42, "isTemp": false, "global": false}, "22": {"varId": 22, "name": "output", "keys": [], "logType": 45, "funcId": 42, "isTemp": false, "global": false}, "23": {"varId": 23, "name": "count", "keys": [], "logType": 46, "funcId": 42, "isTemp": false, "global": false}, "24": {"varId": 24, "name": "index", "keys": [], "logType": 48, "funcId": 42, "isTemp": false, "global": false}, "25": {"varId": 25, "name": "asp_temp_var_b0c8c016099b11f0aaa963f0c00b7079", "keys": [], "logType": 49, "funcId": 42, "isTemp": true, "global": false}, "26": {"varId": 26, "name": "count", "keys": [{"type": "temp_variable", "value": "asp_temp_var_b0c8c016099b11f0aaa963f0c00b7079"}], "logType": 49, "funcId": 42, "isTemp": false, "global": false}, "27": {"varId": 27, "name": "i", "keys": [], "logType": 49, "funcId": 42, "isTemp": false, "global": false}, "28": {"varId": 28, "name": "count", "keys": [{"type": "variable", "value": "i"}], "logType": 51, "funcId": 42, "isTemp": false, "global": false}, "29": {"varId": 29, "name": "i", "keys": [], "logType": 51, "funcId": 42, "isTemp": false, "global": false}, "30": {"varId": 30, "name": "i", "keys": [], "logType": 52, "funcId": 42, "isTemp": false, "global": false}, "31": {"varId": 31, "name": "index", "keys": [], "logType": 54, "funcId": 42, "isTemp": false, "global": false}, "32": {"varId": 32, "name": "asp_temp_var_b0c8c017099b11f0aaa963f0c00b7079", "keys": [], "logType": 55, "funcId": 42, "isTemp": true, "global": false}, "33": {"varId": 33, "name": "output", "keys": [{"type": "temp_variable", "value": "asp_temp_var_b0c8c017099b11f0aaa963f0c00b7079"}], "logType": 55, "funcId": 42, "isTemp": false, "global": false}, "34": {"varId": 34, "name": "asp_temp_var_b0c8c018099b11f0aaa963f0c00b7079", "keys": [], "logType": 56, "funcId": 42, "isTemp": true, "global": false}, "35": {"varId": 35, "name": "count", "keys": [{"type": "temp_variable", "value": "asp_temp_var_b0c8c018099b11f0aaa963f0c00b7079"}], "logType": 56, "funcId": 42, "isTemp": false, "global": false}, "36": {"varId": 36, "name": "i", "keys": [], "logType": 57, "funcId": 42, "isTemp": false, "global": false}, "37": {"varId": 37, "name": "i", "keys": [], "logType": 58, "funcId": 42, "isTemp": false, "global": false}, "38": {"varId": 38, "name": "arr", "keys": [{"type": "variable", "value": "i"}], "logType": 60, "funcId": 42, "isTemp": false, "global": false}, "39": {"varId": 39, "name": "i", "keys": [], "logType": 60, "funcId": 42, "isTemp": false, "global": false}, "40": {"varId": 40, "name": "arr", "keys": [], "logType": 60, "funcId": 42, "isTemp": false, "global": false}, "41": {"varId": 41, "name": "exp1", "keys": [], "logType": 60, "funcId": 42, "isTemp": false, "global": false}, "42": {"varId": 42, "name": "max1", "keys": [], "logType": 63, "funcId": 61, "isTemp": false, "global": false}, "43": {"varId": 43, "name": "exp", "keys": [], "logType": 64, "funcId": 61, "isTemp": false, "global": false}, "44": {"varId": 44, "name": "exp", "keys": [], "logType": 67, "funcId": 61, "isTemp": false, "global": false}, "45": {"varId": 45, "name": "arr", "keys": [], "logType": 68, "funcId": 61, "isTemp": false, "global": false}}}')
try:
    logger.info(1)
    import websockets
    logger.info(2)
    import asyncio
    logger.info(3)
    import json
    logger.info(4)
    from radixSort import radixSort
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
        sortedList = radixSort(message['data'])
        aspAdliVarLog(sortedList, 7)
        logger.info(20)
        resp = {'code': MSG_TYPE['RESPONSE'], 'worker': True, 'type': 'radixSort', 'value': sortedList, 'asp_uid': message['asp_uid'], 'user': message['user']}
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
        await websocket.send(json.dumps({'code': MSG_TYPE['REGISTER'], 'worker': True, 'type': 'radixSort', 'asp_uid': asp_uid}))
        aspAdliVarLog(websocket, 16)

    async def receieve_message():
        logger.info(33)
        logger.info(34)
        '\n        Main loop receives jobs, executes them and responds.\n    '
        logger.info(35)
        async with connection as websocket:
            aspAdliVarLog(websocket, 20)
            logger.info(36)
            await register(websocket=websocket)
            logger.info(37)
            async for message in websocket:
                aspAdliVarLog(message, 18)
                logger.info(38)
                await handle_message(websocket=websocket, message=message)
                logger.info(37)
            logger.info(39)
            await websocket.close()
            aspAdliVarLog(websocket, 19)
    logger.info(40)
    if __name__ == '__main__':
        logger.info(41)
        asyncio.run(receieve_message())
except Exception as e:
    logger.error(f'? {traceback.format_exc()}')
    raise