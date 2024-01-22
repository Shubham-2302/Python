import concurrent.futures
import time
import random
start = time.perf_counter()


def do_somthing(sec):
    print("Sleeping for {} seconds(s)".format(sec))
    time.sleep(sec)
    return f"Fininshed Sleeping {sec}"


#With context Manager

with concurrent.futures.ProcessPoolExecutor() as executor:
    seconds = [5,4,7,6,3,3,2,1,2,3,4,5]
    # results = executor.map(do_somthing,seconds)

    # for result in results:
    #     print(result)

    results = [executor.submit(do_somthing,sec) for sec in seconds]


    for f in concurrent.futures.as_completed(results):
        print(f.result())


finish = time.perf_counter()
print(f"Finish time : {finish}")



print(f"Total time take to run the program is {round(finish - start,4)} seconds(s)")