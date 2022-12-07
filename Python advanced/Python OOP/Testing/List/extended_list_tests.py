import unittest


class Tests(unittest.TestCase):

    def setUp(self):
        self.lst = IntegerList(1, 2, 3, 4, 5, 'a')

    def test_constructor(self):
        self.assertEqual([1, 2, 3, 4, 5], self.lst.get_data())

    def test_add_non_int(self):
        with self.assertRaises(ValueError) as ex:
            self.lst.add('das')
        self.assertEqual('Element is not Integer', str(ex.exception))

    def test_add_int(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], self.lst.add(6))

    def test_remove_invalid_index(self):
        with self.assertRaises(IndexError) as ex:
            self.lst.remove_index(10)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_remove_valid_index(self):
        self.assertEqual(5, self.lst.remove_index(4))

    def test_get_invalid_index(self):
        with self.assertRaises(IndexError) as ex:
            self.lst.get(100)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_get_valid_index(self):
        self.assertEqual(1, self.lst.get(0))

    def test_insert_invalid_index(self):
        with self.assertRaises(IndexError) as ex:
            self.lst.insert(100, 10)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_insert_invalid_element(self):
        with self.assertRaises(ValueError) as ex:
            self.lst.insert(2, 'a')
        self.assertEqual('Element is not Integer', str(ex.exception))

    def test_insert(self):
        self.lst.insert(0, 100)
        self.assertEqual([100, 1, 2, 3, 4, 5], self.lst.get_data())

    def test_get_biggest(self):
        self.assertEqual(5, self.lst.get_biggest())

    def test_get_index(self):
        self.assertEqual(0, self.lst.get_index(1))


if __name__ == '__main__':
    unittest.main()
