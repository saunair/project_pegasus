from threading import Thread
from collections import deque
from queue import Queue, Empty
# dequeue / queue is preferred over lists where pop operations are O(1) here vs O(n) for a list. 
# Looks like the queue is a linked list, but with the easy workings of a python list.

# FIFO rule is followed here. 
# Disadvantage - We can't actually process middle elements like a list. 


# Dequeue is just a data-structure. Queue is a tool of sorts build on top of dequeue.
# Queue shouldn't be used as a collection. It must be used for communication between different threads etc.
# If we have multiple threads accessing the same queue, we should use a Queue as it is threadsafe and we wouldn't need any locking whatsoever.

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



def square_the_number(number):
    return number ** 2


def execute_queue_actions(action_queue):
    while True:
        number = action_queue.get()
        print(square_the_number(number))
        action_queue.task_done()


def threading_example():
    action_queue = Queue()
    Thread(target=execute_queue_actions, daemon=True, args=(action_queue, )).start()
    for number in range(10):
        action_queue.put(number)

    action_queue.put(100)
    action_queue.join()
    print("Done with all the tasks")
     

if __name__ == "__main__":
    example_dequeue_from_geeks()
    threading_example()
    queue_example_geeks()
