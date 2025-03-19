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
    logger.info(34)
    aspAdliVarLog(arr, 25)
    logger.info(35)
    for n in range(len(arr) - 1, 0, -1):
        aspAdliVarLog(n, 24)
        logger.info(36)
        swapped = False
        aspAdliVarLog(swapped, 19)
        logger.info(37)
        for i in range(n):
            aspAdliVarLog(i, 23)
            logger.info(38)
            if arr[i] > arr[i + 1]:
                asp_temp_var_bcdaf700046111f0b89d9f0ee9e28e0e = i + 1
                aspAdliVarLog(asp_temp_var_bcdaf700046111f0b89d9f0ee9e28e0e, 20)
                logger.info(39)
                (arr[i], arr[asp_temp_var_bcdaf700046111f0b89d9f0ee9e28e0e]) = (arr[i + 1], arr[i])
                aspAdliVarLog((arr[i], arr[asp_temp_var_bcdaf700046111f0b89d9f0ee9e28e0e]), 21)
                logger.info(40)
                swapped = True
                aspAdliVarLog(swapped, 22)
            logger.info(37)
        logger.info(41)
        if not swapped:
            logger.info(42)
            break
        logger.info(35)
    logger.info(43)
    return arr