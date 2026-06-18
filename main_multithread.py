import threading


lock = threading.Lock()

def thread1():
    l = []
    for i in range(30):
        l.append(i)

    with lock:
        for i in range(30):
            print('thread1',i)

def thread2():
    with lock:    
        for i in range(30):
            print('thread2',i)


def main():
    th1 = threading.Thread(target=thread1)
    th2 = threading.Thread(target=thread2)
    th1.start()
    th2.start()

    th1.join()
    th2.join()
    
    print("La fin du code ")

if __name__=='__main__':
    main()
