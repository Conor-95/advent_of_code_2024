import re

f = open("corrupt.txt", "r")
f = f.read()
do = re.split("do[(][)]", f)
dont = []
data = []
for line in do:
    dont = re.split("don't[(][)]", line)
    dont = dont[0]
    data.append(dont)
data = "".join(data)

print(data)

t = re.findall("mul[(][0-9]+,[0-9]+[)]", data)
calcs = []
for entry in t:
    entry = re.sub("mul", "", entry)
    entry = re.sub("[(]", "", entry)
    entry = re.sub("[)]", "", entry)
    entry = entry.split(",")
    calcs.append(entry)

answers = []
for calc in calcs:
    calc[0] = int(calc[0])
    calc[1] = int(calc[1])
    ans = calc[0] * calc[1]
    answers.append(ans)

total = sum(answers)
print(total)