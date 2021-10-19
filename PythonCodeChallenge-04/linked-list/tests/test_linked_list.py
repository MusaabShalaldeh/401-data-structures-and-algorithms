from linked_list import __version__
from linked_list.linked_list import Node,  LinkedList
import pytest


def test_version():
    assert __version__ == '0.1.0'


def test_node_has_int_data():
    # Arrange any data that you need to run your test
    expected = 1

    # Act on the subject of the test to produce some actual output
    node = Node(1)
    actual = node.data

    # Assert
    assert actual == expected


def test_node_has_str_data():
    # Arrange any data that you need to run your test
    expected = "a"

    # Act on the subject of the test to produce some actual output
    node = Node("a")
    actual = node.data

    # Assert
    assert actual == expected


def test_node_is_a_Node():
    # Arrange any data that you need to run your test
    expected = "Node"

    # Act on the subject of the test to produce some actual output
    node = Node(1)
    actual = type(node).__name__

    # Assert
    assert actual == expected

def test_node_without_value():
  with pytest.raises(TypeError):
    node = Node()


def test_new_linked_list_is_empty():
  expected = None

  ll = LinkedList()
  actual = ll.head

  assert actual == expected

def test_linked_list_insert():
  # Arrange
  expected = 1
  ll = LinkedList()

  # Act
  ll.insert(1)
  node = ll.head
  actual = node.data

  # Assert
  assert actual == expected

def test_linked_list_insert_twice():
  # Arrange
  expected = 0
  ll = LinkedList()

  # Act
  ll.insert(1)
  ll.insert(0)
  node = ll.head
  actual = node.data

  # Assert
  assert actual == expected
  assert ll.head._next.data == 1


def test_linked_list_includes():
  # Arrange
  expected = True
  ll = LinkedList()

  # Act
  ll.insert(0)
  ll.insert(5)
  ll.insert(9)
  actual = ll.includes(5)

  # Assert
  assert actual == expected


def test_linked_list_includes_fail():
  # Arrange
  expected = False
  ll = LinkedList()

  # Act
  ll.insert(0)
  ll.insert(5)
  ll.insert(9)
  actual = ll.includes(20)

  # Assert
  assert actual == expected


def test_linked_list_includes_first_item():
  # Arrange
  expected = True
  ll = LinkedList()

  # Act
  ll.insert(0)
  ll.insert(5)
  ll.insert(9)
  actual = ll.includes(0)

  # Assert
  assert actual == expected


def test_linked_list_includes_last_item():
  # Arrange
  expected = True
  ll = LinkedList()

  # Act
  ll.insert(0)
  ll.insert(5)
  ll.insert(9)
  actual = ll.includes(9)

  # Assert
  assert actual == expected




def test_linked_list_to_string():
  # Arrange
  expected = "{ 29 } -> { 9 } -> { 5 } -> { 0 } -> NULL"
  ll = LinkedList()

  # Act
  ll.insert(0)
  ll.insert(5)
  ll.insert(9)
  ll.insert(29)
  actual = str(ll)

  # Assert
  assert actual == expected


def test_linked_empty_list_to_string():
  # Arrange
  expected = "NULL"
  ll = LinkedList()

  # Act
  actual = str(ll)

  # Assert
  assert actual == expected




def test_linked_list_append():
  # Arrange
  expected = "{ 9 } -> { 5 } -> { 0 } -> { 29 } -> NULL"
  ll = LinkedList()

  # Act
  ll.insert(0)
  ll.insert(5)
  ll.insert(9)
  ll.append(29)
  actual = str(ll)

  # Assert
  assert actual == expected


def test_linked_list_append_multi_values():
  # Arrange
  expected = "{ 0 } -> { 5 } -> { 9 } -> { 29 } -> NULL"
  ll = LinkedList()

  # Act
  ll.append(0)
  ll.append(5)
  ll.append(9)
  ll.append(29)
  actual = str(ll)

  # Assert
  assert actual == expected

def test_linked_list_append_empty():
  # Arrange
  expected = "{ 29 } -> NULL"
  ll = LinkedList()

  # Act
  ll.append(29)
  actual = str(ll)

  # Assert
  assert actual == expected


def test_linked_list_insert_before():
  # Arrange
  expected = "{ 9 } -> { 29 } -> { 5 } -> { 0 } -> NULL"
  ll = LinkedList()

  # Act
  ll.insert(0)
  ll.insert(5)
  ll.insert(9)
  ll.insert_before(5,29)
  actual = str(ll)

  # Assert
  assert actual == expected


