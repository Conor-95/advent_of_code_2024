def is_safe(levels):
    increasing = all(1 <= levels[i + 1] - levels[i] <= 3 for i in range(len(levels) - 1))
    decreasing = all(1 <= levels[i] - levels[i + 1] <= 3 for i in range(len(levels) - 1))
    return increasing or decreasing


def check_with_dampener(levels):
    if is_safe(levels):
        return True


    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i + 1:]
        if is_safe(new_levels):
            return True

    return False

f = open("puzzle_input.txt", "r")
reports = []
safe_reports = []
for line in f:
    line = line.strip()
    line = line.split(" ")
    for index in range(len(line)):
        line[index] = int(line[index])
    reports.append(line)

for report in reports:
     if check_with_dampener(report):
         safe_reports.append(report)
         continue

print(len(safe_reports))












