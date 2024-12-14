# Sample Python code to run the fit_black_box Python code relatively easily

import fit_black_box as bb
import math
import scipy
from sklearn.metrics import r2_score 

# First, define the function you want to fit. Here it's a linear function.
# It is critical that the independant variable ("t") is first in the list of function variables.



# Here's an exponential function where a is theta0 and b is tau



# Next, generate your data and errorbars. One way is to manually insert it here.

x = bb.np.array([0,1,2,3,4,5,6])
y = bb.np.array([0.1,0.9,2.1,2.9,4.1,4.9,6.1])
xerr = 0.05
yerr = bb.np.array([0.01,0.02,0.03,0.04,0.05,0.06,0.07])

# Note that xerr and yerr can either be an array of the same length as x&y, or a single value


# Now we make the plot, displayed on screen and saved in the directory, and print the best fit values

# bb.plot_fit(linear, x, y, xerr, yerr)


# Let's try again, this time loading from a file like a CSV file.
# NOTE: The CSV file should not have commas to separate things! Spaces or tabs are fine.

# Again, start with a fitting function. This time it is quadratic.

def quadratic(t, a, b, c):
    return a*t**2 + b*t + c


# Now load the data from the file. The file should be in the same directory as this Python code.
# Some chance you will need an absolute path: "C:\\Users\\Brian\\Python\\mydata_fake.txt"

# filename="mydata_fake.txt"
# x, y, xerr, yerr = bb.load_data(filename)

# This time, let's use every single possible option available to bb.plot_fit()

# init_guess = (-0.5, 0, +0.5) # guess for the best fit parameters
# font_size = 20
# xlabel = "Time (s)"
# ylabel = "Height (m)"

# Now we make the plot, displayed on screen and saved in the directory, and print the best fit values
# bb.plot_fit(quadratic, x, y, xerr, yerr, init_guess=init_guess, font_size=font_size,
#             xlabel=xlabel, ylabel=ylabel)

# Note: for sinusoidal functions, guessing the period correctly with init_guess is critical

# Fit the same data with an exponential function

def expon(t, a, b):
    return a*bb.np.exp(-t/b)

def exp_cos(t, a, b, T, C):
    return a*bb.np.exp(-t/b) * bb.np.cos(2*math.pi*t/T)

def power(t, a, b):
    return a*t**b

def linear(t, m, b):
    return m*t + b

filename="logTvsL.txt"
x, y, xerr, yerr = bb.load_data(filename)

# bb.plot_fit(expon, x, y, xerr, yerr, xlabel="Time Elapsed(s)", ylabel="Amplitude(rad)", title="")


# popt = bb.plot_fit(power, x, y, xerr, yerr, xlabel="Length (m)", ylabel="Q Factor (s)", title="")
popt = bb.plot_fit(linear, x, y, xerr, yerr, xlabel="Length (ln m)", ylabel="Period (ln s)", title="")


# r1 = scipy.stats.pearsonr(x, y)
# print("r1:", r1)

y_pred = []
for xi in x:
    # y_pred.append(popt[0] * xi**popt[1])
    y_pred.append(popt[0]*xi + popt[1])


r2power = r2_score(y, y_pred)
# print("r2power:", r2power)

