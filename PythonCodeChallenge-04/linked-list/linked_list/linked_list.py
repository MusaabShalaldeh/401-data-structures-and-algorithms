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
        
        if(current != None):
            while(True):
                if current.data == val:
                    return True
                elif current.data != val and current._next == None:
                    return False
                else:
                    current = current._next

    def __str__(self):
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

    def append(self,value):
        """
        Add a value to the end of the linked list, if none exists the value will be the head of the list.
        """
        current = self.head
        
        if(current != None):
            while(True):
                if current._next != None:
                    current = current._next
                else:
                    current._next = Node(value)
                    break
        else:
            self.head = Node(value)
    
    def insert_before(self,before_value,value):
        """
        Insert a given value before a specificed value in the linked list.
        """
        current = self.head

        if(current != None):
            while(True):
                if current._next == None:
                    if current.data == before_value:
                        self.head = Node(value,current)
                        break
                    else:
                        break
                elif current._next.data == before_value:
                    current._next = Node(value,current._next)
                    break
                else:
                    current = current._next
        else:
            self.head = Node(value)


    def insert_after(self,after_value,value):
        """
        Insert a given value after a specificed value in the linked list.
        """
        current = self.head

        if(current != None):
            while(True):
                if current._next == None:
                    if current.data == after_value:
                        current._next = Node(value,current._next)
                        break
                    else:
                        break
                elif current.data == after_value:
                    current._next = Node(value,current._next)
                    break
                else:
                    current = current._next

    def kthFromEnd(self,input):
        current = self.head

        if input == 1:
            return current.data
        elif(current != None and current._next != None and input > 0):
            count = 1
            second_pointer = [None]

            while(True):
                if count == input:
                    second_pointer[0] = current
                elif count - input == input:
                    second_pointer[0] = second_pointer[0]._next

                if current._next == None:
                    if(count < input):
                        return None
                    else:
                        return second_pointer[0].data
                else:
                    current = current._next
                    count += 1

        elif (current != None and current._next != None and input == 0):
            while(True):
                if current._next == None:
                    return current.data
                else:
                    current = current._next
        else:
            return None

    @staticmethod
    def zipLists(first_list,second_list):
        current = first_list.head

        if(current != None and second_list.head != None):
            newList = LinkedList()
            counter = 1
            while(True):
                if current._next == None and counter == 2:
                    newList.append(current.data)
                    return newList

                elif current._next == None and counter == 1:
                    newList.append(current.data)
                    counter = 2
                    current = second_list.head
                else:
                    newList.append(current.data)
                    current = current._next     
        else:
            raise Exception("One of the provided arguments does not meet the required type of data/ either linked list is empty...")  