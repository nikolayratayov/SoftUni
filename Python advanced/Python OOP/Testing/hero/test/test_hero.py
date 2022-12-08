from project.hero import Hero
import unittest


class HeroTests(unittest.TestCase):

    def setUp(self):
        self.kunkka = Hero('Kunkka', 25, 3000.5, 300.5)
        self.mepo = Hero('Mepo', 1, 100.5, 10.5)

    def test_init(self):
        self.assertEqual('Kunkka', self.kunkka.username)
        self.assertEqual(25, self.kunkka.level)
        self.assertEqual(3000.5, self.kunkka.health)
        self.assertEqual(300.5, self.kunkka.damage)

    def test_cannot_fight_yourself(self):
        self.mepo.username = 'Kunkka'
        with self.assertRaises(Exception) as ex:
            self.kunkka.battle(self.mepo)
        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test_your_health_is_lower(self):
        self.kunkka.health = 0
        with self.assertRaises(ValueError) as ex:
            self.kunkka.battle(self.mepo)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

    def test_enemy_health_lower(self):
        self.mepo.health = 0
        with self.assertRaises(ValueError) as ex:
            self.kunkka.battle(self.mepo)
        self.assertEqual('You cannot fight Mepo. He needs to rest', str(ex.exception))

    def test_draw(self):
        self.mepo.health = 3000.5
        self.mepo.damage = 300.5
        self.mepo.level = 25
        self.assertEqual('Draw', self.kunkka.battle(self.mepo))

    def test_win(self):
        self.assertEqual('You win', self.kunkka.battle(self.mepo))

    def test_lose(self):
        self.assertEqual('You lose', self.mepo.battle(self.kunkka))

    def test_str(self):
        self.assertEqual('Hero Kunkka: 25 lvl\nHealth: 3000.5\nDamage: 300.5\n', str(self.kunkka))

    def test_enemy_level(self):
        self.mepo.battle(self.kunkka)
        self.assertEqual(26, self.kunkka.level)
        self.assertEqual(2995, self.kunkka.health)
        self.assertEqual(305.5, self.kunkka.damage)

    def test_battle_health(self):
        self.kunkka.battle(self.mepo)
        self.assertEqual(26, self.kunkka.level)
        self.assertEqual(2995, self.kunkka.health)
        self.assertEqual(305.5, self.kunkka.damage)



if __name__ == '__main__':
    unittest.main()