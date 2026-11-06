import multiprocessing

def compute():
    count = 0

    for _ in range(10**8):
        count = count + 1

    print("Count: " , count)

if __name__ == "__main__":
    '''compute()
    compute()
    compute()
    '''

    processes = [multiprocessing.Process(target = compute) for _ in range(3)]
    
    for process in processes:
        process.start()

    for process in processes:
            process.join()
    
