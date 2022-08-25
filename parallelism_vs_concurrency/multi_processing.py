import multiprocessing as mp
import time

def wait_for_10_sec(start):
    time.sleep(10)
    end = time.time()
    print(f"Normal   ==> {end - start}")


def main():
    start = time.time()
    p1 = mp.Process(target=wait_for_10_sec, args=(start,) )
    p2 = mp.Process(target=wait_for_10_sec, args=(start,) )
    p3 = mp.Process(target=wait_for_10_sec, args=(start,) )

    p1.start()
    p2.start()
    p3.start()

if __name__ == "__main__":
    main()

