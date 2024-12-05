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
    if report == sorted(report) or report == sorted(report, reverse=True):
        safe_reports.append(report)
    else:
        for i in range(len(report)-1):









