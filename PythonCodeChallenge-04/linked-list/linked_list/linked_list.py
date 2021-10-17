class Node:
    """
    A class represting a Node.

    Data and other attributes:

    data: Any type of valid data

    _next: Next Node
    """
    def __init__(self,data, _next = None):
        self.data = data
        self._next = _next
        pass

class LinkedList:
    """
    A class for creating instances of a Linked List.
  
    Data and other attributes defined here:
  
    head: Node | None

    Methods defined here

    insert(value: any)
    contains(value: any) -> bool
    """
    def __init__(self):
        self.head = None

    def insert(self, value):
        """"
        Insert creates a Node with the value that was passed and adds
        it to the head of the linked list shifting all other values down

        arguments:
        value : any

        returns: None
        """
        self.head = Node(value, self.head)

    def includes(self,val):
        """"
        Check weather a value exists in a list instance

        arguments:
        value : any

        returns: True/False
        """
        current = self.head
        while(True):
            if current.data == val:
                return True
            elif current.data != val and current._next == None:
                return False
            else:
                current = current._next

    def to_string(self):
        """"
        Returns a string containing all elements that exist within the list, if none it will return NULL only.

        Example: 
        "{ 29 } -> { 9 } -> { 5 } -> { 0 } -> NULL"

        arguments:
        None

        returns: String
        """
        current = self.head
        full_string = ''
        while(current != None):
            if(current._next == None):
                full_string += "{ "+str(current.data)+" } -> NULL"
                return full_string
            else:
                full_string += "{ "+str(current.data)+" } -> "
                current = current._next

            
        return "NULL"