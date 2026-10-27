import random
from dwemthy import Creature

class Rabbit(Creature):
    _life = 10
    _strength = 2
    _charisma = 84
    _weapon = 4
    def __init__(self, slogan=""):
        super().__init__(slogan)
        self.bombs = 3

    # little boomerang
    def __xor__(self, enemy):
        self.fight(enemy, 13)

    # the hero's sword is unlimited!!
    def __truediv__(self, enemy):
        weapon = random.randrange(
            4 + (enemy.life % 10) ** 2
        )
        self.fight(enemy, weapon)

    # Lettuce builds your strength and extra roughage flies in the face of your opponent!!
    # Like popeye and spinach but a bunny and lettuce
    def __mod__(self, enemy):
        lettuce = random.randint(0, self.charisma)

        print(f"[Healthy lettuce brings you {lettuce} life and strength points!!]")
        if self._life < 0:
            print("[Reviving with lettuce...]")
        self._life += lettuce
        self._strength += lettuce
        self._charisma += round(lettuce*.5)
        self.fight(enemy, 0)

    # bombs, but you only have three!!
    def __mul__(self, enemy):
        if self.bombs == 0:
            print("[UHN!! You're out of bombs!!]")
            return

        if self.life <= 0:
            print("[Rabbit is too dead to throw a bomb! Revive first with lettuce!!]")
            return
    
        self.bombs -= 1
        if enemy.name == "Dragon":
            print("[The bomb ignites the dragon's fire breath! BOOM!!]")
            enemy.hit(50000)
        else:
            self.fight(enemy, 86)