new = ""
with open("tAmp.txt", "r") as f:
    for line in f:
        new += line.rstrip() + " " + str(0.0008) + " " + str(0.008) + "\n"

with open("tAmp.txt", "w") as f:
    f.write(new)