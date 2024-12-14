import math

new = ""
with open("tAmp3.txt", "r") as f:
    for line in f:
        t, x, y = line.split()
        new += str(t) + " " + str(math.atan(float(x) / float(y))) + " " + str(0.0008) + " " + str(0.008) + "\n"

with open("tAmp3revised.txt", "w") as f:
    f.write(new)
