# The Vehicle is a simple car existing on a 1D road.

# The Vehicle has two attirbutes to its state:
#   - Position: How far along the vechile is
#   - Velocity: The speed and direction (+/-) it is travelling 

# The Vehicle can be be given one of two intructions:
#   - Accelerate (A): The speed of the vehicle doubles
#   - Reverse (R): The speed of the vehicle is reversed

# Every time an before instruction is read, the position of
#   the vechile will be updated by the current velocity


class Vehicle:
    _position = 0
    _velocity = 1

    @property
    def position(self):
        return self._position

    @property
    def velocity(self):
        return self._velocity

    def read_instruction(self, inst):
        self._position += self._velocity

        if inst == 'A':
            self._velocity *= 2

        elif inst == 'R':
            self._velocity *= -1

        else:
            raise ValueError("Unexpected instruction.")


    def read_string(self, string):
        for inst in string:
            self.read_instruction(inst)

