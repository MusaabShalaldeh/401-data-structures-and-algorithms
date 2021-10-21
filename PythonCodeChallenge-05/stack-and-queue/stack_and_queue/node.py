class Node:
    """
    Class: Code
    A class that respresnts an object which contains its own value and a pointer to the next object in line.

    Arguments: Value
    returns: None
    """
    def __init__(self,value,next=None):
        self.value = value
        self.next = next