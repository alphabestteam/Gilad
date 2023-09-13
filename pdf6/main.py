from hero import Hero
from monster import Monster


def choose_action() -> int:
    print(
        "\n\
for damage Enter 1\n\
for level-up Enter 2\n\
for heal Enter 3\n\
for defend Enter 4"
    )
    action = int(input("Enter action: "))
    return action


def main():
    print(
        "Hello!\n\
        You are about to play a crazy game, where you will have to fight against monsters.\n\
        You have 10 lives - deplete by one every time a monster kills your hero.\n\
        Your hero is level 1. Every time you advance a level (by killing a monster) your level will increase by one.\n\
        In addition, you have coins (at the beginning of the game), with which you can level up. Leveling up increases the hero's damage and the hero's health.\n\
        After each turn, one more coin is added.\n\
        Before each action you will have to choose what to do (protect yourself from an attack - reduces the monster's damage,\n\
        attack the monster, level up, increase the hero's life).\n\
        The game will end when you run out of lives.\n\
        good luck in the game!!!"
    )
    hero_name = input("Enter the hero name: ")
    hero = Hero(hero_name)
    monster_name = input("Enter the monster name: ")
    monster = Monster(monster_name, hero.level)
    hero_defend = False

    while hero.hp > 0:
        action = choose_action()
        if action == 1:
            hero.attack(monster)
            hero.increase_coins(1)
            print("\nYour hero attacked the monster!")
        elif action == 2:
            hero.level_up()
            hero.increase_coins(1)
        elif action == 3:
            hero.heal()
            hero.increase_coins(1)
            print("\nYour hero healed!")
        elif action == 4:
            lower_damage = hero.defend(monster.damage)
            hero_defend = True
            hero.increase_coins(1)
            print("\nYour hero is defended!")

        if monster.hp == 0:
            print(
                "the monster was killed!\n\
and the new one was created"
            )
            monster = Monster(input("Enter the monster name: "), hero.level)
            hero.increase_coins(3)
            continue

        if hero_defend:
            hero.reduce_health(lower_damage)
            hero_defend = False
            print("\nThe monster attacked")
        else:
            monster.attack(hero)
            print("\nThe monster attacked")

        if hero.hp == 0:
            break
    print("Game over. Your hero has run out of life")


if __name__ == "__main__":
    main()
