from Node import Node

#Stack Class
class Stack:
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.limit = 1000
        self.top_node = None
    
    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_node)
            self.top_node = item
            self.size += 1
        else:
            print("No room on the stack")


    def pop(self):
        if not self.is_empty():
            item_to_pop = self.top_node
            self.top_node = item_to_pop.get_next_node()
            self.size -= 1
            return item_to_pop.get_value()
        else:
            print("Nothing on the stack to POP")

    def peek(self):
        if not self.is_empty():
            return self.top_node.get_value()
        else:
            print("Nothing to Peek at!")

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def get_name(self):
        return self.name
    
    def listify_stack_values(self):
        pointer = self.top_node
        value_list = []
        while pointer:
            value_list.append(pointer.get_value())
            pointer = pointer.get_next_node()
        return value_list
