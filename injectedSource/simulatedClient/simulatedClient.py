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
logger.info('{"fileTree": {"simulatedClient.py": {"source": "\\nimport websockets\\nimport asyncio\\nimport json\\nimport random\\nimport time\\nimport uuid\\n\\nconnection = websockets.connect(uri=\'ws://localhost:8765\', ping_interval=None)\\n\\nMSG_TYPE = {\\n    \\"REGISTER\\": 1,\\n    \\"REQUEST\\": 2,\\n    \\"RESPONSE\\": 3\\n}\\n\\nJOB_TYPES = [\\n    \\"bubbleSort\\",\\n    \\"mergeSort\\",\\n    \\"radixSort\\"\\n]\\n\\nUSERS = [\\n    \\"user1\\",\\n    \\"user2\\",\\n    \\"user3\\",\\n    \\"user4\\",\\n    \\"user5\\",\\n]\\n\\nIS_REGISTERED = False\\n\\nasync def sendRandomJob(websocket):\\n    \'\'\'\\n        Send a random job from a random user to the jobHandler.\\n    \'\'\'\\n    asp_uid = str(uuid.uuid4())\\n    \\n    await websocket.send(json.dumps({\\n        \\"code\\": MSG_TYPE[\\"REQUEST\\"],\\n        \\"worker\\": True,\\n        \\"type\\": JOB_TYPES[random.randint(0, len(JOB_TYPES) - 1)],\\n        \\"user\\": USERS[random.randint(0, len(USERS) - 1)],\\n        \\"data\\": random.sample(range(6, 101), random.randint(5,15)),\\n        \\"asp_uid\\": asp_uid\\n    }))\\n\\nasync def registerClient(websocket):\\n    \'\'\'\\n        Register the client.\\n    \'\'\'\\n    asp_uid = str(uuid.uuid4())\\n    await websocket.send(json.dumps({\\n        \\"code\\": MSG_TYPE[\\"REGISTER\\"],\\n        \\"client\\": True,\\n        \\"asp_uid\\": asp_uid\\n    }))\\n\\nasync def main():\\n    \'\'\'\\n        Main loop receives jobs, executes them and responds.\\n    \'\'\'\\n    async with connection as websocket:\\n        await registerClient(websocket=websocket)\\n        time.sleep(2)\\n        try:\\n            async for message in websocket:\\n                await sendRandomJob(websocket= websocket)\\n                time.sleep(random.randrange(1, 10))\\n        except KeyboardInterrupt:\\n            print(\'interrupted!\')\\n        except:\\n            pass\\n\\n        await websocket.close()\\n\\n\\nif __name__ == \\"__main__\\":\\n    asyncio.run(main())", "minLt": 0, "maxLt": 35}}, "ltMap": {"1": {"id": 1, "funcid": 0, "lineno": 2, "end_lineno": 2, "type": "child"}, "2": {"id": 2, "funcid": 0, "lineno": 3, "end_lineno": 3, "type": "child"}, "3": {"id": 3, "funcid": 0, "lineno": 4, "end_lineno": 4, "type": "child"}, "4": {"id": 4, "funcid": 0, "lineno": 5, "end_lineno": 5, "type": "child"}, "5": {"id": 5, "funcid": 0, "lineno": 6, "end_lineno": 6, "type": "child"}, "6": {"id": 6, "funcid": 0, "lineno": 7, "end_lineno": 7, "type": "child"}, "7": {"id": 7, "funcid": 0, "lineno": 9, "end_lineno": 9, "type": "child"}, "8": {"id": 8, "funcid": 0, "lineno": 11, "end_lineno": 15, "type": "child"}, "9": {"id": 9, "funcid": 0, "lineno": 17, "end_lineno": 21, "type": "child"}, "10": {"id": 10, "funcid": 0, "lineno": 23, "end_lineno": 29, "type": "child"}, "11": {"id": 11, "funcid": 0, "lineno": 31, "end_lineno": 31, "type": "child"}, "12": {"id": 12, "funcid": 12, "lineno": 33, "end_lineno": 46, "type": "function", "name": "sendRandomJob"}, "13": {"id": 13, "funcid": 12, "lineno": 34, "end_lineno": 36, "type": "child"}, "14": {"id": 14, "funcid": 12, "lineno": 37, "end_lineno": 37, "type": "child"}, "15": {"id": 15, "funcid": 12, "lineno": 39, "end_lineno": 46, "type": "child"}, "16": {"id": 16, "funcid": 16, "lineno": 48, "end_lineno": 57, "type": "function", "name": "registerClient"}, "17": {"id": 17, "funcid": 16, "lineno": 49, "end_lineno": 51, "type": "child"}, "18": {"id": 18, "funcid": 16, "lineno": 52, "end_lineno": 52, "type": "child"}, "19": {"id": 19, "funcid": 16, "lineno": 53, "end_lineno": 57, "type": "child"}, "20": {"id": 20, "funcid": 20, "lineno": 59, "end_lineno": 75, "type": "function", "name": "main"}, "21": {"id": 21, "funcid": 20, "lineno": 60, "end_lineno": 62, "type": "child"}, "22": {"id": 22, "funcid": 20, "lineno": 63, "end_lineno": 75, "type": "child"}, "23": {"id": 23, "funcid": 20, "lineno": 64, "end_lineno": 64, "type": "child"}, "24": {"id": 24, "funcid": 20, "lineno": 65, "end_lineno": 65, "type": "child"}, "25": {"id": 25, "funcid": 20, "lineno": 66, "end_lineno": 73, "type": "child"}, "26": {"id": 26, "funcid": 20, "lineno": 67, "end_lineno": 69, "type": "child"}, "27": {"id": 27, "funcid": 20, "lineno": 68, "end_lineno": 68, "type": "child"}, "28": {"id": 28, "funcid": 20, "lineno": 69, "end_lineno": 69, "type": "child"}, "29": {"id": 29, "funcid": 20, "lineno": 70, "end_lineno": 71, "type": "child"}, "30": {"id": 30, "funcid": 20, "lineno": 71, "end_lineno": 71, "type": "child"}, "31": {"id": 31, "funcid": 20, "lineno": 72, "end_lineno": 73, "type": "child"}, "32": {"id": 32, "funcid": 20, "lineno": 73, "end_lineno": 73, "type": "child"}, "33": {"id": 33, "funcid": 20, "lineno": 75, "end_lineno": 75, "type": "child"}, "34": {"id": 34, "funcid": 0, "lineno": 78, "end_lineno": 79, "type": "child"}, "35": {"id": 35, "funcid": 0, "lineno": 79, "end_lineno": 79, "type": "child"}}, "varMap": {"1": {"varId": 1, "name": "connection", "keys": [], "logType": 7, "funcId": 0, "isTemp": false, "global": true}, "2": {"varId": 2, "name": "MSG_TYPE", "keys": [], "logType": 8, "funcId": 0, "isTemp": false, "global": true}, "3": {"varId": 3, "name": "JOB_TYPES", "keys": [], "logType": 9, "funcId": 0, "isTemp": false, "global": true}, "4": {"varId": 4, "name": "USERS", "keys": [], "logType": 10, "funcId": 0, "isTemp": false, "global": true}, "5": {"varId": 5, "name": "IS_REGISTERED", "keys": [], "logType": 11, "funcId": 0, "isTemp": false, "global": true}, "6": {"varId": 6, "name": "asp_uid", "keys": [], "logType": 14, "funcId": 12, "isTemp": false, "global": false}, "7": {"varId": 7, "name": "websocket", "keys": [], "logType": 15, "funcId": 12, "isTemp": false, "global": false}, "8": {"varId": 8, "name": "asp_uid", "keys": [], "logType": 18, "funcId": 16, "isTemp": false, "global": false}, "9": {"varId": 9, "name": "websocket", "keys": [], "logType": 19, "funcId": 16, "isTemp": false, "global": false}, "10": {"varId": 10, "name": "websocket", "keys": [], "logType": 19, "funcId": 16, "isTemp": false, "global": false}, "11": {"varId": 11, "name": "message", "keys": [], "logType": 28, "funcId": 20, "isTemp": false, "global": false}, "12": {"varId": 12, "name": "websocket", "keys": [], "logType": 33, "funcId": 20, "isTemp": false, "global": false}, "13": {"varId": 13, "name": "websocket", "keys": [], "logType": 33, "funcId": 20, "isTemp": false, "global": false}}}')
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
    USERS = ['user1', 'user2', 'user3', 'user4', 'user5']
    aspAdliVarLog(USERS, 4)
    logger.info(11)
    IS_REGISTERED = False
    aspAdliVarLog(IS_REGISTERED, 5)

    async def sendRandomJob(websocket):
        logger.info(12)
        aspAdliVarLog(websocket, 7)
        logger.info(13)
        '\n        Send a random job from a random user to the jobHandler.\n    '
        logger.info(14)
        asp_uid = str(uuid.uuid4())
        aspAdliVarLog(asp_uid, 6)
        logger.info(15)
        await websocket.send(json.dumps({'code': MSG_TYPE['REQUEST'], 'worker': True, 'type': JOB_TYPES[random.randint(0, len(JOB_TYPES) - 1)], 'user': USERS[random.randint(0, len(USERS) - 1)], 'data': random.sample(range(6, 101), random.randint(5, 15)), 'asp_uid': asp_uid}))

    async def registerClient(websocket):
        logger.info(16)
        aspAdliVarLog(websocket, 10)
        logger.info(17)
        '\n        Register the client.\n    '
        logger.info(18)
        asp_uid = str(uuid.uuid4())
        aspAdliVarLog(asp_uid, 8)
        logger.info(19)
        await websocket.send(json.dumps({'code': MSG_TYPE['REGISTER'], 'client': True, 'asp_uid': asp_uid}))
        aspAdliVarLog(websocket, 9)

    async def main():
        logger.info(20)
        logger.info(21)
        '\n        Main loop receives jobs, executes them and responds.\n    '
        logger.info(22)
        async with connection as websocket:
            aspAdliVarLog(websocket, 13)
            logger.info(23)
            await registerClient(websocket=websocket)
            logger.info(24)
            time.sleep(2)
            try:
                logger.info(25)
                logger.info(26)
                async for message in websocket:
                    aspAdliVarLog(message, 11)
                    logger.info(27)
                    await sendRandomJob(websocket=websocket)
                    logger.info(28)
                    time.sleep(random.randrange(1, 10))
                    logger.info(26)
            except KeyboardInterrupt:
                logger.info(29)
                logger.info(30)
                print('interrupted!')
            except:
                logger.info(31)
                logger.info(32)
                pass
            logger.info(33)
            await websocket.close()
            aspAdliVarLog(websocket, 12)
    logger.info(34)
    if __name__ == '__main__':
        logger.info(35)
        asyncio.run(main())
except Exception as e:
    logger.error(f'? {traceback.format_exc()}')
    raise