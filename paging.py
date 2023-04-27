# Written by: James Lankester
# Student Number: LNKJAM001
# Course: CSC3002F

import sys
import random

def FIFO(size, pages):
    page_faults = 0 
    memory = []
    # loop through the page references
    for page in pages:
        # if the requested page isn't already in memory
        if page not in memory:
            # if there is still available space in memory
            if len(memory) < size:
                # add page to memory
                memory.append(page)
            # if the memory is full               
            else:
                # remove the page at the front of the queue
                memory.pop(0)
                # add the latest page to the back of the queue
                memory.append(page)
            page_faults += 1

    return page_faults

# LRU page replacement algorithm
def LRU(size, pages):
    queue = []
    page_faults = 0
    for page in pages:
        if page in queue:
            # remove the page to put it at the end (most recent)
            queue.remove(page)
        else:
            page_faults += 1
            if len(queue) == size:
                # take the first page (least recently used) off the queue
                queue.pop(0)
        # append the page
        # This will be the same one that was just accessed, or the one that was just loaded in 
        queue.append(page)
    return page_faults


# Optimal page replacement algorithm implementation in python
# Define a function named OPT2 which takes two parameters: size and pages
def OPT2(size, pages):
    # Initialize an empty list named queue to store the frames currently in memory
    queue = []
    # Initialize a variable named page_faults to track the number of page faults that occur during the execution of the function
    page_faults = 0
    # Initialize a null list to keep track of when each page in queue will be used again in the future
    occurance = [None for i in range(size)]
    # Iterate through each page reference in the pages list
    for i in range(len(pages)):
        # If the page is not already in memory, check if there is space in memory for the page
        if pages[i] not in queue:
            # If there is space in memory, add the page to the queue
            if len(queue) < size:
                queue.append(pages[i])
            # If there is no space in memory 
            else:
                # find the page that will not be used for the longest time in the future
                for x in range(len(queue)):
                    if queue[x] not in pages[i+1:]:
                        #  and replace it with the current page
                        queue[x] = pages[i]
                        break
                    else:
                        occurance[x] = pages[i+1:].index(queue[x])
                else:
                    queue[occurance.index(max(occurance))] = pages[i]
            # Increment the page_faults variable by 1
            page_faults += 1
    # Return the value of the page_faults variable
    return page_faults

def generate_pages(n):
    random_pages = [random.randint(0, 9) for _ in range(n)]
    for page in random_pages:
        print(page, " ", sep='', end='')
    return random_pages
   
def main():
    # the number of pages that can be held in memory at a given time
    size = int(sys.argv[1])

    # a list of page numbers (references) being accessed by a program
    pages = generate_pages(32)
    print('\nFIFO', FIFO(size,pages), "page faults.")
    print ('LRU', LRU(size,pages),  "page faults.")
    print ('OPT', OPT2(size,pages), "page faults.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python paging.py [number of page frames]')
    else:
        main()
