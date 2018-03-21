#!/usr/bin/env python

# from multiprocessing import Process


def sub1():
    for i in range(10 ** 8):
        continue
    print("i am sub1")


def sub2():
    for i in range(10 ** 7):
        continue
    print("i am sub2")


def run(sub):
    if sub == "sub1":
        sub1()

    else:
        sub2()


if __name__ == "__main__":
    sub1()
    sub2()
    # processes = list()
    # for name in ("sub1", "sub2"):
    #     p = Process(target=run, args=(name,))
    #     p.daemon = True
    #     processes.append(p)
    #     p.start()
    # for p in processes:
    #     p.join()
    #     # time.sleep(1)

    # time.sleep(5)
