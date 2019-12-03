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

def brute_force_cow_transport(cows, limit=10):
    power_list = sorted(get_partitions(cows), key=len)

    possibilities = []
    for i in power_list:
        ship = []
        for j in i:
            ship_weights = []
            for k in j:
                ship_weights.append(cows[k])
            ship.append(sum(ship_weights))
        if all(d <= limit for d in ship):
            possibilities.append(i)
    pruned_possibilities = []
    for k in possibilities:
        if k not in pruned_possibilities:
            pruned_possibilities.append(k)
    min_list_len = min(map(len, pruned_possibilities))
    for l in pruned_possibilities:
        if len(l) == min_list_len:
            return l

print("The result is :")
print(brute_force_cow_transport(cows, 10))
print("Trip numbers are :")
print(len(brute_force_cow_transport(cows, 10)))