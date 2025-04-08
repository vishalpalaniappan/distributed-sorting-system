import subprocess
from pathlib import Path

processes = []

def stopProcess(path):
    '''
        Stops the process using the pm2 stop command.
    '''
    result = subprocess.run(["pm2", "delete", path])
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
        stopProcess(process)