import sqlite3
import atexit
import time
from apscheduler.schedulers.background import BackgroundScheduler


def exit_handler():
    '''
        Close the database connection on exit.
    '''
    global conn, cursor
    print("Shutting down compressor.")
    conn.commit()
    conn.close()

def getFirstNEntries():
    '''
        Get the first N entries from the database.
    '''
    global conn, cursor

    statement = '''SELECT * from tempdata LIMIT 3'''
    cursor.execute(statement) 
    entries = cursor.fetchall() 
    
    statement = '''DELETE FROM tempdata LIMIT 3'''
    cursor.execute(statement) 
    conn.commit()

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
    count = getNumberOfEntries()
    print("COUNT:", count)

    if count > 3:
        entries = getFirstNEntries()
        print(entries)
        
def main():
    '''
        Runs the main loop.
    '''
    global conn, sched, cursor
    conn = sqlite3.connect("../data.db", check_same_thread=False)
    cursor = conn.cursor()

    sched = BackgroundScheduler(standalone=True)
    sched.add_job(compress, 'interval', seconds=5)
    sched.start()

    while True:
        time.sleep(5)

if __name__ == "__main__":
    atexit.register(exit_handler)
    main()