import threading as tr
import time

def wait_for_10_sec(start):
    time.sleep(10)
    end = time.time()
    print(f"Normal   ==> {end - start}")


def main():
    start = time.time()
    t1 = tr.Thread(target=wait_for_10_sec, args=(start,) )
    t2 = tr.Thread(target=wait_for_10_sec, args=(start,) )
    t3 = tr.Thread(target=wait_for_10_sec, args=(start,) )

    t1.start()
    t2.start()
    t3.start()

if __name__ == "__main__":
    main()

