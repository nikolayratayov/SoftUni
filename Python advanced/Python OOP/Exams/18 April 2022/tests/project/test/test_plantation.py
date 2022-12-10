import pyexpat

from ..plantation import Plantation
import unittest


class PlantationTests(unittest.TestCase):
    def setUp(self):
        self.plantation = Plantation(5)

    def test_init(self):
        self.assertEqual(5, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.plantation.size = -1
        self.assertEqual('Size must be positive number!', str(ex.exception))

    def test_size(self):
        self.plantation.size = 2
        self.assertEqual(2, self.plantation.size)

    def test_hire_worker_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.plantation.hire_worker('niki')
            self.plantation.hire_worker('niki')
        self.assertEqual('Worker already hired!', str(ex.exception))

    def test_hire_worker(self):
        res = self.plantation.hire_worker('a')
        self.assertEqual('a successfully hired.', res)

    def test_len(self):
        self.assertEqual(0, len(self.plantation))
        self.plantation.plants['a'] = ['1', '2']
        self.plantation.plants['b'] = ['3']
        self.assertEqual(3, len(self.plantation))

    def test_planting_worker_not_hired(self):
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting('niki', 'a')
        self.assertEqual('Worker with name niki is not hired!', str(ex.exception))

    def test_planting_full_plantation(self):
        with self.assertRaises(ValueError) as ex:
            self.plantation.hire_worker('niki')
            self.plantation.plants['a'] = [1, 1, 1, 1, 1,]
            self.plantation.planting('niki', 'a')
        self.assertEqual('The plantation is full!', str(ex.exception))

    def test_planting_plant(self):
        self.plantation.hire_worker('a')
        self.plantation.plants['a'] = ['of']
        res = self.plantation.planting('a', 'plant1')
        self.assertEqual('a planted plant1.', res)

    def test_planting_first_plant(self):
        self.plantation.hire_worker('a')
        self.assertEqual('a planted it\'s first eee.', self.plantation.planting('a', 'eee'))

    def test_str(self):
        self.plantation.hire_worker('niki')
        self.plantation.hire_worker('ioni')
        self.plantation.planting('niki', 'a')
        self.plantation.planting('niki', 'b')
        self.plantation.planting('ioni', 'c')
        self.plantation.planting('ioni', 'd')
        self.assertEqual('Plantation size: 5\nniki, ioni\nniki planted: a, b\nioni planted: c, d', str(self.plantation))

    def test_repr(self):
        self.plantation.hire_worker('niki')
        self.plantation.hire_worker('ioni')
        self.assertEqual('Size: 5\nWorkers: niki, ioni', repr(self.plantation))



if __name__ == '__main__':
    unittest.main()