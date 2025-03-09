import sqlite3
import atexit
from apscheduler.schedulers.background import BackgroundScheduler


def exit_handler():
    '''
        Close the database connection on exit.
    '''
    global conn, cursor, sched
    print("Shutting down compressor.")
    conn.commit()
    conn.close()
    sched.shutdown()

def getFirstNEntries():
    '''
        Get the first N entries from the database.
    '''
    statement = '''SELECT * from tempdata LIMIT 3'''
    cursor.execute(statement) 
    entries = cursor.fetchall() 
    return entries

def getNumberOfEntries():
    '''
        Get the number of entries in the database.
    '''
    statement = '''SELECT Count(*) from tempdata'''
    cursor.execute(statement) 
    output = cursor.fetchall() 
    numEntries = output[0][0]
    return numEntries

def compress():
    count = getNumberOfEntries()

    if count > 3:
        entries = getFirstNEntries()
        print(entries)
        
def main():
    '''
        Runs the main loop.
    '''
    global conn, cursor, sched
    conn = sqlite3.connect("../data.db", check_same_thread=False)
    cursor = conn.cursor()

    getFirstNEntries()

    sched = BackgroundScheduler()
    sched.add_job(compress, 'interval', seconds=5)
    sched.start()

    while(True):
        pass

if __name__ == "__main__":
    atexit.register(exit_handler)
    main()