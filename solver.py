from itertools  import count
from vehicle    import Vehicle

def build_permutations(symbols, length):
    result = []

    def _build(current, depth):
        if len(current) == depth:
            result.append(current)
            return

        for s in symbols:
            _build(current + s, depth)

    _build("", length)
    return result


def all_permutations(symbols):
    for length in count(start=0, step=1):
        chunk = build_permutations(symbols, length)
        for item in chunk:
            yield item


def find_solution(final_position):
    perms = all_permutations(['A', 'R'])

    for p in perms:
        vehicle = Vehicle()
        vehicle.read_string(p)

        if vehicle.position == final_position:
            return p

    return None

