import numpy as np
import matplotlib.pyplot as plt

h = 0.01  # Step size
xn = 100  # Number of points in x direction
yn = 40   # Number of points in y direction

# Initialize potential matrix
phi = np.zeros([xn, yn])

# Set potential to 1000 between (20,20) and (100,20)
for i in range(20, 100):
    phi[i][20] = int(1000)
phi01 = phi

# Set potential to 1000 between (20,20) and (20,40)
for i in range(20, 40):
    phi[20][i] = 1000

# Linear potential along x direction from (0,0) to (99,0)
x = 0
phi02 = phi
for i in range(20):
    phi[99][i] = x
    x = x + 50

# Set potential to 1000 between (0,39) and (20,39)
phi03 = phi
for i in range(20):
    phi[i][39] = 1000

phi04 = phi

# Solve Poisson's equation iteratively
for k in range(200):
    for i in range(99):
        if i < 20:
            end = 39
        else:
            end = 20
        for j in range(1, end):
            if i == 0:
                u = (1/6)*(4*phi[i+1][j] + phi[i][j+1] + phi[i][j-1])
            else:
                u = (1/4)*(phi[i+1][j] + phi[i-1][j] + phi[i][j+1] + phi[i][j-1]) + (1/(8*i))*(phi[i+1][j] - phi[i-1][j])
            phi[i][j] = phi[i][j] + 1.5*(u - phi[i][j])

# Mirror the potential matrix and concatenate to get a symmetric potential
phi1 = np.zeros([xn, yn])
for i in range(100):
    phi1[i] = phi[99-i]
phi = np.vstack((phi1, phi))
phi1 = np.zeros([2*xn, yn])
phi2 = -phi
for i in range(40):
    phi1[:, i] = phi2[:, 39-i]
phi = np.concatenate((phi1, phi), axis=1)

# Plot equipotential lines
ra = [-1000, -800, -600, -400, -200, 200, 400, 600, 800, 1000]
for k in ra:
    x = []
    y = []
    for i in range(200):
        for j in range(80):
            if phi[i][j] > (k-5) and phi[i][j] < (k+5):
                x.append(j)
                y.append(i)
    plt.plot(x, y, color='b')

plt.show()
