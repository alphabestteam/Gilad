import random


PROPORTION = random.randint(1,9)


class Monster:
    def __init__(self, name: str, hero_level: int) -> None:
        self._name = name
        self._level = self.level_calculator(hero_level)
        self._hp = self._level * PROPORTION
        self._damage = self._level * PROPORTION

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def level(self) -> int:
        return self._level
    
    @property
    def hp(self) -> int:
        return self._hp
    
    @property
    def damage(self) -> int:
        return self._damage
    
    @hp.setter
    def hp(self, new_hp: int) -> None:
        self._hp = new_hp

    def level_calculator(self, hero_level: int) -> int:
        """
        Function that calculate the possible level for the monster
        """
        if hero_level == 1:
            return random.randint(1,(hero_level + 1))
        else:
            return random.randint((hero_level - 1),(hero_level + 1))
        
    def attack(self, hero) -> None:
        """
        Function that lower the heroine life
        by the monster's damage
        """
        hero.hp -= self.damage

    def reduce_health(self, hero) -> int:
        """
        Function that return the remaining life of the monster,
        after the heroine's attack
        """
        if hero.damage > self.hp:
            self.hp = 0
        else:
            self.hp -= hero.damage
        return self.hp

    