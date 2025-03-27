import logging
import json
logger = logging.getLogger('adli')

def aspAdliVarLog(val, varid):
    try:
        val = json.dumps(val, default=lambda o: o.__dict__)
    except:
        pass
    logger.info(f'# {varid} {val}')

def countingSort(arr, exp1):
    logger.info(43)
    aspAdliVarLog(arr, 40)
    aspAdliVarLog(exp1, 41)
    logger.info(44)
    '\n        Reference: https://www.geeksforgeeks.org/python-program-for-radix-sort/\n    '
    logger.info(45)
    n = len(arr)
    aspAdliVarLog(n, 21)
    logger.info(46)
    output = [0] * n
    aspAdliVarLog(output, 22)
    logger.info(47)
    count = [0] * 10
    aspAdliVarLog(count, 23)
    logger.info(48)
    for i in range(0, n):
        aspAdliVarLog(i, 27)
        logger.info(49)
        index = arr[i] / exp1
        aspAdliVarLog(index, 24)
        asp_temp_var_6164713c09f011f09997b14cf8cd16f4 = int(index % 10)
        aspAdliVarLog(asp_temp_var_6164713c09f011f09997b14cf8cd16f4, 25)
        logger.info(50)
        count[asp_temp_var_6164713c09f011f09997b14cf8cd16f4] += 1
        aspAdliVarLog(count[asp_temp_var_6164713c09f011f09997b14cf8cd16f4], 26)
        logger.info(48)
    logger.info(51)
    for i in range(1, 10):
        aspAdliVarLog(i, 29)
        logger.info(52)
        count[i] += count[i - 1]
        aspAdliVarLog(count[i], 28)
        logger.info(51)
    logger.info(53)
    i = n - 1
    aspAdliVarLog(i, 30)
    logger.info(54)
    while i >= 0:
        logger.info(55)
        index = arr[i] / exp1
        aspAdliVarLog(index, 31)
        asp_temp_var_6164713d09f011f09997b14cf8cd16f4 = count[int(index % 10)] - 1
        aspAdliVarLog(asp_temp_var_6164713d09f011f09997b14cf8cd16f4, 32)
        logger.info(56)
        output[asp_temp_var_6164713d09f011f09997b14cf8cd16f4] = arr[i]
        aspAdliVarLog(output[asp_temp_var_6164713d09f011f09997b14cf8cd16f4], 33)
        asp_temp_var_6164713e09f011f09997b14cf8cd16f4 = int(index % 10)
        aspAdliVarLog(asp_temp_var_6164713e09f011f09997b14cf8cd16f4, 34)
        logger.info(57)
        count[asp_temp_var_6164713e09f011f09997b14cf8cd16f4] -= 1
        aspAdliVarLog(count[asp_temp_var_6164713e09f011f09997b14cf8cd16f4], 35)
        logger.info(58)
        i -= 1
        aspAdliVarLog(i, 36)
        logger.info(54)
    logger.info(59)
    i = 0
    aspAdliVarLog(i, 37)
    logger.info(60)
    for i in range(0, len(arr)):
        aspAdliVarLog(i, 39)
        logger.info(61)
        arr[i] = output[i]
        aspAdliVarLog(arr[i], 38)
        logger.info(60)

def radixSort(arr):
    logger.info(62)
    aspAdliVarLog(arr, 45)
    logger.info(63)
    '\n        Reference: https://www.geeksforgeeks.org/python-program-for-radix-sort/\n    '
    logger.info(64)
    max1 = max(arr)
    aspAdliVarLog(max1, 42)
    logger.info(65)
    exp = 1
    aspAdliVarLog(exp, 43)
    logger.info(66)
    while max1 // exp > 0:
        logger.info(67)
        countingSort(arr, exp)
        logger.info(68)
        exp *= 10
        aspAdliVarLog(exp, 44)
        logger.info(66)
    logger.info(69)
    return arr