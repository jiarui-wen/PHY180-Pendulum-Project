import numpy

new = "length Q xerr yerr"
with open("TauToQ.txt", "r") as f:
    first = True
    for line in f:
        if first:
            first = False
            continue
        tau, err, length, T = line.rstrip().split()
        tau = float(tau)
        err = float(err)
        length = float(length)
        T = float(T)
        Q = numpy.pi * tau / T
        max_percent = max(err / tau, 0.0008 / T)
        yerr = max_percent * Q
        new += str(length) + " " + str(Q) + " " + str(0.0005) + " " + str(yerr) + "\n"

with open("QfactorVsLength.txt", "w") as f:
    f.write(new)