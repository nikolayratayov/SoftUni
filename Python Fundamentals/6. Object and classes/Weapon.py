class Weapon:
    def __init__(self, bullets):
        self.bullets = bullets

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            a = 'shooting...'
            return a
        else:
            a = 'no bullets left'
            return a

    def __repr__(self):
        a = f'Remaining bullets: {self.bullets}'
        return a

