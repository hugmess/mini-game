class Character:
    def __init__(self, name="", hp=30, damage=1, armor=0):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.armor = armor

    def attack(self, target):
        target.take_damage(self.damage)

    def take_damage(self, damage):
        # abs - модуль числа (целая часть)
        self.hp -= abs(damage)

    def stats(self):
        return \
            f" === {self.name} ===\n" \
            f" Здоровье: {self.hp}\n "\
            f"Урон: {self.damage}\n "\
            f"Броня: {self.armor}\n"


class Berserk(Character):
    def __init__(self, name="", hp=30, damage=1, armor=0):
        Character.__init__(self, name, hp, damage, armor)
        self.max_hp = self.hp

    def count_damage(self):
        return  self.damage + (self.hp / self.max_hp * self.damage)

    def attack(self, target):
        target.take_damage(self.count_damage())

class Assassin(Character):
    def __init__(self, name="", hp=30, damage=3, armor=0):
        Character.__init__(self, name, hp, damage, armor)

    def count_damage1(self):
            return self.damage + (self.damage / 10 % + self.hp)

class Samurai(Character):
    def __init__(self, name="", hp=30, damage=1, armor=10):
        Character.__init__(self, name, hp, damage, armor)
        self.max_armor = self.armor

    def count_damage3(self):
         return  self.damage + (self.armor / self.max_armor * self.damage)

class Ninja (Character):
    def __init__(self, name="", hp=30, damage=1, armor=5):
        Character.__init__(self, name, hp, damage, armor)
        self.max_hp = self.hp

    def count_damage3(self):
        return  self.armor + (self.hp / self.max_hp * self.armor)

    def attack(self, target):
        target.take_damage(self.count_damage3())


class Vampyre (Character):
    def __init__(self, name="", hp=30, damage=1, armor=0):
        Character.__init__(self, name, hp, damage, armor)

    def count_damage4(self):
        return  self.hp + (self.damage / 10% + self.hp)

    def attack3(self, target):
        target.take_damage(self.count_damage4())


