from stack_and_queue import __version__
from stack_and_queue.stack import Stack, EmptyStack
from stack_and_queue.queue import Queue, EmptyQueue
import pytest


def test_version():
    assert __version__ == '0.1.0'


    # Arrange

    # Actual

    # Assert



# Can successfully push onto a stack

def test_push_stack():
    # Arrange
    stack = Stack()
    stack.push(1)
    expected = 1

    # Actual
    actual = stack.top.value

    # Assert
    assert actual == expected

# Can successfully push multiple values onto a stack

def test_push_multi_stack():
    # Arrange
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    expected = 4

    # Actual
    actual = stack.top.value

    # Assert
    assert actual == expected


# Can successfully pop off the stack

def test_pop_stack():
    # Arrange
    stack = Stack()
    stack.push(3)
    stack.push(4)
    expected = 4

    # Actual
    actual = stack.pop()

    # Assert
    assert actual == expected


# Can successfully empty a stack after multiple pops

def test_pop_multi_stack():
    # Arrange
    stack = Stack()
    stack.push(3)
    stack.push(4)
    expected = True
    stack.pop()
    stack.pop()

    # Actual
    actual = stack.is_empty()

    # Assert
    assert actual == expected


# Can successfully peek the next item on the stack

def test_peek_stack():
    # Arrange
    stack = Stack()
    stack.push(3)
    stack.push(4)
    stack.push(8)
    expected = 8

    # Actual
    actual = stack.peek()

    # Assert
    assert actual == expected


# Can successfully instantiate an empty stack

def test_instantiate_stack():
    # Arrange
    stack = Stack()
    expected = None

    # Actual
    actual = stack.top.value

    # Assert
    assert actual == expected

# Calling pop or peek on empty stack raises exception

def test_instantiate_stack():
    with pytest.raises(EmptyStack) as excinfo:
        pop_fail()

    assert str(excinfo.value) == "Errour encounted....Stack is empty."
def pop_fail():
    stack = Stack()
    stack.pop()

# Can successfully enqueue into a queue

def test_enqueue():
    # Arrange
    queue = Queue()
    queue.enqueue(5)
    expected = 5

    # Actual
    actual = queue.front.value
    # Assert

    assert actual == expected

#C an successfully enqueue multiple values into a queue

def test_multi_enqueue():
    # Arrange
    queue = Queue()
    queue.enqueue(8)
    queue.enqueue(10)
    queue.enqueue(2)
    queue.enqueue(12)
    expected = 12

    # Actual
    actual = queue.rear.value
    # Assert

    assert actual == expected

# Can successfully dequeue out of a queue the expected value

def test_multi_enqueue():
    # Arrange
    queue = Queue()
    queue.enqueue(8)
    queue.enqueue(10)
    queue.enqueue(2)
    queue.enqueue(12)
    expected = 8

    # Actual
    actual = queue.dequeue()
    # Assert

    assert actual == expected

# Can successfully peek into a queue, seeing the expected value

def test_peek_enqueue():
    # Arrange
    queue = Queue()
    queue.enqueue(15)
    queue.enqueue(10)
    queue.enqueue(2)
    queue.enqueue(12)
    expected = 15

    # Actual
    actual = queue.peek()
    # Assert

    assert actual == expected

# Can successfully empty a queue after multiple dequeues

def test_peek_enqueue():
    # Arrange
    queue = Queue()
    queue.enqueue(15)
    queue.enqueue(10)
    queue.enqueue(2)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    expected = True

    # Actual
    actual = queue.is_empty()
    # Assert

    assert actual == expected

# Can successfully instantiate an empty queue

def test_peek_enqueue():
    # Arrange
    queue = Queue()
    expected = None

    # Actual
    actual = queue.front
    # Assert

    assert actual == expected

# Calling dequeue or peek on empty queue raises exception


def test_dequeue_fail():
    with pytest.raises(EmptyQueue) as excinfo:
        dequeue_fail()

    assert str(excinfo.value) == "Empty Queue! can't dequeue an empty queue."
def dequeue_fail():
    queue = Queue()
    queue.dequeue()

