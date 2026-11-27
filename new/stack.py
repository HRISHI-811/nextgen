stack = []
top = -1
def push(item):
    global top
    stack.append(item)
    top += 1
def pop():
    global top
    if top == -1:
        print("Stack Underflow")
        return None
    top -= 1
    return stack.pop()

def peek():
    if top == -1:
        print("Stack is Empty")
        return None
    return stack[top]
push(10)
push(20)
push(30)


print("Top Element:", peek())

print(pop())