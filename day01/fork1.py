import os
import time


ret_val = os.fork()


if ret_val:
    print("in parent")
    time.sleep(10)
    print("parent exit")
else:
    for i in range(11):
        print(time.strftime("%H:%M:%S",time.localtime(time.time())))
        time.sleep(1)
    print("child exit")
