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
    logger.info(42)
    aspAdliVarLog(arr, 40)
    aspAdliVarLog(exp1, 41)
    logger.info(43)
    '\n        Reference: https://www.geeksforgeeks.org/python-program-for-radix-sort/\n    '
    logger.info(44)
    n = len(arr)
    aspAdliVarLog(n, 21)
    logger.info(45)
    output = [0] * n
    aspAdliVarLog(output, 22)
    logger.info(46)
    count = [0] * 10
    aspAdliVarLog(count, 23)
    logger.info(47)
    for i in range(0, n):
        aspAdliVarLog(i, 27)
        logger.info(48)
        index = arr[i] / exp1
        aspAdliVarLog(index, 24)
        asp_temp_var_b0c8c016099b11f0aaa963f0c00b7079 = int(index % 10)
        aspAdliVarLog(asp_temp_var_b0c8c016099b11f0aaa963f0c00b7079, 25)
        logger.info(49)
        count[asp_temp_var_b0c8c016099b11f0aaa963f0c00b7079] += 1
        aspAdliVarLog(count[asp_temp_var_b0c8c016099b11f0aaa963f0c00b7079], 26)
        logger.info(47)
    logger.info(50)
    for i in range(1, 10):
        aspAdliVarLog(i, 29)
        logger.info(51)
        count[i] += count[i - 1]
        aspAdliVarLog(count[i], 28)
        logger.info(50)
    logger.info(52)
    i = n - 1
    aspAdliVarLog(i, 30)
    logger.info(53)
    while i >= 0:
        logger.info(54)
        index = arr[i] / exp1
        aspAdliVarLog(index, 31)
        asp_temp_var_b0c8c017099b11f0aaa963f0c00b7079 = count[int(index % 10)] - 1
        aspAdliVarLog(asp_temp_var_b0c8c017099b11f0aaa963f0c00b7079, 32)
        logger.info(55)
        output[asp_temp_var_b0c8c017099b11f0aaa963f0c00b7079] = arr[i]
        aspAdliVarLog(output[asp_temp_var_b0c8c017099b11f0aaa963f0c00b7079], 33)
        asp_temp_var_b0c8c018099b11f0aaa963f0c00b7079 = int(index % 10)
        aspAdliVarLog(asp_temp_var_b0c8c018099b11f0aaa963f0c00b7079, 34)
        logger.info(56)
        count[asp_temp_var_b0c8c018099b11f0aaa963f0c00b7079] -= 1
        aspAdliVarLog(count[asp_temp_var_b0c8c018099b11f0aaa963f0c00b7079], 35)
        logger.info(57)
        i -= 1
        aspAdliVarLog(i, 36)
        logger.info(53)
    logger.info(58)
    i = 0
    aspAdliVarLog(i, 37)
    logger.info(59)
    for i in range(0, len(arr)):
        aspAdliVarLog(i, 39)
        logger.info(60)
        arr[i] = output[i]
        aspAdliVarLog(arr[i], 38)
        logger.info(59)

def radixSort(arr):
    logger.info(61)
    aspAdliVarLog(arr, 45)
    logger.info(62)
    '\n        Reference: https://www.geeksforgeeks.org/python-program-for-radix-sort/\n    '
    logger.info(63)
    max1 = max(arr)
    aspAdliVarLog(max1, 42)
    logger.info(64)
    exp = 1
    aspAdliVarLog(exp, 43)
    logger.info(65)
    while max1 // exp > 0:
        logger.info(66)
        countingSort(arr, exp)
        logger.info(67)
        exp *= 10
        aspAdliVarLog(exp, 44)
        logger.info(65)
    logger.info(68)
    return arr