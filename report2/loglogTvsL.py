import math

first_line = True
length = []
period = []
res = "logl logt xerr yerr\n"

with open("PeriodVsLength.txt", "r") as f:
    for line in f:
        if first_line:
            first_line = False
            continue
        l, t, xerr, yerr = line.rstrip().split()
        l = float(l)
        t = float(t)
        xerr = float(xerr)
        yerr = float(yerr)
        logl = math.log(l)
        logt = math.log(t)

        xerr = abs(xerr/l * logl)
        yerr = abs(yerr/t * logt)
        res += str(logl) + " " + str(logt) + " " + str(xerr) + " " + str(yerr) + "\n"

with open("logTvsL.txt", "w") as file:
    file.write(res)

