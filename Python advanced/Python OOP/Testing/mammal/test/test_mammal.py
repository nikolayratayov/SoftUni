import unittest
from project.mammal import Mammal

class MammalTests(unittest.TestCase):

    def setUp(self):
        self.mammal = Mammal('niki', 'human', 'haha')

    def test_init(self):
        self.assertEqual('niki', self.mammal.name)
        self.assertEqual('human', self.mammal.type)
        self.assertEqual('haha', self.mammal.sound)

    def test_sound(self):
        self.assertEqual('niki makes haha', self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual('niki is of type human', self.mammal.info())

if __name__ == '__main__':
    unittest.main()
