from collections import deque
from queue import Queue, Empty
# dequeue / queue is preferred over lists where pop operations are O(1) here vs O(n) for a list. 
# Looks like the queue is a linked list, but with the easy workings of a python list.

# FIFO rule is followed here. 
# Disadvantage - We can't actually process middle elements like a list. 


def example_dequeue_from_geeks():
    q = deque() 
    q.append('a')
    q.append('b')
    q.append('c')
    print(f"before dequeing {q}")

    print(q.popleft())
    print(q.popleft())
    print(f"after two pops {q}")
    print(q.popleft())
    

def queue_example_geeks():
    q = Queue(maxsize=3)
    print(q.qsize())
    q.put('a')
    q.put('b')
    print("\nFull: ", q.full())
    
    # Now removing the elemets from the queue
    print(q.get())
    print(q.get())
    try:
        print(q.get_nowait()) # Error here?
    except Empty:
        print("Got the empty error as expected")
    print(q.get()) # Expect the pause here?


if __name__ == "__main__":
    example_dequeue_from_geeks()
    queue_example_geeks()
