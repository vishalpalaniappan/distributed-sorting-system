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

def merge(arr, l, m, r):
    logger.info(35)
    aspAdliVarLog(arr, 42)
    aspAdliVarLog(l, 43)
    aspAdliVarLog(m, 44)
    aspAdliVarLog(r, 45)
    logger.info(36)
    '\n        Reference: https://www.geeksforgeeks.org/python-program-for-merge-sort/\n    '
    logger.info(37)
    n1 = m - l + 1
    aspAdliVarLog(n1, 20)
    logger.info(38)
    n2 = r - m
    aspAdliVarLog(n2, 21)
    logger.info(39)
    L = [0] * n1
    aspAdliVarLog(L, 22)
    logger.info(40)
    R = [0] * n2
    aspAdliVarLog(R, 23)
    logger.info(41)
    for i in range(0, n1):
        aspAdliVarLog(i, 25)
        logger.info(42)
        L[i] = arr[l + i]
        aspAdliVarLog(L[i], 24)
        logger.info(41)
    logger.info(43)
    for j in range(0, n2):
        aspAdliVarLog(j, 27)
        logger.info(44)
        R[j] = arr[m + 1 + j]
        aspAdliVarLog(R[j], 26)
        logger.info(43)
    logger.info(45)
    i = 0
    aspAdliVarLog(i, 28)
    logger.info(46)
    j = 0
    aspAdliVarLog(j, 29)
    logger.info(47)
    k = l
    aspAdliVarLog(k, 30)
    logger.info(48)
    while i < n1 and j < n2:
        logger.info(49)
        if L[i] <= R[j]:
            logger.info(50)
            arr[k] = L[i]
            aspAdliVarLog(arr[k], 31)
            logger.info(51)
            i += 1
            aspAdliVarLog(i, 32)
        else:
            logger.info(52)
            arr[k] = R[j]
            aspAdliVarLog(arr[k], 33)
            logger.info(53)
            j += 1
            aspAdliVarLog(j, 34)
        logger.info(54)
        k += 1
        aspAdliVarLog(k, 35)
        logger.info(48)
    logger.info(55)
    while i < n1:
        logger.info(56)
        arr[k] = L[i]
        aspAdliVarLog(arr[k], 36)
        logger.info(57)
        i += 1
        aspAdliVarLog(i, 37)
        logger.info(58)
        k += 1
        aspAdliVarLog(k, 38)
        logger.info(55)
    logger.info(59)
    while j < n2:
        logger.info(60)
        arr[k] = R[j]
        aspAdliVarLog(arr[k], 39)
        logger.info(61)
        j += 1
        aspAdliVarLog(j, 40)
        logger.info(62)
        k += 1
        aspAdliVarLog(k, 41)
        logger.info(59)

def mergeSort(arr, l, r):
    logger.info(63)
    aspAdliVarLog(arr, 47)
    aspAdliVarLog(l, 48)
    aspAdliVarLog(r, 49)
    logger.info(64)
    '\n        Reference: https://www.geeksforgeeks.org/python-program-for-merge-sort/\n    '
    logger.info(65)
    if l < r:
        logger.info(66)
        m = l + (r - l) // 2
        aspAdliVarLog(m, 46)
        logger.info(67)
        mergeSort(arr, l, m)
        logger.info(68)
        mergeSort(arr, m + 1, r)
        logger.info(69)
        merge(arr, l, m, r)
    logger.info(70)
    return arr