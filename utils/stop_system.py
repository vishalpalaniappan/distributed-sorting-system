import subprocess
from pathlib import Path

'''
{
    "type": "adli_metadata",
    "name": "Stop Distributed Sorting System",
    "description": "Uses PM2 to stop each program in system.",
    "version": "0.0",
    "language": "python"
}
'''

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