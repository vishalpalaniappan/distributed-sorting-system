import traceback
import logging
import json
import sys
from pathlib import Path
from clp_logging.handlers import CLPFileHandler
clp_handler = CLPFileHandler(Path('./simulatedClient.clp.zst'))
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
logger.info('{"fileTree": {"simulatedClient.py": {"source": "\\nimport websockets\\nimport asyncio\\nimport json\\nimport random\\nimport time\\nimport uuid\\n\\nconnection = websockets.connect(uri=\'ws://localhost:8765\', ping_interval=None)\\n\\nMSG_TYPE = {\\n    \\"REGISTER\\": 1,\\n    \\"REQUEST\\": 2,\\n    \\"RESPONSE\\": 3\\n}\\n\\nJOB_TYPES = [\\n    \\"bubbleSort\\",\\n    \\"mergeSort\\",\\n    \\"radixSort\\"\\n]\\n\\nIS_REGISTERED = False\\n\\nasync def sendRandomJob(websocket, asp_uid):\\n    # Send response\\n    await websocket.send(json.dumps({\\n        \\"code\\": MSG_TYPE[\\"REQUEST\\"],\\n        \\"worker\\": True,\\n        \\"type\\": JOB_TYPES[random.randint(0,2)],\\n        \\"data\\": random.sample(range(6, 101), random.randint(5,15)),\\n        \\"asp_uid\\": asp_uid\\n    }))\\n\\nasync def main():\\n    \'\'\'\\n        Main loop receives jobs, executes them and responds.\\n    \'\'\'\\n    async with connection as websocket:\\n\\n        asp_uid = str(uuid.uuid4())\\n\\n        # Send message to register the worker.\\n        await websocket.send(json.dumps({\\n            \\"code\\": MSG_TYPE[\\"REGISTER\\"],\\n            \\"client\\": True,\\n            \\"asp_uid\\": asp_uid\\n        }))\\n\\n        time.sleep(2)\\n        try:\\n            async for message in websocket:\\n                asp_uid = str(uuid.uuid4())\\n                await sendRandomJob(websocket= websocket, asp_uid= asp_uid)\\n                time.sleep(random.randrange(1, 10))\\n        except KeyboardInterrupt:\\n            print(\'interrupted!\')\\n        except:\\n            pass\\n\\n        await websocket.close()\\n\\n\\nasync def main2():\\n    async with connection as websocket:\\n\\n         # Listen for messages\\n        async for message in websocket:\\n            print(message)\\n\\n\\nif __name__ == \\"__main__\\":\\n    asyncio.run(main())\\n    asyncio.run(main2())", "minLt": 0, "maxLt": 35}}, "ltMap": {"1": {"id": 1, "funcid": 0, "lineno": 2, "end_lineno": 2, "type": "child"}, "2": {"id": 2, "funcid": 0, "lineno": 3, "end_lineno": 3, "type": "child"}, "3": {"id": 3, "funcid": 0, "lineno": 4, "end_lineno": 4, "type": "child"}, "4": {"id": 4, "funcid": 0, "lineno": 5, "end_lineno": 5, "type": "child"}, "5": {"id": 5, "funcid": 0, "lineno": 6, "end_lineno": 6, "type": "child"}, "6": {"id": 6, "funcid": 0, "lineno": 7, "end_lineno": 7, "type": "child"}, "7": {"id": 7, "funcid": 0, "lineno": 9, "end_lineno": 9, "type": "child"}, "8": {"id": 8, "funcid": 0, "lineno": 11, "end_lineno": 15, "type": "child"}, "9": {"id": 9, "funcid": 0, "lineno": 17, "end_lineno": 21, "type": "child"}, "10": {"id": 10, "funcid": 0, "lineno": 23, "end_lineno": 23, "type": "child"}, "11": {"id": 11, "funcid": 11, "lineno": 25, "end_lineno": 33, "type": "function", "name": "sendRandomJob"}, "12": {"id": 12, "funcid": 11, "lineno": 27, "end_lineno": 33, "type": "child"}, "13": {"id": 13, "funcid": 13, "lineno": 35, "end_lineno": 61, "type": "function", "name": "main"}, "14": {"id": 14, "funcid": 13, "lineno": 36, "end_lineno": 38, "type": "child"}, "15": {"id": 15, "funcid": 13, "lineno": 39, "end_lineno": 61, "type": "child"}, "16": {"id": 16, "funcid": 13, "lineno": 41, "end_lineno": 41, "type": "child"}, "17": {"id": 17, "funcid": 13, "lineno": 44, "end_lineno": 48, "type": "child"}, "18": {"id": 18, "funcid": 13, "lineno": 50, "end_lineno": 50, "type": "child"}, "19": {"id": 19, "funcid": 13, "lineno": 51, "end_lineno": 59, "type": "child"}, "20": {"id": 20, "funcid": 13, "lineno": 52, "end_lineno": 55, "type": "child"}, "21": {"id": 21, "funcid": 13, "lineno": 53, "end_lineno": 53, "type": "child"}, "22": {"id": 22, "funcid": 13, "lineno": 54, "end_lineno": 54, "type": "child"}, "23": {"id": 23, "funcid": 13, "lineno": 55, "end_lineno": 55, "type": "child"}, "24": {"id": 24, "funcid": 13, "lineno": 56, "end_lineno": 57, "type": "child"}, "25": {"id": 25, "funcid": 13, "lineno": 57, "end_lineno": 57, "type": "child"}, "26": {"id": 26, "funcid": 13, "lineno": 58, "end_lineno": 59, "type": "child"}, "27": {"id": 27, "funcid": 13, "lineno": 59, "end_lineno": 59, "type": "child"}, "28": {"id": 28, "funcid": 13, "lineno": 61, "end_lineno": 61, "type": "child"}, "29": {"id": 29, "funcid": 29, "lineno": 64, "end_lineno": 69, "type": "function", "name": "main2"}, "30": {"id": 30, "funcid": 29, "lineno": 65, "end_lineno": 69, "type": "child"}, "31": {"id": 31, "funcid": 29, "lineno": 68, "end_lineno": 69, "type": "child"}, "32": {"id": 32, "funcid": 29, "lineno": 69, "end_lineno": 69, "type": "child"}, "33": {"id": 33, "funcid": 0, "lineno": 72, "end_lineno": 74, "type": "child"}, "34": {"id": 34, "funcid": 0, "lineno": 73, "end_lineno": 73, "type": "child"}, "35": {"id": 35, "funcid": 0, "lineno": 74, "end_lineno": 74, "type": "child"}}, "varMap": {"1": {"varId": 1, "name": "connection", "keys": [], "logType": 7, "funcId": 0, "isTemp": false, "global": true}, "2": {"varId": 2, "name": "MSG_TYPE", "keys": [], "logType": 8, "funcId": 0, "isTemp": false, "global": true}, "3": {"varId": 3, "name": "JOB_TYPES", "keys": [], "logType": 9, "funcId": 0, "isTemp": false, "global": true}, "4": {"varId": 4, "name": "IS_REGISTERED", "keys": [], "logType": 10, "funcId": 0, "isTemp": false, "global": true}, "5": {"varId": 5, "name": "websocket", "keys": [], "logType": 12, "funcId": 11, "isTemp": false, "global": false}, "6": {"varId": 6, "name": "asp_uid", "keys": [], "logType": 12, "funcId": 11, "isTemp": false, "global": false}, "7": {"varId": 7, "name": "asp_uid", "keys": [], "logType": 16, "funcId": 13, "isTemp": false, "global": false}, "8": {"varId": 8, "name": "websocket", "keys": [], "logType": 17, "funcId": 13, "isTemp": false, "global": false}, "9": {"varId": 9, "name": "asp_uid", "keys": [], "logType": 21, "funcId": 13, "isTemp": false, "global": false}, "10": {"varId": 10, "name": "message", "keys": [], "logType": 23, "funcId": 13, "isTemp": false, "global": false}, "11": {"varId": 11, "name": "websocket", "keys": [], "logType": 28, "funcId": 13, "isTemp": false, "global": false}, "12": {"varId": 12, "name": "websocket", "keys": [], "logType": 28, "funcId": 13, "isTemp": false, "global": false}, "13": {"varId": 13, "name": "message", "keys": [], "logType": 32, "funcId": 29, "isTemp": false, "global": false}, "14": {"varId": 14, "name": "websocket", "keys": [], "logType": 32, "funcId": 29, "isTemp": false, "global": false}}}')
try:
    logger.info(1)
    import websockets
    logger.info(2)
    import asyncio
    logger.info(3)
    import json
    logger.info(4)
    import random
    logger.info(5)
    import time
    logger.info(6)
    import uuid
    logger.info(7)
    connection = websockets.connect(uri='ws://localhost:8765', ping_interval=None)
    aspAdliVarLog(connection, 1)
    logger.info(8)
    MSG_TYPE = {'REGISTER': 1, 'REQUEST': 2, 'RESPONSE': 3}
    aspAdliVarLog(MSG_TYPE, 2)
    logger.info(9)
    JOB_TYPES = ['bubbleSort', 'mergeSort', 'radixSort']
    aspAdliVarLog(JOB_TYPES, 3)
    logger.info(10)
    IS_REGISTERED = False
    aspAdliVarLog(IS_REGISTERED, 4)

    async def sendRandomJob(websocket, asp_uid):
        logger.info(11)
        aspAdliVarLog(websocket, 5)
        aspAdliVarLog(asp_uid, 6)
        logger.info(12)
        await websocket.send(json.dumps({'code': MSG_TYPE['REQUEST'], 'worker': True, 'type': JOB_TYPES[random.randint(0, 2)], 'data': random.sample(range(6, 101), random.randint(5, 15)), 'asp_uid': asp_uid}))

    async def main():
        logger.info(13)
        logger.info(14)
        '\n        Main loop receives jobs, executes them and responds.\n    '
        logger.info(15)
        async with connection as websocket:
            aspAdliVarLog(websocket, 12)
            logger.info(16)
            asp_uid = str(uuid.uuid4())
            aspAdliVarLog(asp_uid, 7)
            logger.info(17)
            await websocket.send(json.dumps({'code': MSG_TYPE['REGISTER'], 'client': True, 'asp_uid': asp_uid}))
            aspAdliVarLog(websocket, 8)
            logger.info(18)
            time.sleep(2)
            try:
                logger.info(19)
                logger.info(20)
                async for message in websocket:
                    aspAdliVarLog(message, 10)
                    logger.info(21)
                    asp_uid = str(uuid.uuid4())
                    aspAdliVarLog(asp_uid, 9)
                    logger.info(22)
                    await sendRandomJob(websocket=websocket, asp_uid=asp_uid)
                    logger.info(23)
                    time.sleep(random.randrange(1, 10))
                    logger.info(20)
            except KeyboardInterrupt:
                logger.info(24)
                logger.info(25)
                print('interrupted!')
            except:
                logger.info(26)
                logger.info(27)
                pass
            logger.info(28)
            await websocket.close()
            aspAdliVarLog(websocket, 11)

    async def main2():
        logger.info(29)
        logger.info(30)
        async with connection as websocket:
            aspAdliVarLog(websocket, 14)
            logger.info(31)
            async for message in websocket:
                aspAdliVarLog(message, 13)
                logger.info(32)
                print(message)
                logger.info(31)
    logger.info(33)
    if __name__ == '__main__':
        logger.info(34)
        asyncio.run(main())
        logger.info(35)
        asyncio.run(main2())
except Exception as e:
    logger.error(f'? {traceback.format_exc()}')
    raise