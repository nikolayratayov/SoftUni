from project.toy_store import ToyStore
import unittest


class ToyStoreTests(unittest.TestCase):
    def setUp(self):
        self.toy = ToyStore()

    def test_init(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy.toy_shelf)

    def test_add_toy_shelf_doesnt_exist(self):
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy('Z', 'ee')
        self.assertEqual('Shelf doesn\'t exist!', str(ex.exception))

    def test_add_toy_toy_exists(self):
        self.toy.add_toy('A', 'a')
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy('A', 'a')
        self.assertEqual('Toy is already in shelf!', str(ex.exception))

    def test_add_toy_shelf_is_taken(self):
        self.toy.add_toy('A', 'zzzz')
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy('A', 'b')
        self.assertEqual('Shelf is already taken!', str(ex.exception))

    def test_add_toy(self):
        res = self.toy.add_toy('A', 'a')
        self.assertEqual('Toy:a placed successfully!', res)
        self.assertEqual({
            "A": 'a',
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy.toy_shelf)

    def test_remove_toy_shelf_doesnt_exist(self):
        with self.assertRaises(Exception) as ex:
            self.toy.remove_toy('Z', 'z')
        self.assertEqual('Shelf doesn\'t exist!', str(ex.exception))

    def test_remove_toy_toy_doesnt_exist(self):
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy('A', 'a')
            self.toy.remove_toy('A', 'z')
        self.assertEqual('Toy in that shelf doesn\'t exists!', str(ex.exception))

    def test_remove_toy(self):
        self.toy.add_toy('A', 'a')
        res = self.toy.remove_toy('A', 'a')
        self.assertEqual('Remove toy:a successfully!', res)
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy.toy_shelf)


if __name__ == '__main__':
    unittest.main()
