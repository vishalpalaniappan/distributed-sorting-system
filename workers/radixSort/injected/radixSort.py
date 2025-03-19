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

def countingSort(arr, exp1):
    logger.info(35)
    aspAdliVarLog(arr, 39)
    aspAdliVarLog(exp1, 40)
    logger.info(36)
    '\n        Reference: https://www.geeksforgeeks.org/python-program-for-radix-sort/\n    '
    logger.info(37)
    n = len(arr)
    aspAdliVarLog(n, 20)
    logger.info(38)
    output = [0] * n
    aspAdliVarLog(output, 21)
    logger.info(39)
    count = [0] * 10
    aspAdliVarLog(count, 22)
    logger.info(40)
    for i in range(0, n):
        aspAdliVarLog(i, 26)
        logger.info(41)
        index = arr[i] / exp1
        aspAdliVarLog(index, 23)
        asp_temp_var_b543d980046111f0b89d9f0ee9e28e0e = int(index % 10)
        aspAdliVarLog(asp_temp_var_b543d980046111f0b89d9f0ee9e28e0e, 24)
        logger.info(42)
        count[asp_temp_var_b543d980046111f0b89d9f0ee9e28e0e] += 1
        aspAdliVarLog(count[asp_temp_var_b543d980046111f0b89d9f0ee9e28e0e], 25)
        logger.info(40)
    logger.info(43)
    for i in range(1, 10):
        aspAdliVarLog(i, 28)
        logger.info(44)
        count[i] += count[i - 1]
        aspAdliVarLog(count[i], 27)
        logger.info(43)
    logger.info(45)
    i = n - 1
    aspAdliVarLog(i, 29)
    logger.info(46)
    while i >= 0:
        logger.info(47)
        index = arr[i] / exp1
        aspAdliVarLog(index, 30)
        asp_temp_var_b543d981046111f0b89d9f0ee9e28e0e = count[int(index % 10)] - 1
        aspAdliVarLog(asp_temp_var_b543d981046111f0b89d9f0ee9e28e0e, 31)
        logger.info(48)
        output[asp_temp_var_b543d981046111f0b89d9f0ee9e28e0e] = arr[i]
        aspAdliVarLog(output[asp_temp_var_b543d981046111f0b89d9f0ee9e28e0e], 32)
        asp_temp_var_b543d982046111f0b89d9f0ee9e28e0e = int(index % 10)
        aspAdliVarLog(asp_temp_var_b543d982046111f0b89d9f0ee9e28e0e, 33)
        logger.info(49)
        count[asp_temp_var_b543d982046111f0b89d9f0ee9e28e0e] -= 1
        aspAdliVarLog(count[asp_temp_var_b543d982046111f0b89d9f0ee9e28e0e], 34)
        logger.info(50)
        i -= 1
        aspAdliVarLog(i, 35)
        logger.info(46)
    logger.info(51)
    i = 0
    aspAdliVarLog(i, 36)
    logger.info(52)
    for i in range(0, len(arr)):
        aspAdliVarLog(i, 38)
        logger.info(53)
        arr[i] = output[i]
        aspAdliVarLog(arr[i], 37)
        logger.info(52)

def radixSort(arr):
    logger.info(54)
    aspAdliVarLog(arr, 44)
    logger.info(55)
    '\n        Reference: https://www.geeksforgeeks.org/python-program-for-radix-sort/\n    '
    logger.info(56)
    max1 = max(arr)
    aspAdliVarLog(max1, 41)
    logger.info(57)
    exp = 1
    aspAdliVarLog(exp, 42)
    logger.info(58)
    while max1 // exp > 0:
        logger.info(59)
        countingSort(arr, exp)
        logger.info(60)
        exp *= 10
        aspAdliVarLog(exp, 43)
        logger.info(58)
    logger.info(61)
    return arr