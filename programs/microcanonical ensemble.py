import numpy as np
import random as rand
import matplotlib.pyplot as plt

num_particles = int(input('Input number of particles: '))
total_system_energy = float(input('Input total system energy: '))
V0 = np.sqrt(2 * total_system_energy / num_particles)
particles = [V0] * num_particles
particles = np.array(particles)
velocities = np.full(num_particles, V0)

demon_energy = 0
max_velocity_change = 2.0
convergence = 0
num_accepted = 0
max_iterations = 1000000
mean_energy = total_system_energy / num_particles
cumulative_energy = total_system_energy
temp_energy = total_system_energy
demon_sum_energy = 0
iteration_num = 0
system_energy_average = []
mean_velocity = []
demon_mean_energy = []
time = []
convergence_check = []

for j in range(1, max_iterations + 1):
    system_energy_average_val = cumulative_energy / j
    system_energy_average.append(system_energy_average_val)
    time.append(j)
    demon_energy_average = demon_sum_energy / j
    demon_mean_energy.append(demon_energy_average)
    mean_velocity.append((2 * (system_energy_average_val / num_particles) ** 0.5))
    convergence_diff = np.abs(temp_energy - system_energy_average_val)
    convergence_check.append(convergence_diff)
    
    if convergence_diff <= 1.0e-4:
        convergence += 1
    else:
        convergence = 0
    
    if convergence >= 10:
        print('The loop is breaking at', j)
        break
    
    temp_energy = system_energy_average_val
    for i in range(1, num_particles + 1):
        dV = (2 * rand.random() - 1) * max_velocity_change
        iparticle = rand.randint(0, num_particles - 1)
        V_trial = velocities[iparticle] + dV
        delta_E = 0.5 * (V_trial ** 2 - velocities[iparticle] ** 2)
        if delta_E <= demon_energy:
            velocities[iparticle] = V_trial
            num_accepted += 1
            demon_energy -= delta_E
            total_system_energy += delta_E
        
        iteration_num += 1
        
    mean_energy = total_system_energy / num_particles
    cumulative_energy += total_system_energy
    demon_sum_energy += demon_energy

acceptance_ratio = float(num_accepted) / (num_particles * max_iterations)
print('Acceptance Ratio =', acceptance_ratio)

# Plot average system energy, mean velocity, and demon mean energy
plt.plot(time, system_energy_average, label='Average Energy')
plt.legend()
plt.show()

plt.plot(time, mean_velocity, label='Mean Velocity')
plt.legend()
plt.show()

plt.plot(time, demon_mean_energy, label='Demon Mean Energy')
plt.legend()
plt.show()

print('Equilibrium mean velocity per particle is', mean_velocity[-1])
print('Mean energy of the demon is', demon_mean_energy[-1])
