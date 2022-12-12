from project.shopping_cart import ShoppingCart
import unittest


class ShoppingCartTests(unittest.TestCase):
    def setUp(self):
        self.shopping_cart = ShoppingCart('Niki', 100.5)
        self.additional_products = {'a': 1, 'b': 2}

    def test_init(self):
        self.assertEqual('Niki', self.shopping_cart.shop_name)
        self.assertEqual(100.5, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)
        self.shopping_cart.products = self.additional_products
        self.assertEqual({'a': 1, 'b': 2}, self.shopping_cart.products)

    def test_name_setter_value_error_non_capital_start(self):
        with self.assertRaises(ValueError) as ex:
            self.shopping_cart.shop_name = 'niki'
        self.assertEqual('Shop must contain only letters and must start with capital letter!', str(ex.exception))

    def test_name_setter_value_error_nums(self):
        with self.assertRaises(ValueError) as ex:
            self.shopping_cart.shop_name = 'N23'
        self.assertEqual('Shop must contain only letters and must start with capital letter!', str(ex.exception))

    def test_name_setter_valid(self):
        self.shopping_cart.shop_name = 'Ioni'
        self.assertEqual('Ioni', self.shopping_cart.shop_name)

    def test_add_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.shopping_cart.add_to_cart('das', 100)
        self.assertEqual('Product das cost too much!', str(ex.exception))

    def test_add_to_cart(self):
        res = self.shopping_cart.add_to_cart('a', 10.5)
        self.assertEqual('a product was successfully added to the cart!', res)
        self.assertEqual({'a': 10.5}, self.shopping_cart.products)

    def test_remove_non_existing(self):
        with self.assertRaises(ValueError) as ex:
            self.shopping_cart.remove_from_cart('a')
        self.assertEqual('No product with name a in the cart!', str(ex.exception))

    def test_remove_product(self):
        self.shopping_cart.products = self.additional_products
        self.shopping_cart.add_to_cart('c', 3.3)

        res = self.shopping_cart.remove_from_cart('a')
        self.assertEqual('Product a was successfully removed from the cart!', res)
        self.assertEqual({'b': 2, 'c': 3.3}, self.shopping_cart.products)

        res2 = self.shopping_cart.remove_from_cart('b')
        self.assertEqual('Product b was successfully removed from the cart!', res2)
        self.assertEqual({'c': 3.3}, self.shopping_cart.products)

    def test_add(self):
        other_instance = ShoppingCart('Ioni', 200.5)
        other_instance.products = {'x': 1, 'y': 2}
        self.shopping_cart.products = self.additional_products
        new_obj = self.shopping_cart + other_instance
        self.assertEqual('NikiIoni', new_obj.shop_name)
        self.assertEqual(301, new_obj.budget)
        self.assertEqual({'a': 1, 'b': 2, 'x': 1, 'y': 2}, new_obj.products)

    def test_buy_product_value_error(self):
        with self.assertRaises(Exception) as ex:
            self.shopping_cart.add_to_cart('a', 50)
            self.shopping_cart.add_to_cart('b', 50)
            self.shopping_cart.add_to_cart('c', 50)
            self.shopping_cart.buy_products()
        self.assertEqual('Not enough money to buy the products! Over budget with 49.50lv!', str(ex.exception))

    def test_buy_products(self):
        self.shopping_cart.add_to_cart('a', 50)
        res = self.shopping_cart.buy_products()
        self.assertEqual('Products were successfully bought! Total cost: 50.00lv.', res)






if __name__ == '__main__':
    unittest.main()