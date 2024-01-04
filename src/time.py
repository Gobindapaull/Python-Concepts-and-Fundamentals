import time

def other_fun():
    time.sleep(1)

def time_cal():
    t1 = time.time()
    other_fun()
    t2 = time.time() - t1
    print(t2)

time_cal()
