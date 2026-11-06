import random


class Creature:
    def __init__(self, slogan=""):
        self.slogan = slogan
        self._life = type(self)._life
        self._strength = type(self)._strength
        self._charisma = type(self)._charisma
        self._weapon = type(self)._weapon

    @property
    def life(self):
        return self._life

    @property
    def strength(self):
        return self._strength

    @property
    def charisma(self):
        return self._charisma

    @property
    def weapon(self):
        return self._weapon

    @property
    def name(self):
        return self.__class__.__name__

    def __repr__(self):
        return f"<{self.name}(life={self.life})>"

    # -- new methods --- 

    def __call__(self):
        if self.slogan:
            print(self.slogan)

    # This method applies a hit taken during a fight.
    def hit(self, damage):
        if self.life <= 0:
            return
        power_up = random.randint(0, self.charisma)

        if power_up % 9 == 7: 
            self._life += power_up // 4
            print(f"[{self.name} magick restores {power_up // 4} life points!]")

        self._life -= damage

        if self._life <= 0:
            print(f"[{self.name} has died.]")

    # This method takes one turn in a fight.
    def fight(self, enemy, weapon):
        if self.life <= 0:
            print(f"[{self.name} is too dead to fight!]")
            return

        # Attack the opponent
        your_hit = random.randrange(self.strength + weapon)

        print(f"[You hit with {your_hit} points of damage!]")
        enemy.hit(your_hit)

        # Retaliation
        print(enemy)

        if enemy.life > 0:
            enemy_hit = random.randrange(enemy.strength + enemy.weapon)

            print(f"[Your enemy hit with {enemy_hit} points of damage!]")
            self.hit(enemy_hit)

class DwemthysArray(list):
    def __getattr__(self, name):
        if not self: # empty list
            if name == "life":
                return 0
            raise AttributeError("Dwemthy’s Array isn't found!")

        monster = self[0]
        attr = getattr(monster, name)
        if not callable(attr):
            return attr

        def dynamic_access(*args, **kwargs):
            result = attr(*args, **kwargs)
            # The selected monster should still be in front of the list.
            assert self and self[0] is monster, "The attacking monster is gone!"
            if monster.life <= 0:
                self.pop(0)
                if self:
                    print("\n")
                    print(f"[Get ready. A wild {self[0].name} has emerged.]")
                else:
                    print("[Whoa. You decimated Dwemthy’s Array!]")
            return result
        return dynamic_access