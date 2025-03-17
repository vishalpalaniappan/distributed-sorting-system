
import websockets
import asyncio
import json

connection = websockets.connect(uri='ws://localhost:8765')

MSG_TYPE = {
    "CONNECT": 1,
    "REQUEST": 2,
    "RESPONSE": 3
}

def merge(arr, l, m, r):
    '''
        Reference: https://www.geeksforgeeks.org/python-program-for-merge-sort/
    '''
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, l, r):
    '''
        Reference: https://www.geeksforgeeks.org/python-program-for-merge-sort/
    '''
    if l < r:

        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

    return arr


async def main():
    async with connection as websocket:
        await websocket.send('{"code": 1, "worker": true, "type": "mergeSort"}')

        async for message in websocket:
            message = json.loads(message)

            if message["code"] == MSG_TYPE["CONNECT"]:
                global IS_REGISTERED
                IS_REGISTERED = True
            else:
                print(f"Task: {message['type']}, Value:{message['data']}")
                n = len(message["data"])
                resp = {
                    "code": MSG_TYPE["RESPONSE"],
                    "worker": True,
                    "type": "mergeSort",
                    "value": mergeSort(message["data"], 0, n-1)
                }
                await websocket.send(json.dumps(resp))
            
        await websocket.close()

asyncio.run(main())