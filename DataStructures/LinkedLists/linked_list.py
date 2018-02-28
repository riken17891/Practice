

class LinkedList:
    def __init__(self, head):
        self.head = head

    def __str__(self):
        n = self.head
        s = ""
        while n is not None:
            s = s + n.name + " -> "
            n = n.next

        return s

class Node:
    def __init__(self, name, next=None):
        self.name = name
        self.next = next

    def __str__(self):
        n = self
        s = ""
        while n is not None:
            s = s + n.name + " -> "
            n = n.next

        return s

def generate_sample_list(items):
    my_list = LinkedList(None)
    last_node = None

    for i in items:
        node = Node(i)

        if last_node is None:
            my_list.head = node
        else:
            last_node.next = node

        last_node = node

    return my_list
