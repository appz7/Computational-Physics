import numpy as np
import matplotlib.pyplot as plt

left_boundary = -4  # Left boundary of the domain
right_boundary = 4   # Right boundary of the domain

# Function to compute wavefunction from the right boundary
def compute_wavefunction_right(e, target):
    step_size = 0.001
    x = -4
    s0 = 0
    s1 = 5
    wavefunction = [s0, s1]  # Initial conditions
    while x <= target + step_size:  # Iterating until reaching the target point t
        s2 = (2 - (step_size ** 2) * (e - 3 * (x ** 2))) * s1 - s0  # Update wavefunction
        wavefunction.append(s2)  # Appending the new value to the list
        s0 = s1
        s1 = s2
        x += step_size
    return wavefunction

# Function to compute wavefunction from the left boundary
def compute_wavefunction_left(e, target):
    step_size = 0.001
    x = 4
    s0 = 0
    s1 = 5
    wavefunction = [s0, s1]  # Initial conditions
    while x >= target - step_size:  # Iterating until reaching the target point t
        s2 = (2 - (step_size ** 2) * (e - 3 * (x ** 2))) * s1 - s0  # Update wavefunction
        wavefunction.append(s2)  # Appending the new value to the list
        s0 = s1
        s1 = s2
        x -= step_size
    return wavefunction

# Generating energy values
energies = np.arange(1, 15, 0.1)  

# Lists to store differences between wavefunctions
differences = []

# Computing difference for each energy value
for energy in energies:
    turning_point = (energy / 3) ** 0.5
    wavefunction_right = np.array(compute_wavefunction_right(energy, turning_point))
    wavefunction_left = np.array(compute_wavefunction_left(energy, turning_point))
    scale = wavefunction_right[-2] / wavefunction_left[-2]
    wavefunction_left = wavefunction_left * scale
    difference = wavefunction_left[-1] - wavefunction_right[-3]
    differences.append(difference)

# Function to compute difference
def compute_difference(energy):
    turning_point = (energy / 3) ** 0.5
    wavefunction_right = np.array(compute_wavefunction_right(energy, turning_point))
    wavefunction_left = np.array(compute_wavefunction_left(energy, turning_point))
    scale = wavefunction_right[-2] / wavefunction_left[-2]
    wavefunction_left = wavefunction_left * scale
    difference = wavefunction_left[-1] - wavefunction_right[-3]
    return difference

# Plotting energy versus difference
plt.plot(energies, differences)
plt.xlabel('energy')
plt.ylabel('difference of wavefunction')
plt.show()

# Function to find eigenvalue and eigenfunction
def find_eigen(e):
    step_size = 0.001
    x = -3.998
    s0 = 0
    s1 = 1
    x_points = [x, -3.999]
    wavefunction = [s0, s1]  # Initial conditions
    while x < 3:  # Iterating until reaching the right boundary
        s2 = (2 - (step_size ** 2) * (e - 3 * (x ** 2))) * s1 - s0  # Update wavefunction
        wavefunction.append(s2)  # Appending the new value to the list
        s0 = s1
        s1 = s2
        x_points.append(x)
        x += step_size
    return x_points, wavefunction

# Initial guesses for eigenvalues
initial_guess_1 = 1.6
s1 = compute_difference(initial_guess_1)
initial_guess_2 = 2
s2 = compute_difference(initial_guess_2)
next_guess = (initial_guess_2 * s1 - initial_guess_1 * s2) / (s1 - s2)

# Iteratively refining eigenvalue
while abs(next_guess - initial_guess_2) > 0.00001:
    initial_guess_1 = initial_guess_2
    initial_guess_2 = next_guess
    s2 = compute_difference(initial_guess_2)
    s1 = compute_difference(initial_guess_1)
    next_guess = (initial_guess_2 * s1 - initial_guess_1 * s2) / (s1 - s2)

# Plotting the eigenfunction
x_values, eigenfunction = find_eigen(next_guess)
plt.plot(x_values, eigenfunction)
plt.show()
