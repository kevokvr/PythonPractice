import unittest

'''
Description: Assignment 2 - Dictionary
Author: Kevin Valenzuela
Version: 2.0
Help provided to: I helped Makda by writing pseudocode of what I did in some methods
Help received from: Read some stuff online about dictionaries, lists, hashmaps. 
'''

'''
    Implement a dictionary using chaining.
    You may assume every key has a hash() method, e.g.:
    >>> hash(1)
    1
    >>> hash('hello world')
    -2324238377118044897
'''


class dictionary:
    def __init__(self, init=None):
        self.__limit = 10
        self.__items = [[] for _ in range(self.__limit)]
        self.__count = 0
        if init:
            for i in init:
                self.__setitem__(i[0], i[1])

    def __len__(self):
        return self.__count

    def flattened(self):
        return [item for inner in self.__items for item in inner]

    def limit(self):
        return self.__limit

    def __iter__(self):
        return (iter(self.flattened()))

    def __str__(self):
        return (str(self.flattened()))

    def __setitem__(self, key, value):
        keyhash = self.gethash(key)
        keyvalue = [key, value]
        if self.__items[keyhash] is None:
            self.__items[keyhash] = list([keyvalue])
        else:
            for item in self.__items[keyhash]:
                if item[0] == key:
                    item[1] = value
            self.__items[keyhash].append(keyvalue)
        self.__count += 1
        counttest = self.__count
        limittest = self.__limit * .75
        if counttest >= limittest:
            self.redo()

    def __getitem__(self, key):
        # Retrieve from the dictionary.
        keyhash = self.gethash(key)
        if self.__items[keyhash] is not None:
            for item in self.__items[keyhash]:
                if item[0] == key:
                    return item[1]
        return None

    def __contains__(self, key):
        # Implements the 'in' operator.
        keyhash = self.gethash(key)
        if self.__items[keyhash] is not None:
            for item in self.__items[keyhash]:
                if item[0] == key:
                    return True
                else:
                    return False

    def gethash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char) # ord gets the number value of a letter and adds it
        return hash % self.__limit
    # this hash works for both integer keys and string keys

    def __delitem__(self, key):
        keyhash = self.gethash(key)
        if self.__items[keyhash] is not None:
            for item in self.__items[keyhash]:
                if item[0] == key:
                    self.__items[keyhash].pop()  # since its a list, we can pop
        self.__count -= 1
        counttest = self.__count
        limittest = self.__limit * .25
        if counttest <= limittest:
            self.gosmall()

    def print(self):
        # used this to print my list while testing hash and doubling/halving
        print('----------------------------------------')
        for item in self.__items:
                print(str(item))
        print('----------------------------------------')

    def redo(self):
        temp = self.flattened()
        self.__limit = self.__limit * 2
        self.__count = 0
        self.__items = [[] for _ in range(self.__limit)]
        for i in temp:
            self.__setitem__(i[0], i[1])

    def gosmall(self):
        stemp = self.flattened()
        self.__limit = int(self.__limit / 2)
        self.__count = 0
        self.__items = [[] for _ in range(self.__limit)]
        for i in stemp:
            self.__setitem__(i[0], i[1])

    def thekeys(self):
        keylist = list()
        for i in range(self.limit()):
            if self.__items[i] is not None:
                for item in self.__items[i]:
                    if item[0] is not None:
                        keylist.append(item[0])
        return keylist

    def thevalues(self):
        valuelist = list()
        for i in range(self.limit()):
            if self.__items[i] is not None:
                for item in self.__items[i]:
                    if item[1] is not None:
                        valuelist.append(item[1])
        return valuelist

#     C-level work

