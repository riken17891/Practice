from linked_list import LinkedList
from linked_list import Node
from linked_list import generate_sample_list

def kth_to_last(linked_list, i):
    c = n = linked_list.head

    for t in range(i):
        if n.next:
            n = n.next
        else:
            return None

    while n:
        c = c.next
        n = n.next

    return c

if __name__ == "__main__":
    my_list = generate_sample_list(["1", "2", "4", "5", "5", "6", "8", "9", "10", "11"])
    print(kth_to_last(my_list, 9))
