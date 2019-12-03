cows = {
    'Maggie' : 3, 'Herman' : 7, 'Besty' : 9, 'Oreo' : 6,
    'MooMoo': 3, 'Milkshake': 2, 'Millie' : 5, 'Lola': 2,
    'Florence' : 2, 'Henrietta' : 9
}

def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2 ** len(set_) // 2):
        parts = [set(), set()]
        for item in set_:
            parts[i & 1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]] + b

def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]

def greedy_cow_transport(cows, limit=10):
    trips = []
    cowsCopy = cows.copy()
    sortedCows = sorted(cowsCopy.items(), key=lambda x: x[1], reverse=True)
    while sum(cowsCopy.values()) > 0:
        ship = []
        total = 0
        for cow, value in sortedCows:
            if cowsCopy[cow] != 0 and value + total <= limit:
                ship.append(cow)
                total += value
                cowsCopy[cow] = 0
        trips.append(ship)
    return trips

print("The result is :")
print(greedy_cow_transport(cows, 10))
print("Trip numbers are :")
print(len(greedy_cow_transport(cows, 10)))