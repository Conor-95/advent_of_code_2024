f = open("puzzle_input.txt", "r")

locations_1 = []
locations_2 = []
distance = []
for lines in f:
    line = lines.strip()
    line = line.split("   ")
    locations_1.append(int(line[0]))
    locations_2.append(int(line[1]))

locations_1.sort()
locations_2.sort()
index = 0

for location in locations_1:

    if locations_1[index] >= locations_2[index]:
        distance.append(locations_1[index] - locations_2[index])
        index = index + 1
    else:
        distance.append(locations_2[index] - locations_1[index])
        index = index + 1


total_distance = sum(distance)
print(total_distance)