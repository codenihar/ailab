from itertools import permutations

distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

possibilities = list(permutations(range(len(distances))))
print(possibilities)
min_distance = 999
route = None
total_distance = 0
for each in possibilities:
    total_distance = 0
    for i in range(len(distances)-1):
        total_distance+=distances[each[i]][each[i+1]]
    total_distance+=distances[each[-1]][each[0]]
    if total_distance<min_distance:
        min_distance = total_distance
        route = each

print(min_distance)
print(route)
