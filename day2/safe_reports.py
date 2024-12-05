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
        continue

unsafe_reports = []
for report2 in safe_reports:
        for i in range(len(report2)-1):
            if report2[i] +1 == report2[i+1] or report2[i] +2 == report2[i+1] or report2[i] +3 == report2[i+1]:
                continue
            elif report2[i] -1 == report2[i+1] or report2[i] -2 == report2[i+1] or report2[i] -3 == report2[i+1]:
                continue
            else:
                unsafe_reports.append(report2)
                break



print(len(safe_reports)-len(unsafe_reports))


