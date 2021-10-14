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
  actual = ll.to_string()

  # Assert
  assert actual == expected


def test_linked_empty_list_to_string():
  # Arrange
  expected = "NULL"
  ll = LinkedList()

  # Act
  actual = ll.to_string()

  # Assert
  assert actual == expected

