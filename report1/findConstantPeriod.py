new = ""
with open("PeriodVsAngleData.txt", "r") as f:
    first = True
    for line in f:
        if first:
            first = False
            continue
        angle, period, xerr, yerr = line.rstrip().split()
        if float(angle) > -0.75 and float(angle) < 0.75:
            new += line

with open("Extracted.txt", "w") as f:
    f.write(new)