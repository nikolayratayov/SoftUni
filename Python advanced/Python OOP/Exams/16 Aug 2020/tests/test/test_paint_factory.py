from project.factory.paint_factory import PaintFactory
import unittest


class PaintFactoryTests(unittest.TestCase):

    def setUp(self):
        self.paintfactory = PaintFactory('niki', 3)

    def test_init(self):
        self.assertEqual('niki', self.paintfactory.name)
        self.assertEqual(3, self.paintfactory.capacity)
        self.assertEqual({}, self.paintfactory.ingredients)
        self.assertEqual(['white', 'yellow', 'blue', 'green', 'red'], self.paintfactory.valid_ingredients)

    def test_add_type_error(self):
        with self.assertRaises(TypeError) as ex:
            self.paintfactory.add_ingredient('black', 1)
        self.assertEqual('Ingredient of type black not allowed in PaintFactory', str(ex.exception))

    def test_add_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.paintfactory.add_ingredient('white', 5)
        self.assertEqual('Not enough space in factory', str(ex.exception))

    def test_add_new_ingredient(self):
        self.paintfactory.add_ingredient('white', 1)
        self.assertEqual(1, self.paintfactory.ingredients['white'])

    def test_add_existing(self):
        self.paintfactory.add_ingredient('white', 1)
        self.paintfactory.add_ingredient('white', 1)
        self.assertEqual(2, self.paintfactory.ingredients['white'])

    def test_products(self):
        self.assertEqual({}, self.paintfactory.products)

    def test_remove_key_error(self):
        with self.assertRaises(KeyError) as ex:
            self.paintfactory.remove_ingredient('white', 1)
        self.assertEqual('\'No such ingredient in the factory\'', str(ex.exception))

    def test_remove_value_error(self):
        self.paintfactory.add_ingredient('white', 1)
        with self.assertRaises(ValueError) as ex:
            self.paintfactory.remove_ingredient('white', 2)
        self.assertEqual('Ingredients quantity cannot be less than zero', str(ex.exception))

    def test_remove(self):
        self.paintfactory.add_ingredient('white', 2)
        self.paintfactory.remove_ingredient('white', 1)
        self.assertEqual(1, self.paintfactory.products['white'])


if __name__ == '__main__':
    unittest.main()