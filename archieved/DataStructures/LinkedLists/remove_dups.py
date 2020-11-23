from linked_list import LinkedList
from linked_list import Node

def remove_dups(linked_list):
    already_occured = []

    n = linked_list.head
    p = None
    while n.next is not None:
        if n.name in already_occured:
            p.next = n.next
        else:
            already_occured.append(n.name)
        p = n
        n = n.next

    return linked_list

if __name__ == "__main__":

    my_list = LinkedList(None)
    last_node = None

    for i in ["1", "2", "1", "3", "4", "5"]:
        node = Node(i)

        if last_node is None:
            my_list.head = node
        else:
            last_node.next = node

        last_node = node

    print(remove_dups(my_list))
