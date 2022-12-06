import unittest


class CatTests(unittest.TestCase):

  def setUp(self):
    self.cat = Cat('Niki')

  def test_cat_size_increase(self):
    self.cat.eat()
    self.assertEqual(1, self.cat.size)

  def test_cat_is_fed_after_eating(self):
    self.cat.eat()
    self.assertTrue(self.cat.fed)

  def test_cannot_eat_if_already_fed(self):
    with self.assertRaises(Exception) as ex:
      self.cat.eat()
      self.cat.eat()
    self.assertEqual(str(ex.exception), 'Already fed.')

  def test_cannot_sleep_if_not_fed(self):
    with self.assertRaises(Exception) as ex:
      self.cat.sleep()
    self.assertEqual(str(ex.exception), 'Cannot sleep while hungry')

  def test_cat_is_not_sleepy_after_sleeping(self):
    self.cat.eat()
    self.cat.sleep()
    self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
  unittest.main()
