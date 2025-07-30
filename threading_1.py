import threading
import time
import sys

def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print (threadName, time.ctime(time.time()))

try:
    t1 = threading.Thread(target = print_time, args = ("Thread-1", 2,))
    t2 = threading.Thread(target = print_time, args = ("Thread-2", 4,))

    t1.start()
    t2.start()
except KeyboardInterrupt:
    print("Interrupted by user. Exiting...")
    t1.join()
    t2.join()
    sys.exit()
except:
    print("Errror: Unable to start thread")