def test_linked_list_insert_before_not_found():
  # Arrange
  expected = "{ 9 } -> { 7 } -> { 0 } -> NULL"
  ll = LinkedList()

  # Act
  ll.insert(0)
  ll.insert(7)
  ll.insert(9)
  ll.insert_before(5,29)
  actual = str(ll)

  # Assert
  assert actual == expected

def test_linked_list_insert_before_first():
  # Arrange
  expected = "{ 29 } -> { 1 } -> NULL"
  ll = LinkedList()

  # Act
  ll.insert(1)
  ll.insert_before(1,29)
  actual = str(ll)

  # Assert
  assert actual == expected



def test_linked_list_insert_after():
  # Arrange
  expected = "{ 9 } -> { 5 } -> { 25 } -> { 0 } -> NULL"
  ll = LinkedList()

  # Act
  ll.insert(0)
  ll.insert(5)
  ll.insert(9)
  ll.insert_after(5,25)
  actual = str(ll)

  # Assert
  assert actual == expected



def test_linked_list_insert_after_last():
  # Arrange
  expected = "{ 9 } -> { 5 } -> { 0 } -> { 25 } -> NULL"
  ll = LinkedList()

  # Act
  ll.insert(0)
  ll.insert(5)
  ll.insert(9)
  ll.insert_after(0,25)
  actual = str(ll)

  # Assert
  assert actual == expected


def test_linked_list_kth():
  #Arrange
  expected = 8
  ll = LinkedList()

  #Actual
  ll.insert(2)
  ll.insert(8)
  ll.insert(3)
  ll.insert(1)

  actual = ll.kthFromEnd(3)

  # Assert
  assert actual == expected

def test_second_linked_list_kth():
  #Arrange
  expected = 2
  ll = LinkedList()

  #Actual
  ll.insert(2)
  ll.insert(8)
  ll.insert(3)
  ll.insert(1)

  actual = ll.kthFromEnd(4)

  # Assert
  assert actual == expected

def test_third_linked_list_kth():
  #Arrange
  expected = 10
  ll = LinkedList()

  #Actual
  ll.insert(2)
  ll.insert(10)
  ll.insert(86)
  ll.insert(6)
  ll.insert(3)
  ll.insert(1)

  actual = ll.kthFromEnd(5)

  # Assert
  assert actual == expected

def test_fourth_linked_list_kth():
  #Arrange
  expected = 2
  ll = LinkedList()

  #Actual
  ll.insert(2)
  ll.insert(10)
  ll.insert(86)
  ll.insert(6)
  ll.insert(3)
  ll.insert(1)

  actual = ll.kthFromEnd(0)

  # Assert
  assert actual == expected


def test_linked_list_kth_greaterthan():
  #Arrange
  expected = None
  ll = LinkedList()

  #Actual
  ll.insert(2)
  ll.insert(10)
  ll.insert(86)
  ll.insert(6)
  ll.insert(3)
  ll.insert(1)

  actual = ll.kthFromEnd(8)

  # Assert
  assert actual == expected



def test_linked_list_kth_same_length():
  #Arrange
  expected = 2
  ll = LinkedList()

  #Actual
  ll.insert(2)
  ll.insert(10)
  ll.insert(86)
  ll.insert(6)
  ll.insert(3)
  ll.insert(1)

  actual = ll.kthFromEnd(6)

  # Assert
  assert actual == expected

def test_linked_list_kth_negative_k():
  #Arrange
  expected = None
  ll = LinkedList()

  #Actual
  ll.insert(2)
  ll.insert(10)
  ll.insert(86)
  ll.insert(6)
  ll.insert(3)
  ll.insert(1)

  actual = ll.kthFromEnd(-5)

  # Assert
  assert actual == expected


def test_linked_list_size_1():
  #Arrange
  expected = 10
  ll = LinkedList()

  #Actual
  ll.insert(10)

  actual = ll.kthFromEnd(1)

  # Assert
  assert actual == expected



def test_linked_list_kth_happy_path():
  #Arrange
  expected = 86
  ll = LinkedList()

  #Actual
  ll.insert(2)
  ll.insert(10)
  ll.insert(86)
  ll.insert(6)
  ll.insert(3)

  actual = ll.kthFromEnd(3)

  # Assert
  assert actual == expected
