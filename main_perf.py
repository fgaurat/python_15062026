import timeit

def init_loop():
    r = []
    for i in range(100):
        r.append(i)

def init_map():
    r = list(map(lambda i:i,range(100)))

def init_comp():
    r = [i for i in range(100)]    


def main():
    loop_time = timeit.timeit(init_loop)
    map_time = timeit.timeit(init_map)
    comp_time = timeit.timeit(init_comp)

    print(f"Loop time: {loop_time:.6f} seconds")
    print(f"Map time: {map_time:.6f} seconds")
    print(f"Comprehension time: {comp_time:.6f} seconds")


if __name__=='__main__':
    main()

