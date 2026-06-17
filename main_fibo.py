import fibo as fb
import pprint
from pprint import pprint
from fibo import fib2 as f2
import sys


def fib2(a):
    print("local fib2",a)

def main():
    params = sys.argv
    print(params)
    last_param = int(params[-1])
    fb.fib(last_param )

    pprint([])
    r = f2(12)

if __name__=='__main__':
    main()


