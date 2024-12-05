f = open("puzzle_input.txt", "r")

locations_1 = []
locations_2 = []
distance = []
for lines in f:
    line = lines.strip()
    line = line.split("   ")
    locations_1.append(int(line[0]))
    locations_2.append(int(line[1]))
similarity_score = 0
for location in locations_1:
    if location in locations_2:
        count = locations_2.count(location)
        similarity_score += (location * count)

print(similarity_score)
