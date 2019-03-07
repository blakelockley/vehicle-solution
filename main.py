from vehicle import Vehicle
from solver import find_solution

def main(args):
    if len(args) < 2:
        usage(args)
        return

    # Dispatch
    command = args[1]
    command_map = {"run": run, "find": find, 'trace': trace}

    procedure = command_map.get(command, usage)
    procedure(args)


def usage(args):
    print("usage: %s [run instruction_string] | [find final_position]", args[0])


def run(args):
    vehicle = Vehicle()
    instructions = args[2]

    vehicle.read_string(instructions)
    print("Final position: ", vehicle.position)


def find(args):
    final_position = int(args[2])
    solution = find_solution(final_position)
    print("Solution:", solution)


def trace(args):
    vehicle = Vehicle()
    instructions = args[2]

    trace = vehicle.trace_string(instructions)
    instructions, positions, velocities = zip(*trace)

    print("     +" + "-" * (len(trace) * 6 - 1) + "+")
    print("     |", " | ".join(map(lambda x: x.center(3), instructions)), "|")
    print("     +" + "-" * (len(trace) * 6 - 1) + "+")
    print("vel: |", " | ".join(map(lambda x: str(x).center(3), velocities)), "|")
    print("pos: |", " | ".join(map(lambda x: str(x).center(3), positions)), "|")
    print("     +" + "-" * (len(trace) * 6 - 1) + "+")

    print("Final position: ", vehicle.position)


if __name__ == "__main__":
    import sys
    main(sys.argv)