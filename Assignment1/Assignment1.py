from __future__ import print_function
import unittest
# Kevin Valenzuela

''' when run with "-m unittest", the following produces:
    FAILED (failures=9, errors=2)
    your task is to fix the failing tests by implementing the necessary
    methods. '''


class LinkedList(object):
    class Node(object):
        # pylint: disable=too-few-public-methods
        ''' no need for get or set, we only access the values inside the
            LinkedList class. and really: never have setters. '''

        def __init__(self, value, next_node):
            self.value = value
            self.next_node = next_node

    def __init__(self, initial = None):
        self.front = self.back = self.current = None
        if initial is not None:
            for i in initial:
                self.push_front(i)
    # Kevin Valenzuela
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
    # Had to research the str method, credit to.  https://stackoverflow.com/questions/727761/python-str-and-lists

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

    ''' you need to(at least) implement the following three methods'''

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
        return value




    # Used this for testing
    # def printLinkedList(self):
    #     node = self.front
    #     print("The List.")
    #     while node:
    #         print(node.value)
    #         node = node.next_node

# ''' C-level work '''


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


# ''' B-level work '''


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


# ''' A-level work '''


class TestRepr(unittest.TestCase):
    def test(self):
        linked_list = LinkedList((1, 2, 3))
        self.assertEqual(linked_list.__repr__(), 'LinkedList((1, 2, 3))')


class TestErrors(unittest.TestCase):
    def test_pop_front_empty(self):
        self.assertRaises(RuntimeError, lambda: LinkedList().pop_front())

    def test_pop_back_empty(self):
        self.assertRaises(RuntimeError, lambda: LinkedList().pop_back())
#
#     KEVIN VALENZUELA
# ''' write some more test cases. '''
#
# ''' extra credit.
#     - write test cases for and implement a delete(value) method.
#     - write test cases for and implement a method that finds the middle
#       element with only a single traversal.
# '''
#
# ''' the following is a demonstration that uses our data structure as a
#     stack'''
#
#
# def fact(number):
#     '''"Pretend" to do recursion via a stack and iteration'''
#
#     if number < 0:
#         raise ValueError("Less than zero")
#     if number == 0 or number == 1:
#         return 1
#
#     stack = LinkedList()
#     while number > 1:
#         stack.push_front(number)
#         number -= 1
#
#     result = 1
#     while not stack.empty():
#         result *= stack.pop_front()
#
#     return result
#
#
# class TestFactorial(unittest.TestCase):
#     def test_less_than_zero(self):
#         self.assertRaises(ValueError, lambda: fact(-1))
#
#     def test_zero(self):
#         self.assertEqual(fact(0), 1)
#
#     def test_one(self):
#         self.assertEqual(fact(1), 1)
#
#     def test_two(self):
#         self.assertEqual(fact(2), 2)
#
#     def test_10(self):
#         self.assertEqual(fact(10), 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)


if '__main__' == __name__:
     unittest.main()
