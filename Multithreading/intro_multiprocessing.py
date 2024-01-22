#python
import time
from multiprocessing import Process


"""
start , do something and finish
"""

start = time.perf_counter()
print(f"Start time : {start}")

def do_somthing(sec):
    print("Sleeping for {} seconds(s)".format(sec))
    time.sleep(sec)
    print("Fininshed Sleeping")

p1 = Process(target=do_somthing)
p2 = Process(target=do_somthing)

#Basicall you are calling function

# WHen calling function with paranthesis, return values is added to a process

processes = []
for _ in range(10):
    p = Process(target=do_somthing,args=[0.000001])
    p.start()
    processes.append(p)

for process in processes:
    process.join()

# do_somthing()
# do_somthing()

finish = time.perf_counter()
print(f"Finish time : {finish}")



print(f"Total time take to run the program is {round(finish - start,4)} seconds(s)")