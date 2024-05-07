import numpy as np
import matplotlib.pyplot as plt

# One Particle Simulation
num_particles_1 = 1
Beta_1 = 1
Energy_1 = 5
Num_mcs_1 = 10000
Energy_values_1 = [Energy_1]
Max_energy_change_1 = 2

for i in range(1, Num_mcs_1):
    energy_change = (2 * np.random.rand() - 1) * Max_energy_change_1
    energy_trial = Energy_1 + energy_change
    delta_energy = energy_trial - Energy_1
    if energy_trial > 0:
        if delta_energy < 0:
            Energy_1 = energy_trial
            Energy_values_1.append(Energy_1)
        else:
            w = np.exp(-Beta_1 * delta_energy)
            r = np.random.rand()
            if r < w:
                Energy_1 = energy_trial
                Energy_values_1.append(Energy_1)
            else:
                Energy_values_1.append(Energy_1)

# Energy Distribution for 1 Particle
X_1 = np.linspace(0, 10, 101)
Probability_1 = []
for i in range(len(X_1) - 1):
    count = 0
    for j in Energy_values_1:
        if j < X_1[i + 1] and j > X_1[i]:
            count += 1
    Probability_1.append(count)
X_1 = np.delete(X_1, [-1])

plt.plot(X_1, Probability_1)
plt.xlabel('Energy')
plt.ylabel('Distribution')
plt.title('Energy Distribution for 1 Particle')
plt.show()

# Multi-Particle Simulation
num_particles_2 = 10
Beta_2 = 0.4
Total_energy_2 = 0
Configurations_2 = np.full(num_particles_2, Total_energy_2 / num_particles_2)
Num_mcs_2 = 100000
Energy_values_2 = [Total_energy_2]
Max_energy_change_2 = 2

for i in range(1, Num_mcs_2):
    for j in range(1, num_particles_2 + 1):
        energy_change = (2 * np.random.rand() - 1) * Max_energy_change_2
        iparticle = np.random.randint(0, num_particles_2)
        energy_trial = Configurations_2[iparticle] + energy_change
        delta_energy = energy_trial - Configurations_2[iparticle]
        if energy_trial > 0:
            if delta_energy <= 0:
                Configurations_2[iparticle] = energy_trial
                Total_energy_2 += delta_energy
            else:
                w = np.exp(-Beta_2 * delta_energy)
                r = np.random.rand()
                if r < w:
                    Configurations_2[iparticle] = energy_trial
                    Total_energy_2 += delta_energy
    Energy_values_2.append(Total_energy_2)

# Energy Distribution for Multi-Particle System
X_2 = np.linspace(0, 100, 101)
Probability_2 = []
for i in range(len(X_2) - 1):
    count = 0
    for j in Energy_values_2:
        if j < X_2[i + 1] and j > X_2[i]:
            count += 1
    Probability_2.append(count)
X_2 = np.delete(X_2, [-1])

plt.plot(X_2, Probability_2)
plt.xlabel('Energy')
plt.ylabel('Distribution')
plt.title('Energy Distribution for Multi-Particle System')
plt.show()

# Simulation for Different Beta (Temperature)
num_particles_3 = 10
Beta_values_3 = np.linspace(0.5, 1.5, 10)
Total_energy_3 = 0
Configurations_3 = np.full(num_particles_3, Total_energy_3 / num_particles_3)
Num_mcs_3 = 100000
Energy_values_3 = [Total_energy_3]
Max_energy_change_3 = 2
Average_energy_values_3 = []

for k in range(len(Beta_values_3)):
    Total_energy_3 = 0
    for i in range(1, Num_mcs_3):
        Beta_3 = Beta_values_3[k]
        for j in range(1, num_particles_3 + 1):
            energy_change = (2 * np.random.rand() - 1) * Max_energy_change_3
            iparticle = np.random.randint(0, num_particles_3)
            energy_trial = Configurations_3[iparticle] + energy_change
            delta_energy = energy_trial - Configurations_3[iparticle]
            if energy_trial > 0:
                if delta_energy <= 0:
                    Configurations_3[iparticle] = energy_trial
                    Total_energy_3 += delta_energy
                else:
                    w = np.exp(-Beta_3 * delta_energy)
                    r = np.random.rand()
                    if r < w:
                        Configurations_3[iparticle] = energy_trial
                        Total_energy_3 += delta_energy
        Energy_values_3.append(Total_energy_3)
    average_energy = Total_energy_3 / Num_mcs_3
    Average_energy_values_3.append(average_energy)

# Plot Average Energy vs Temperature
Temperature_values_3 = 1 / Beta_values_3
plt.plot(Temperature_values_3, Average_energy_values_3)
plt.xlabel('Temperature')
plt.ylabel('Average Energy')
plt.title('Average Energy vs Temperature')
plt.show()

# Specific Heat Capacity Calculation
coefficients = np.polyfit(Temperature_values_3, Average_energy_values_3, 1)
specific_heat_capacity = coefficients[0]

print("Estimated specific heat capacity (Cv):", specific_heat_capacity)
