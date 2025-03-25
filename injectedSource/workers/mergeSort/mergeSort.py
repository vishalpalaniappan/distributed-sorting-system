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
    logger.info(46)
    aspAdliVarLog(arr, 44)
    aspAdliVarLog(l, 45)
    aspAdliVarLog(m, 46)
    aspAdliVarLog(r, 47)
    logger.info(47)
    '\n        Reference: https://www.geeksforgeeks.org/python-program-for-merge-sort/\n    '
    logger.info(48)
    n1 = m - l + 1
    aspAdliVarLog(n1, 22)
    logger.info(49)
    n2 = r - m
    aspAdliVarLog(n2, 23)
    logger.info(50)
    L = [0] * n1
    aspAdliVarLog(L, 24)
    logger.info(51)
    R = [0] * n2
    aspAdliVarLog(R, 25)
    logger.info(52)
    for i in range(0, n1):
        aspAdliVarLog(i, 27)
        logger.info(53)
        L[i] = arr[l + i]
        aspAdliVarLog(L[i], 26)
        logger.info(52)
    logger.info(54)
    for j in range(0, n2):
        aspAdliVarLog(j, 29)
        logger.info(55)
        R[j] = arr[m + 1 + j]
        aspAdliVarLog(R[j], 28)
        logger.info(54)
    logger.info(56)
    i = 0
    aspAdliVarLog(i, 30)
    logger.info(57)
    j = 0
    aspAdliVarLog(j, 31)
    logger.info(58)
    k = l
    aspAdliVarLog(k, 32)
    logger.info(59)
    while i < n1 and j < n2:
        logger.info(60)
        if L[i] <= R[j]:
            logger.info(61)
            arr[k] = L[i]
            aspAdliVarLog(arr[k], 33)
            logger.info(62)
            i += 1
            aspAdliVarLog(i, 34)
        else:
            logger.info(63)
            arr[k] = R[j]
            aspAdliVarLog(arr[k], 35)
            logger.info(64)
            j += 1
            aspAdliVarLog(j, 36)
        logger.info(65)
        k += 1
        aspAdliVarLog(k, 37)
        logger.info(59)
    logger.info(66)
    while i < n1:
        logger.info(67)
        arr[k] = L[i]
        aspAdliVarLog(arr[k], 38)
        logger.info(68)
        i += 1
        aspAdliVarLog(i, 39)
        logger.info(69)
        k += 1
        aspAdliVarLog(k, 40)
        logger.info(66)
    logger.info(70)
    while j < n2:
        logger.info(71)
        arr[k] = R[j]
        aspAdliVarLog(arr[k], 41)
        logger.info(72)
        j += 1
        aspAdliVarLog(j, 42)
        logger.info(73)
        k += 1
        aspAdliVarLog(k, 43)
        logger.info(70)

def mergeSort(arr, l, r):
    logger.info(74)
    aspAdliVarLog(arr, 49)
    aspAdliVarLog(l, 50)
    aspAdliVarLog(r, 51)
    logger.info(75)
    '\n        Reference: https://www.geeksforgeeks.org/python-program-for-merge-sort/\n    '
    logger.info(76)
    if l < r:
        logger.info(77)
        m = l + (r - l) // 2
        aspAdliVarLog(m, 48)
        logger.info(78)
        mergeSort(arr, l, m)
        logger.info(79)
        mergeSort(arr, m + 1, r)
        logger.info(80)
        merge(arr, l, m, r)
    logger.info(81)
    return arr