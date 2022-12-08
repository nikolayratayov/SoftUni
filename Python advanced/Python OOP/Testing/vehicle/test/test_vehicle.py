from project.vehicle import Vehicle
import unittest

class VehicleTests(unittest.TestCase):

    def setUp(self):
        self.vehicle = Vehicle(60.5, 163.5)

    def test_init(self):
        self.assertEqual(60.5, self.vehicle.fuel)
        self.assertEqual(60.5, self.vehicle.capacity)
        self.assertEqual(163.5, self.vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual('Not enough fuel', str(ex.exception))

    def test_drive(self):
        self.vehicle.drive(4)
        self.assertEqual(55.5, self.vehicle.fuel)

    def test_refuel_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(100)
        self.assertEqual('Too much fuel', str(ex.exception))

    def test_refuel(self):
        self.vehicle.drive(4)
        self.vehicle.refuel(1)
        self.assertEqual(56.5, self.vehicle.fuel)

    def test_str(self):
        self.assertEqual('The vehicle has 163.5 horse power with 60.5 fuel left and 1.25 fuel consumption', str(self.vehicle))

    def test_class_var(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)



if __name__ == '__main__':
    unittest.main()
