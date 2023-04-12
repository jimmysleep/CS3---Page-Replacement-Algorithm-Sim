# Written by: James Lankester
# Student Number: LNKJAM001
# Course: CSC3002F

import sys
import random

def generate_pages(n):
    return [random.randint(0, 9) for _ in range(n)]


def main():
    #...TODO...
    size = int(sys.argv[1])
    print('FIFO', FIFO(size,pages), "page faults.")
    print ('LRU', LRU(size,pages),  "page faults.")
    print ('OPT', OPT(size,pages), "page faults.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python paging.py [number of page frames]')
    else:
        main()
