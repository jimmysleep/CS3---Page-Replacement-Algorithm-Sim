Page Replacement Algorithms
This project includes three different page replacement algorithms: FIFO, LRU, and OPT. These algorithms simulate how a computer's operating system handles memory allocation for running programs. The project is written in Python and includes a program paging.py that demonstrates the algorithms in action.

Usage
To use the program, run python paging.py [number of page frames] in the command line, where [number of page frames] is the number of pages that can be held in memory at a given time.

The program generates a list of 256 random page references (this can be changed) and uses each of the three algorithms to simulate how they would handle the page references. The output of the program includes the number of page faults for each algorithm.

Page Replacement Algorithms
FIFO
The FIFO algorithm is a simple page replacement algorithm that evicts the oldest page in memory when a new page is loaded and there is no space left in memory.

LRU
The LRU (least recently used) algorithm is a more sophisticated page replacement algorithm that evicts the page that has not been used for the longest time when a new page is loaded and there is no space left in memory.

OPT
The OPT (optimal) algorithm is the most efficient page replacement algorithm in theory. It evicts the page that will not be used for the longest time in the future when a new page is loaded and there is no space left in memory.

Contact
If you have any questions or suggestions, please contact James Lankester at lnkjam001@myuct.ac.za.