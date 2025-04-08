import subprocess
import time

processes = []

def startProcess(path):
    '''
        Starts the processes and sleeps briefly. The websocket server has to be open
        before the client and workers can connect to it, so I added some delay. 
    '''
    result = subprocess.run(["pm2", "start", path, "--interpreter", "/usr/bin/python3"])
    time.sleep(0.5)
    print(result)


if __name__ == "__main__":

    processes = [
        "./jobHandler/jobHandler.py",
        "./workers/bubbleSort/bubbleSortWorker.py",
        "./workers/radixSort/radixSortWorker.py",
        "./workers/mergeSort/mergeSortWorker.py",
        "./simulatedClient/simulatedClient.py",
    ]

    for process in processes:
        startProcess(process)
