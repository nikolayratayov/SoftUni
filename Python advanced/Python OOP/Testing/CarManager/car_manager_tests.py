import unittest


class CarTests(unittest.TestCase):

    def setUp(self):
        self.car = Car('Volvo', 'V60', 3.5, 67)

    def test_constructor(self):
        self.assertEqual('Volvo', self.car.make)
        self.assertEqual('V60', self.car.model)
        self.assertEqual(3.5, self.car.fuel_consumption)
        self.assertEqual(67, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_setter_invalid(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual('Make cannot be null or empty!', str(ex.exception))

    def test_make(self):
        self.car.make = 'VOLVO'
        self.assertEqual('VOLVO', self.car.make)

    def test_model_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual('Model cannot be null or empty!', str(ex.exception))

    def test_model(self):
        self.car.model = 'XC90'
        self.assertEqual('XC90', self.car.model)

    def test_fuel_consumption_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1
        self.assertEqual('Fuel consumption cannot be zero or negative!', str(ex.exception))

    def test_fuel_consumption(self):
        self.car.fuel_consumption = 1
        self.assertEqual(1, self.car.fuel_consumption)

    def test_fuel_capacity_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1
        self.assertEqual('Fuel capacity cannot be zero or negative!', str(ex.exception))

    def test_fuel_capacity(self):
        self.car.fuel_capacity = 2
        self.assertEqual(2, self.car.fuel_capacity)

    def test_fuel_amount_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual('Fuel amount cannot be negative!', str(ex.exception))

    def test_refuel_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual('Fuel amount cannot be zero or negative!', str(ex.exception))

    def test_refuel(self):
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)

    def test_drive_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(10)
        self.assertEqual('You don\'t have enough fuel to drive!', str(ex.exception))

    def test_drive(self):
        self.car.refuel(67)
        self.car.drive(100)
        self.assertEqual(63.5, self.car.fuel_amount)


if __name__ == '__main__':
    unittest.main()