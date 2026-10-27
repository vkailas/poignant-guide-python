from dwemthy import Creature, DwemthysArray
from rabbit import Rabbit

class IndustrialRaverMonkey(Creature):
    _life = 46
    _strength = 35
    _charisma = 91
    _weapon = 2


class DwarvenAngel(Creature):
    _life = 540
    _strength = 6
    _charisma = 144
    _weapon = 50


class AssistantViceTentacleAndOmbudsman(Creature):
    _life = 320
    _strength = 6
    _charisma = 144
    _weapon = 50


class TeethDeer(Creature):
    _life = 655
    _strength = 192
    _charisma = 19
    _weapon = 109


class IntrepidDecomposedCyclist(Creature):
    _life = 901
    _strength = 560
    _charisma = 422
    _weapon = 105


class Dragon(Creature):
    _life = 45000       # tough scales
    _strength = 451    # bristling veins
    _charisma = 1020   # toothy smile
    _weapon = 939      # fire breath
    
dwary = DwemthysArray([
    IndustrialRaverMonkey(),
    DwarvenAngel(),
    AssistantViceTentacleAndOmbudsman(),
    TeethDeer(),
    IntrepidDecomposedCyclist(),
    Dragon(),
])

for monster in dwary:
    print(f"A wild {monster.name} appears!")