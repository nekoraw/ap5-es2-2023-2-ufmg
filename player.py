import random


def get_random(chance):
    if random.random() < chance:
        return 1


class Player:
    def __init__(self, health=100, attack=100, defense=100, crit_rate=0.05, crit_damage=0.5):
        self.health = health
        self.attack = attack
        self.defense = defense

        self.crit_rate = crit_rate
        self.crit_damage = crit_damage

    def attack_user(self):
        damage_value = self.attack

        if get_random(self.crit_rate):
            damage_value *= (1 + self.crit_damage)

        return damage_value

    def take_damage(self, value):
        self.health -= max((value - self.defense, 0))
        return self.health


