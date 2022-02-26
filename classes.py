class warrior:
    def __init__(self, health, stamina):
        self.health = health
        self.stamina = stamina
class mag:
    def __init__(self):
        self.health = 80
        self.stamina = 99
unit1 = warrior(100, 100)
unit2 = mag()

# unit1.health = 100
# unit1.stamina = 100

# unit2.health = 80
# unit2.stamina = 99

print(unit1.__dict__)
print(unit2.__dict__)

