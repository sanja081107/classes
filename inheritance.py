from classes import warrior, mag
class archer(warrior):
    def __init__(self, health=100, stamina=100, arrows=20):
        super().__init__(health, stamina)
        self.arrows = arrows
    def attacs(self, target):
        target.health -= 5
        self.arrows -= 1
        print('-----------')
        print(f'{self.__class__.__name__} наносит удар {target.__class__.__name__}',
              f'\nЗдоровье у {target.__class__.__name__} понижено до {target.health}',
              f'\nСтрел у {self.__class__.__name__} стало {self.arrows}')
        print('-----------')
unit1 = archer()
unit2 = warrior()

unit1.attacs(unit2)
print(unit1.__dict__)
unit1.introduces()
