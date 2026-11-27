queue = []
front = -1
rear = -1

def enqueue(item):
    global front, rear
    if front == -1:
        front = 0
    queue.append(item)
    rear += 1
def dequeue():
    global front, rear
    if front == -1 or front > rear:
        print("Queue Underflow")
        return
    item = queue[front]
    front += 1
    if front > rear:
        front = rear = -1
    return item

enqueue(10)
enqueue(20)
enqueue(30)


dequeue()