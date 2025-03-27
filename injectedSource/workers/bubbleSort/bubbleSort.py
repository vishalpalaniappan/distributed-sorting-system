import logging
import json
logger = logging.getLogger('adli')

def aspAdliVarLog(val, varid):
    try:
        val = json.dumps(val, default=lambda o: o.__dict__)
    except:
        pass
    logger.info(f'# {varid} {val}')

def bubble_sort(arr):
    logger.info(46)
    aspAdliVarLog(arr, 27)
    logger.info(47)
    for n in range(len(arr) - 1, 0, -1):
        aspAdliVarLog(n, 26)
        logger.info(48)
        swapped = False
        aspAdliVarLog(swapped, 21)
        logger.info(49)
        for i in range(n):
            aspAdliVarLog(i, 25)
            logger.info(50)
            if arr[i] > arr[i + 1]:
                asp_temp_var_5ab545f009f011f09997b14cf8cd16f4 = i + 1
                aspAdliVarLog(asp_temp_var_5ab545f009f011f09997b14cf8cd16f4, 22)
                logger.info(51)
                (arr[i], arr[asp_temp_var_5ab545f009f011f09997b14cf8cd16f4]) = (arr[i + 1], arr[i])
                aspAdliVarLog((arr[i], arr[asp_temp_var_5ab545f009f011f09997b14cf8cd16f4]), 23)
                logger.info(52)
                swapped = True
                aspAdliVarLog(swapped, 24)
            logger.info(49)
        logger.info(53)
        if not swapped:
            logger.info(54)
            break
        logger.info(47)
    logger.info(55)
    return arr