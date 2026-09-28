class Elevator:
    """A deliberately inspectable elevator for demonstrating Python classes.

    The ``level`` is an property attribute: every Elevator object tracks its own
    current floor. 
    The password is a class attribute so all elevator instances
    use the same maintenance code.
    """

    __maintenance_password = "stairs_are_history!"
    power_circuit_active = True
    min_level = 1
    max_level = 12

    def __init__(self, password, level=4):
        if password != type(self).__maintenance_password:
            raise PermissionError("bad password")
        self._validate_level(level)
        self._level = level
        self.doors_open = False
        self.moving = False

    @classmethod
    def diagnostic_report(cls):
        """Return shared elevator configuration and power information."""
        return {
            "power_circuit_active": cls.power_circuit_active,
            "service_levels": f"{cls.min_level}–{cls.max_level}",
        }

    def _validate_level(self, level):
        if isinstance(level, bool) or not isinstance(level, int):
            raise TypeError("level must be an integer")
        if not self.min_level <= level <= self.max_level:
            raise ValueError(
                f"level must be between {self.min_level} and {self.max_level}"
            )

    def open_doors(self):
        if self.moving:
            raise RuntimeError("cannot open doors while the elevator is moving")
        self.doors_open = True
        return f"Doors open at level {self._level}."

    def close_doors(self):
        self.doors_open = False
        return "Doors closed."

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, destination):
        """Move the elevator to ``destination`` and return a status message."""
        self._validate_level(destination)
        if not type(self).power_circuit_active:
            raise RuntimeError("power circuit is inactive")
        if self.doors_open:
            raise RuntimeError("close the doors before moving")
        if destination == self._level:
            return f"Already at level {self._level}."

        direction = "up" if destination > self._level else "down"
        self.moving = True
        start = self._level
        self._level = destination
        self.moving = False
        print( f"Moving {direction} from level {start} to level {self._level}.")
        start = self._level
        self._level = destination
        self.moving = False
        self.open_doors()
        return f"Moved {direction} from level {start} to level {self._level}."

    def __repr__(self):
        door_state = "open" if self.doors_open else "closed"
        return f"<Elevator level={self._level} doors={door_state}>"
