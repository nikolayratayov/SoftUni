import unittest


class WorkerTests(unittest.TestCase):

    def setUp(self):
        self.person = Worker('Niki', 1, 1)

    def test_initialize(self):
        res_name = self.person.name
        expected_res_name = 'Niki'
        self.assertEqual(res_name, expected_res_name)
        res_salary = self.person.salary
        expected_res_salsary = 1
        self.assertEqual(res_salary, expected_res_salsary)
        res_energy = self.person.energy
        expected_res_energy = 1
        self.assertEqual(res_energy, expected_res_energy)
        res_money = self.person.money
        expected_res_money = 0
        self.assertEqual(res_money, expected_res_money)

    def test_work_add_money(self):
        self.person.work()
        res = self.person.money
        exp = 1
        self.assertEqual(res, exp)

    def test_work_decrease_energy(self):
        self.person.work()
        res = self.person.energy
        exp = 0
        self.assertEqual(res, exp)

    def test_rest_energy_increase(self):
        self.person.rest()
        res = self.person.energy
        exp = 2
        self.assertEqual(res, exp)

    def test_raise_exception(self):
        self.person.work()
        with self.assertRaises(Exception) as ex:
            self.person.work()
        self.assertEqual(str(ex.exception), 'Not enough energy.')

    def test_get_info(self):
        self.assertEqual('Niki has saved 0 money.', self.person.get_info())


if __name__ == '__main__':
    unittest.main()
