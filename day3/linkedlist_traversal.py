class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def traverse(head):
    """Return a list of node values from head to tail."""
    result = []
    cur = head
    while cur:
        result.append(cur.data)
        cur = cur.next
    return result

if __name__ == "__main__":
    # Example list: 1 -> 2 -> 3
    head = Node(1, Node(2, Node(3)))
    print('Traversal:', traverse(head))
