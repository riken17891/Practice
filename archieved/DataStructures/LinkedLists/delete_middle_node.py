from linked_list import LinkedList
from linked_list import Node
from linked_list import generate_sample_list

def delete_middle_node(linked_list):
    c = r = linked_list.head
    p = None

    while r:
        r = r.next

        if r:
            r = r.next
            p = c
            c = c.next

    p.next = c.next

    return linked_list

if __name__ == "__main__":
    my_list = generate_sample_list(["a", "b", "c", "d", "e", "f", "g", "h", "i"])
    print(delete_middle_node(my_list))
