from stack_and_queue.node import Node

class Stack:
    """
    Class: Stack

    """
    def __init__(self):
        self.top = None

    def push(self,value):
        if self.top == None:
            self.top = Node(value)
        else:
            self.top = Node(value,self.top)

    def pop(self):
        if(self.top != None):
            last_top = self.top.value
            if self.top.next != None:
                self.top = self.top.next
                return last_top
            else:
                self.top = None
                return last_top
        else:
            raise EmptyStack("Errour encounted....Stack is empty.")

    def peek(self):
        return self.top.value

    def is_empty(self):
        if self.top == None:
            return True
        return False




class EmptyStack(Exception):
    pass