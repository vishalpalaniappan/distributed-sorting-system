import logging
import json
logger = logging.getLogger('adli')

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

def bubble_sort(arr):
    logger.info(45)
    aspAdliVarLog(arr, 27)
    logger.info(46)
    for n in range(len(arr) - 1, 0, -1):
        aspAdliVarLog(n, 26)
        logger.info(47)
        swapped = False
        aspAdliVarLog(swapped, 21)
        logger.info(48)
        for i in range(n):
            aspAdliVarLog(i, 25)
            logger.info(49)
            if arr[i] > arr[i + 1]:
                asp_temp_var_9ba3b150099b11f0aaa963f0c00b7079 = i + 1
                aspAdliVarLog(asp_temp_var_9ba3b150099b11f0aaa963f0c00b7079, 22)
                logger.info(50)
                (arr[i], arr[asp_temp_var_9ba3b150099b11f0aaa963f0c00b7079]) = (arr[i + 1], arr[i])
                aspAdliVarLog((arr[i], arr[asp_temp_var_9ba3b150099b11f0aaa963f0c00b7079]), 23)
                logger.info(51)
                swapped = True
                aspAdliVarLog(swapped, 24)
            logger.info(48)
        logger.info(52)
        if not swapped:
            logger.info(53)
            break
        logger.info(46)
    logger.info(54)
    return arr