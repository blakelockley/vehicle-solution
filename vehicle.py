# The Vehicle is a simple car existing on a 1D road.

# The Vehicle has two attirbutes to its state:
#   - Position: How far along the vechile is
#   - Velocity: The speed and direction (+/-) it is travelling 

# The Vehicle can be be given one of two intructions:
#   - Accelerate (A): The speed of the vehicle increases by 1
#   - Reverse (R): The vehicle comes to a hault and the direction of the vehicle is reversed

# Every time an instruction is read, the position of
#   the vechile will be updated by the current velocity

from collections import namedtuple

class Vehicle:
    _position  = 0
    _velocity  = 0
    _direction = 1

    @property
    def position(self):
        return self._position

    @property
    def velocity(self):
        return self._velocity

    def read_instruction(self, inst):
        if inst == 'A':
            self._velocity += self._direction

        elif inst == 'R':
            self._velocity = 0
            self._direction *= -1

        else:
            raise ValueError("Unexpected instruction.")

        self._position += self._velocity


    def read_string(self, string):
        for inst in string:
            self.read_instruction(inst)


    def trace_string(self, string):
        TraceItem = namedtuple('TraceItem', ['instruction', 'position', 'velocity'])
        trace = []

        trace.append(TraceItem('I', self.position, self.velocity))

        for inst in string:
            self.read_instruction(inst)
            trace.append(TraceItem(inst, self.position, self.velocity))

        return trace

