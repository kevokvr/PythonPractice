from __future__ import print_function
import unittest

class LinkedList(object):
    class Node(object):

        def __init__(self, value, next_node):
            self.value = value
            self.next_node = next_node

    def __init__(self, initial = None):
        self.front = self.back = self.current = None
        if initial is not None:
            for i in initial:
                self.push_front(i)

    def empty(self):
        return self.front == self.back == None

    def __iter__(self):
        self.current = self.front
        return self

    def __next__(self):
        if self.current:
            tmp = self.current.value
            self.current = self.current.next_node
            return tmp
        else:
            raise StopIteration()


    def __str__(self):
        self.reverse()
        string = ', '.join(map(str, self))
        return string

    def __repr__(self):
        return 'LinkedList((' + self.__str__()+ '))'

    def reverse(self):
        previous = None
        front = self.front
        while front is not None:
            next = front.next_node
            front.next_node = previous
            previous = front
            front = next
        self.front = previous

    def push_front(self, value):
        new = self.Node(value, self.front)
        if self.empty():
            self.front = self.back = new
        else:
            self.front = new

    def pop_front(self):
        if self.empty():
            raise RuntimeError
        else:
            value = self.front.value
        front = self.front
        if front.next_node is not None:
            while front.next_node is not None:
                self.front = front.next_node
                front.next_node = None
        else:
            self.front = self.back = self.current = None
        return value


    def push_back(self, value):
        new = self.Node(value, None)
        if self.empty():
            self.front = self.back = new
            return
        back = self.front
        while back.next_node is not None:
            back = back.next_node
        back.next_node = new
        self.back = back.next_node
        new.next_node = None


    def pop_back(self):
        if self.empty():
            raise RuntimeError
        else:
            value = self.back.value
        last = self.front
        previous = None
        if self.back is self.front:
            self.front = self.back = self.current = None
            return value
        else:
            while last.next_node is not None:
                previous = last
                last = last.next_node
            previous.next_node = None
            self.back = previous
            self.back = previous
        return value

    # Used this for testing
    def printLinkedList(self):
        node = self.front
        print("The List.")
        while node:
            print(node.value)
            node = node.next_node

class TestEmpty(unittest.TestCase):
    def test(self):
        self.assertTrue(LinkedList().empty())


class TestPushFrontPopBack(unittest.TestCase):
    def test(self):
        linked_list = LinkedList()
        linked_list.push_front(1)
        linked_list.push_front(2)
        linked_list.push_front(3)
        self.assertFalse(linked_list.empty())
        self.assertEqual(linked_list.pop_back(), 1)
        self.assertEqual(linked_list.pop_back(), 2)
        self.assertEqual(linked_list.pop_back(), 3)
        # linked_list.printLinkedList()
        self.assertTrue(linked_list.empty())


class TestPushFrontPopFront(unittest.TestCase):
    def test(self):
        linked_list = LinkedList()
        linked_list.push_front(1)
        linked_list.push_front(2)
        linked_list.push_front(3)
        # linked_list.printLinkedList()
        self.assertEqual(linked_list.pop_front(), 3)
        self.assertEqual(linked_list.pop_front(), 2)
        self.assertEqual(linked_list.pop_front(), 1)
        self.assertTrue(linked_list.empty())


class TestPushBackPopFront(unittest.TestCase):
    def test(self):
        linked_list = LinkedList()
        linked_list.push_back(1)
        linked_list.push_back(2)
        linked_list.push_back(3)
        self.assertFalse(linked_list.empty())
        # linked_list.printLinkedList()
        self.assertEqual(linked_list.pop_front(), 1)
        self.assertEqual(linked_list.pop_front(), 2)
        self.assertEqual(linked_list.pop_front(), 3)
        self.assertTrue(linked_list.empty())

		
class TestPushBackPopBack(unittest.TestCase):
    def test(self):
        linked_list = LinkedList()
        linked_list.push_back(1)
        linked_list.push_back("foo")
        linked_list.push_back([3, 2, 1])
        self.assertFalse(linked_list.empty())
        # linked_list.printLinkedList()
        self.assertEqual(linked_list.pop_back(), [3, 2, 1])
        self.assertEqual(linked_list.pop_back(), "foo")
        self.assertEqual(linked_list.pop_back(), 1)
        self.assertTrue(linked_list.empty())


class TestInitialization(unittest.TestCase):
    def test(self):
        linked_list = LinkedList(("one", 2, 3.141592))
        # linked_list.printLinkedList()
        self.assertEqual(linked_list.pop_back(), "one")
        self.assertEqual(linked_list.pop_back(), 2)
        self.assertEqual(linked_list.pop_back(), 3.141592)


class TestStr(unittest.TestCase):
    def test(self):
        linked_list = LinkedList((1, 2, 3))
        self.assertEqual(linked_list.__str__(), '1, 2, 3')


class TestRepr(unittest.TestCase):
    def test(self):
        linked_list = LinkedList((1, 2, 3))
        self.assertEqual(linked_list.__repr__(), 'LinkedList((1, 2, 3))')


class TestErrors(unittest.TestCase):
    def test_pop_front_empty(self):
        self.assertRaises(RuntimeError, lambda: LinkedList().pop_front())

    def test_pop_back_empty(self):
        self.assertRaises(RuntimeError, lambda: LinkedList().pop_back())


if '__main__' == __name__:
     unittest.main()
