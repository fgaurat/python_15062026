import os
from multiprocessing import Pool
import time

def f(x):
    t = 2
    start = time.time()
    while time.time()-start<t:
        pass
    return x*x




def main():
    print("cpu_count",os.cpu_count())

    with Pool(2) as p:
        print(p.map(f,range(100)))

if __name__=='__main__':
    main()
