import random


N = 4
M = 4
K = 2


class Hero:
    def __init__(self, name: str) -> None:
        self._name = name
        self._hp = 10
        self._damage = 2
        self._level = 1
        self._coins = 0

    @property
    def name(self) -> str:
        return self._name

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def damage(self) -> int:
        return self._damage

    @property
    def level(self) -> int:
        return self._level

    @property
    def coins(self) -> int:
        return self._coins

    @hp.setter
    def hp(self, new_hp: int) -> None:
        self._hp = new_hp

    @damage.setter
    def damage(self, new_damage: int) -> None:
        self._damage = new_damage

    @level.setter
    def level(self, new_level: int) -> None:
        self._level = new_level

    @coins.setter
    def coins(self, new_coins: int) -> None:
        self._coins = new_coins

    def heal(self) -> int:
        """
        Function that return N percent of the heroine's life
        """
        self.hp += (N / 100) * self.hp
    
    def level_up(self) -> None:
        """
        Function that raises the level of the heroine
        """
        if self.coins >= (K * (self.level + 1)):
            self.coins -= (K * (self.level + 1))
            self.level += 1
            self.damage += (M / 100) * self.damage
            self.hp += (M / 100) * self.hp
            print("\nYour hero moved a level-up!")
        else:
            print("\nCoins are missing")


    def attack(self, monster) -> None:
        """
        Function that attacked monster and takes her life.
        If the heroine killed the monster, the heroine will get coins
        """
        monster.reduce_health(self)
        if monster.hp == 0:
            self.coins += self.level

    def defend(self, damage: int) -> int:
        """
        Function that received damage for the heroine,
        and lowers 80 percent of the damage
        """
        damage -= (80 / 100) * damage
        return damage

    def reduce_health(self, damage: int) -> int:
        """
        Function returns the life left for the heroine
        after the monster's attack.
        """
        if damage > self.hp:
            self.hp = 0
        else:
            self.hp -= damage
        return self.hp

    def increase_coins(self, coins: int) -> None:
        """
        Function that add coins to the total coins the heroine has
        """
        self.coins += coins