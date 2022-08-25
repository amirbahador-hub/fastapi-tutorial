import time

def timer(func):
    def wrapper():
        before = time.time()
        func()
        print(f"{ time.time() - before} sec")

def wait_for_10_sec(start):
    time.sleep(10)
    end = time.time()
    print(f"Normal   ==> {end - start}")

#@timer
def main():
    start = time.time()
    wait_for_10_sec(start)
    wait_for_10_sec(start)
    wait_for_10_sec(start)

if __name__ == "__main__":
    main()
