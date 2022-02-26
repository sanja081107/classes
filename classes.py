class warrior:
    def __init__(self, health=100, stamina=100):
        self.health = health
        self.stamina = stamina
    def introduces(self):
        print('-----------')
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.health}',
              f'\nStamina: {self.stamina}')
        print('-----------')
    def heals(self, target):
        target.health += 10
        self.stamina -= 20
        print('-----------')
        print(f'{self.__class__.__name__} накладывает повязку из трав {target.__class__.__name__}',
              f'\nЗдоровье у {target.__class__.__name__} повышено до {target.health}',
              f'\nY {self.__class__.__name__} осталось {self.stamina} жизненной силы')
        print('-----------')
    def attacs(self, target):
        target.health -= 3
        print(f'{self.__class__.__name__} наносит удар {target.__class__.__name__}',
              f'\nЗдоровье у {target.__class__.__name__} понижено до {target.health}')
        print('-----------')


class mag:
    def __init__(self, health, stamina):
        self.health = health
        self.stamina = stamina
    def introduces(self):
        print('-----------')
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.health}',
              f'\nStamina: {self.stamina}')
        print('-----------')
    def heals(self, target):
        target.health += 10
        self.stamina -= 20
        print('-----------')
        print(f'{self.__class__.__name__} принимает заклинание лечения',
              f'\nЗдоровье у {target.__class__.__name__} повышено до {self.health}',
              f'\nY {self.__class__.__name__} осталось {self.stamina} жизненной силы')
        print('-----------')
    def attacs(self, target):
        target.health -= 3
        print(f'{self.__class__.__name__} наносит удар {target.__class__.__name__}',
              f'\nЗдоровье у {target.__class__.__name__} понижено до {target.health}')
        print('-----------')

unit1 = warrior(60, 40)
unit2 = mag(40, 55)
unit3 = mag(80, 60)

unit1.introduces()
unit2.introduces()
unit3.heals(unit3)
unit1.heals(unit1)
unit1.attacs(unit2)
# unit1.health = 100
# unit1.stamina = 100

# unit2.health = 80
# unit2.stamina = 99

print(unit1.__dict__)
print(unit2.__dict__)
print(unit3.__dict__)
