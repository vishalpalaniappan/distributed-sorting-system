import sqlite3
import atexit
import time
import json
import gzip
import os
import math
from apscheduler.schedulers.background import BackgroundScheduler

COMPRESS_THRESHOLD = 30

def exit_handler():
    '''
        Close the database connection on exit.
    '''
    global conn, sched, cursor
    print("Shutting down compressor.")
    conn.commit()
    conn.close()
    sched.shutdown()


def deleteFirstNEntries(N):
    '''
        Deletes the first N entries from the database.
    '''
    global conn, cursor
    
    statement = "DELETE FROM tempdata LIMIT " + str(N)
    cursor.execute(statement) 
    conn.commit()

def getFirstNEntries(N):
    '''
        Get the first N entries from the database.
    '''
    global conn, cursor

    statement = "SELECT * from tempdata LIMIT " + str(N)
    cursor.execute(statement) 
    conn.commit()
    entries = cursor.fetchall() 

    return entries

def getNumberOfEntries():
    '''
        Get the number of entries in the database.
    '''
    global conn, cursor

    statement = '''SELECT Count(*) from tempdata'''
    cursor.execute(statement) 
    conn.commit()

    output = cursor.fetchall()     
    numEntries = output[0][0]

    return numEntries

def compress():
    '''
        Scheduled job to compress data when number of 
        entries reaches a threshold.
    '''
    count = getNumberOfEntries()
    print("Number of Entries:", count)

    if count >= COMPRESS_THRESHOLD:
        entries = getFirstNEntries(COMPRESS_THRESHOLD)

        # Compression Files
        startTs = round(float(entries[0][0].replace('"', "")))
        fileName = "../compressed_data/" + str(startTs) + ".gz"

        with gzip.open(fileName, 'wb') as f:
            f.write(json.dumps(entries).encode())
            
        deleteFirstNEntries(COMPRESS_THRESHOLD)
        
def main():
    '''
        Runs the main loop.
    '''
    if (not os.path.exists("../compressed_data/")):
        os.mkdir("../compressed_data/")

    global conn, sched, cursor
    conn = sqlite3.connect("../data.db", check_same_thread=False)
    cursor = conn.cursor()

    sched = BackgroundScheduler(standalone=True)
    sched.add_job(compress, 'interval', seconds=1)
    sched.start()

    while True:
        time.sleep(5)

if __name__ == "__main__":
    atexit.register(exit_handler)
    main()