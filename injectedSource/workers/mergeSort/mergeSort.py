import logging
import json
logger = logging.getLogger('adli')

def aspAdliVarLog(val, varid):
    try:
        val = json.dumps(val, default=lambda o: o.__dict__)
    except:
        pass
    logger.info(f'# {varid} {val}')

def merge(arr, l, m, r):
    logger.info(47)
    aspAdliVarLog(arr, 44)
    aspAdliVarLog(l, 45)
    aspAdliVarLog(m, 46)
    aspAdliVarLog(r, 47)
    logger.info(48)
    '\n        Reference: https://www.geeksforgeeks.org/python-program-for-merge-sort/\n    '
    logger.info(49)
    n1 = m - l + 1
    aspAdliVarLog(n1, 22)
    logger.info(50)
    n2 = r - m
    aspAdliVarLog(n2, 23)
    logger.info(51)
    L = [0] * n1
    aspAdliVarLog(L, 24)
    logger.info(52)
    R = [0] * n2
    aspAdliVarLog(R, 25)
    logger.info(53)
    for i in range(0, n1):
        aspAdliVarLog(i, 27)
        logger.info(54)
        L[i] = arr[l + i]
        aspAdliVarLog(L[i], 26)
        logger.info(53)
    logger.info(55)
    for j in range(0, n2):
        aspAdliVarLog(j, 29)
        logger.info(56)
        R[j] = arr[m + 1 + j]
        aspAdliVarLog(R[j], 28)
        logger.info(55)
    logger.info(57)
    i = 0
    aspAdliVarLog(i, 30)
    logger.info(58)
    j = 0
    aspAdliVarLog(j, 31)
    logger.info(59)
    k = l
    aspAdliVarLog(k, 32)
    logger.info(60)
    while i < n1 and j < n2:
        logger.info(61)
        if L[i] <= R[j]:
            logger.info(62)
            arr[k] = L[i]
            aspAdliVarLog(arr[k], 33)
            logger.info(63)
            i += 1
            aspAdliVarLog(i, 34)
        else:
            logger.info(64)
            arr[k] = R[j]
            aspAdliVarLog(arr[k], 35)
            logger.info(65)
            j += 1
            aspAdliVarLog(j, 36)
        logger.info(66)
        k += 1
        aspAdliVarLog(k, 37)
        logger.info(60)
    logger.info(67)
    while i < n1:
        logger.info(68)
        arr[k] = L[i]
        aspAdliVarLog(arr[k], 38)
        logger.info(69)
        i += 1
        aspAdliVarLog(i, 39)
        logger.info(70)
        k += 1
        aspAdliVarLog(k, 40)
        logger.info(67)
    logger.info(71)
    while j < n2:
        logger.info(72)
        arr[k] = R[j]
        aspAdliVarLog(arr[k], 41)
        logger.info(73)
        j += 1
        aspAdliVarLog(j, 42)
        logger.info(74)
        k += 1
        aspAdliVarLog(k, 43)
        logger.info(71)

def mergeSort(arr, l, r):
    logger.info(75)
    aspAdliVarLog(arr, 49)
    aspAdliVarLog(l, 50)
    aspAdliVarLog(r, 51)
    logger.info(76)
    '\n        Reference: https://www.geeksforgeeks.org/python-program-for-merge-sort/\n    '
    logger.info(77)
    if l < r:
        logger.info(78)
        m = l + (r - l) // 2
        aspAdliVarLog(m, 48)
        logger.info(79)
        mergeSort(arr, l, m)
        logger.info(80)
        mergeSort(arr, m + 1, r)
        logger.info(81)
        merge(arr, l, m, r)
    logger.info(82)
    return arr