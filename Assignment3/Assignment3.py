import unittest

'''
Write a recursive method that takes 1) a string to find, 2) a string to replace the found string with, and 3) an initial
string. Return the initial string with all the found strings replaced with the replacement string. You may not use loops 
or the built-in string methods except comparison, length, and slicing. Here is an outline.
'''

'''
Description: Assignment 3
Author: Kevin Valenzuela
# Version: 15+ tries
Help received from: 
-https://stackoverflow.com/questions/9573244/most-elegant-way-to-check-if-the-string-is-empty-in-python
-https://www.pythoncentral.io/cutting-and-slicing-strings-in-python/
-https://www.python-course.eu/recursive_functions.php
-https://www.youtube.com/results?search_query=python+recursion

Help provided to: Makda and I sat at the library and learned recursion with slide examples. Over the due weekend, we
talked about what we were planning to do and our roadblocks.
'''


def findandreplace(find, replace, string):
    '''
    Replace all instances of find with replace in string.

    Recursive approach:
    If the string starts with find
        return replace and call findandreplace with the rest of the string
    else
        return the first character of the string and call findandreplace with the rest of the string
    '''
    if not string:       # Base cases up here
        return string
    elif not find:
        return string
    elif replace is None:
        return string     # Base cases end
    else:
        string1 = string[:len(find)] # This make a string by slicing the original string by the lenght of find
        if string1 == find:          # It helps because I don't need to iterate through each array slot
            return replace + findandreplace(find, replace, string[len(find):]) # this passes the remainder of the string
        else:
            return string[0] + findandreplace(find, replace, string[1:])

class TestFindAndReplace(unittest.TestCase):
    def test_all_none(self):
        self.assertEqual(findandreplace(None, None, None), None)

    def test_find_none(self):
        self.assertEqual(findandreplace(None, "a", "aabb"), "aabb")

    def test_find_empty(self):
        self.assertEqual(findandreplace("", "a", "aabb"), "aabb")

    def test_replace_none(self):
        self.assertEqual(findandreplace("a", None, "aabb"), "aabb")

    def test_string_none(self):
        self.assertEqual(findandreplace("a", "b", None), None)

    def test_simple(self):
        self.assertEqual(findandreplace("a", "b", "aabb"), "bbbb")

    def test_remove(self):
        self.assertEqual(findandreplace(" ", "", " a abb"), "aabb")

    def test_anotherone(self):
        self.assertEqual(findandreplace("dog", "cat", "My dog is cool"), "My cat is cool")

    def test_gettysburg(self):
        self.assertEqual(findandreplace("Four score", "Twenty", \
                                        "Four score and seven years ago"), "Twenty and seven years ago")
if __name__ == '__main__':
    unittest.main()