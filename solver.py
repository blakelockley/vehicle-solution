from vehicle import Vehicle

def build_permutations(symbols, limit):
    result = []

    def _build(current, depth):
        if len(current) == depth:
            result.append(current)
            return

        for s in symbols:
            _build(current + s, depth)

    for i in range(limit+1):
        _build("", i)

    return result


def find_solution(final_position):
    perms = build_permutations(['A', 'R'], 10)

    for p in perms:
        vehicle = Vehicle()
        vehicle.read_string(p)

        if vehicle.position == final_position:
            return p

    return None


