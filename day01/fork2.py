import os

for i in range(1000):
    ret_val = os.fork()
    if not ret_val:
        print("Hello world!")
        exit()

