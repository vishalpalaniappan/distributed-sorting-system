import subprocess
import time
from pathlib import Path

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

    rootDir = str(Path(__file__).resolve().parents[1])

    processes = [
        rootDir + "/jobHandler/jobHandler.py",
        rootDir + "/bubbleSortWorker/bubbleSortWorker.py",
        rootDir + "/radixSortWorker/radixSortWorker.py",
        rootDir + "/mergeSortWorker/mergeSortWorker.py",
        rootDir + "/simulatedClient/simulatedClient.py",
    ]

    for process in processes:
        startProcess(process)
