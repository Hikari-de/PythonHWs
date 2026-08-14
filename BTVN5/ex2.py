class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.__hp = hp
        self._level = level

    def get_hp(self):
        return self.__hp

    def take_damage(self, damage):
        if damage > 0:
            self.__hp = max(0, self.__hp - damage)

    def heal(self, amount):
        if amount > 0:
            self.__hp += amount

    def attack(self):
        return 0

    def show_info(self):
        print(
            f"Name: {self.name}, "
            f"HP: {self.__hp}, "
            f"Level: {self._level}"
        )


class Warrior(Character):
    def __init__(self, name, hp, level, strength):
        super().__init__(name, hp, level)
        self.strength = strength

    def attack(self):
        return self._level * 5 + self.strength


class Mage(Character):
    def __init__(self, name, hp, level, mana, magic_power):
        super().__init__(name, hp, level)
        self.__mana = mana
        self.magic_power = magic_power

    def attack(self):
        if self.__mana >= 10:
            self.__mana -= 10
            return self._level * 3 + self.magic_power
        return 0

    def show_info(self):
        print(
            f"Name: {self.name}, "
            f"HP: {self.get_hp()}, "
            f"Level: {self._level}, "
            f"Mana: {self.__mana}"
        )


warrior1 = Warrior("Thor", 150, 10, 20)
warrior2 = Warrior("Leon", 140, 9, 25)

mage1 = Mage("Merlin", 100, 10, 50, 30)
mage2 = Mage("Luna", 110, 8, 40, 35)

characters = [warrior1, warrior2, mage1, mage2]

damage = warrior1.attack()
mage1.take_damage(damage)

damage = mage1.attack()
warrior1.take_damage(damage)

damage = warrior2.attack()
mage2.take_damage(damage)

damage = mage2.attack()
warrior2.take_damage(damage)

print("Characters after battle:")

for character in characters:
    character.show_info()

strongest_character = max(characters, key=lambda character: character.get_hp())

print("\nCharacter with the highest HP:")
print(strongest_character.name, strongest_character.get_hp())

print("\nClass relationships:")
print(isinstance(warrior1, Character))
print(isinstance(mage1, Character))
print(issubclass(Warrior, Character))
print(issubclass(Mage, Character))