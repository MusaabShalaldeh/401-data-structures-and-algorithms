# Singly Linked List

Singly Linked List is a dynamic data structure where each element (called a node) is made up of two items: the data and a reference (or pointer), which points to the next node.

## Challenge

Creating a single linked list with few methods to compliment its usage.

## Approach & Efficiency

***Cost of accessing an element: O(n)***

***Cost of inserting an element to the beginning of the list: O(n)***

***Cost of inserting an element to the end of the list: O(n)***

***Cost of appending an element to the end of the list: O(n)***

***Cost of inserting an element before a specified value in the list: O(n)***

***Cost of inserting an element after a specified value in the list: O(n)***

## API


    insert method
    ```
        Insert creates a Node with the value that was passed and adds
        it to the head of the linked list shifting all other values down

        arguments:
        value : any

        returns: None
    ```

    includes Method
    ```
        Check weather a value exists in a list instance

        arguments:
        value : any

        returns: True/False
    ```


    __str__ Method
    ```
        Returns a string containing all elements that exist within the list, if none it will return NULL only.

        Example: 
        "{ 29 } -> { 9 } -> { 5 } -> { 0 } -> NULL"

        arguments:
        None

        returns: String
    ```


    append Methpd
    ```
    Adds a value to the end of the linked list
    ```

    insert_before Method
    ```
    Insert a given value before a specificed value in the linked list.
    ```


    insert_after Method
    ```
    Insert a given value after a specificed value in the linked list.
    ```