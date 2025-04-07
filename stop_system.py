import subprocess

processes = []

def stopProcess(path):
    '''
        Stops the process using the pm2 stop command.
    '''
    result = subprocess.run(["pm2", "stop", path])
    print(result)


if __name__ == "__main__":

    processes = [
        "./jobHandler/jobHandler.py",
        "./simulatedClient/simulatedClient.py",
        "./workers/bubbleSort/bubbleSortWorker.py",
        "./workers/radixSort/radixSortWorker.py",
        "./workers/mergeSort/mergeSortWorker.py"
    ]
    
    for process in processes:
        stopProcess(process)