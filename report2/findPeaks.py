from scipy.signal import find_peaks

amps = []
times = []
first_line = True
with open("8055amp.txt", "r") as f:
    for line in f:
        if first_line:
            first_line = False
            continue
        t, a, xerr, yerr = line.rstrip().split()
        amps.append(a)
        times.append(t)

peaks, _ = find_peaks(amps)

new = "t amplitude xerr yerr\n"
for i in peaks:
    new += str(times[i]) + " " + str(amps[i]) + " " + str(0.0008) + " " + str(0.008) + "\n"
with open("8055peaks.txt", "w") as f:
    f.write(new)