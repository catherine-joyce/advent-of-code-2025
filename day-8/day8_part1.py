import math

coordinates = [
    [162, 817, 812],
    [57, 618, 57],
    [906, 360, 560],
    [592, 479, 940],
    [352, 342, 300],
    [466, 668, 158],
    [542, 29, 236],
    [431, 825, 988],
    [739, 650, 466],
    [52, 470, 668],
    [216, 146, 977],
    [819, 987, 18],
    [117, 168, 530],
    [805, 96, 715],
    [346, 949, 466],
    [970, 615, 88],
    [941, 993, 340],
    [862, 61, 35],
    [984, 92, 344],
    [425, 690, 689],
]
distances = {}
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        x1, y1, z1 = coordinates[i]
        x2, y2, z2 = coordinates[j]
        dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
        distances[(i, j)] = dist
print(distances)

sorted_distances = sorted(distances.items(), key=lambda x: x[1])

for (i, j), dist in sorted_distances[:10]:
    print(f"Points {i} and {j}: distance = {dist}")
