class Node:
    def __init__(self, data):
        self.data = data
        self.next = Noneclass LinkedList:
    def __init__(self):
        self.head = Nonedef insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def find_nth_element_from_last(self, n):
        first_pointer = self.head
        second_pointer = self.head
        for i in range(n):
            if second_pointer is None:
                return None
            second_pointer = second_pointer.nextwhile second_pointer:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.nextreturn first_pointer.data
linked_list = LinkedList()
linked_list.insert_at_end(1)
linked_list.insert_at_end(2)
linked_list.insert_at_end(3)
linked_list.insert_at_end(4)
linked_list.insert_at_end(5)
result = linked_list.find_nth_element_from_last(3)
print(result)