class test_add_two(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "one"
        s[2] = "two"
        self.assertEqual(len(s), 2)
        self.assertEqual(s[1], "one")
        self.assertEqual(s[2], "two")

class test_add_twice(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "one"
        s[1] = "one"
        self.assertEqual(len(s), 2)
        self.assertEqual(s[1], "one")

class test_store_false(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = False
        self.assertTrue(1 in s)
        self.assertFalse(s[1])

class test_store_none(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = None
        self.assertTrue(1 in s)
        self.assertEqual(s[1], None)

class test_none_key(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[None] = 1
        self.assertTrue(None in s)
        self.assertEqual(s[None], 1)

class test_False_key(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[False] = 1
        self.assertTrue(False in s)
        self.assertEqual(s[False], 1)

class test_collide(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[0] = "zero"
        s[10] = "ten"
        self.assertEqual(len(s), 2)
        self.assertTrue(0 in s)
        self.assertTrue(10 in s)

class test_Many_new(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "zero"
        s[10] = "ten"
        s[2] = "two"
        s[84] = "one"
        s[56] = "awesome"
        s[9] = "cool"
        self.assertEqual(len(s), 6)

class test_del_key(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[9] = "cool"
        s[4] = "nice"
        s[8] = "kev"
        s[17] = "comp"
        s[56] = "water"
        s[73] = "book"
        s[45] = "pen"
        s[23] = "shoe"
        s[19] = "day"
        s.__delitem__(19)
        s.__delitem__(56)
        self.assertFalse(19 in s)
        self.assertFalse(56 in s)

class test_rehash(unittest.TestCase):
    def test(self):
        d = dictionary()
        d[10] = "ten"
        d[2] = "two"
        d[84] = "one"
        d[56] = "awesome"
        d[9] = "cool"
        d[4] = "nice"
        d.__setitem__(45, "howdy")
        d.__setitem__(63, "testing")
        d.__setitem__(7, "richard")
        self.assertTrue(d.__len__(), 9)
        self.assertEqual(d.limit(), 20)

class test_halving(unittest.TestCase):
    def test(self):
        d = dictionary()
        d[10] = "tinkle"
        d[2] = "two"
        d[84] = "one"
        d[56] = "awesome"
        d[9] = "cool"
        d[4] = "nice"
        d[8] = "kev"
        d[17] = "comp"
        d[56] = "water"
        d[73] = "book"
        d[45] = "pen"
        d[23] = "shoe"
        d[19] = "day"
        d[18] = "ten"
        d[67] = "sixseven"
        d[51] = "fiveone"
        d[69] = "sixnine"
        d[43] = "fourthree"
        d[573] = "big"
        d[888] = "google"
        d.__delitem__(18)
        d.__delitem__(2)
        d.__delitem__(84)
        d.__delitem__(56)
        d.__delitem__(9)
        d.__delitem__(4)
        d.__delitem__(17)
        d.__delitem__(56)
        d.__delitem__(73)
        d.__delitem__(45)
        d.__delitem__(23)
        self.assertEqual(d.limit(), 20)
        d.__delitem__(51)
        d.__delitem__(43)
        d.__delitem__(73)
        d.__delitem__(888)
        d.__delitem__(67)
        self.assertEqual(d.limit(), 10)

class test_key_return(unittest.TestCase):
    def test(self):
        d = dictionary()
        d[20] = "Hi"
        d[34] = "hello"
        d[60] = "ciao"
        self.assertEqual(d.thekeys(), [60, 34, 20])

class test_value_return(unittest.TestCase):
    def test(self):
        d = dictionary()
        d[20] = "Hi"
        d[34] = "hello"
        d[60] = "ciao"
        self.assertEqual(d.thevalues(), ['ciao', 'hello', 'Hi'])


''' B-level work - All tests towards bottom of tests
    Add doubling and rehashing when load goes over 75%
        ON LINE 45ish
    Add __delitem__(self, key)
        ON LINE 90ish
'''

''' A-level work - All tests towards bottom of tests
    Add halving and rehashing when load goes below 25%
        ON LINE 114ish
    Add keys() returns list of keys
        ON LINE 122ish
    Add values() returns list of values
        ON LINE 133ish
'''

''' Extra credit
    Add __eq__()
    Add items(), "a list of D's (key, value) pairs, as 2-tuples"
'''

if __name__ == '__main__':
    unittest.main()