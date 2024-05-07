import numpy as np
import matplotlib.pyplot as plt

# Number of total particles
total_particles = 4

# Initialize arrays for particles in the right and left compartments
particles_right = np.full(total_particles, 1)
particles_left = np.zeros(total_particles)

# Number of configurations
num_configurations = 20
num_comparisons = (num_configurations * (num_configurations - 1)) / 2

# List to store the number of particles on the left
num_left_particles_list = []

# List to store the entropy values
entropy_values = []

# Iterate over possible number of particles on the left
for num_left_particles in range(total_particles + 1):
    num_left_particles_list.append(num_left_particles)
    
    # Array to store configurations
    configurations = np.zeros(num_configurations)
    
    # Generate configurations
    for config_index in range(num_configurations):
        configuration = 0
        count = 0
        
        # Assign particles to the left compartment randomly
        while count <= num_left_particles - 1:
            random_index = np.random.randint(0, total_particles)
            if particles_left[random_index] != 1:
                particles_left[random_index] = 1
                count += 1
        
        # Convert the configuration to a decimal number
        for particle_index in range(len(particles_left)):
            if particles_left[particle_index] == 1:
                configuration += (2 ** particle_index)
        
        # Reset particle arrays for the next configuration
        particles_right = np.full(total_particles, 1)
        particles_left = np.zeros(total_particles)
        
        # Store the configuration
        configurations[config_index] = configuration
    
    # Find unique configurations
    unique_configurations = []
    for config in configurations:
        is_unique = 0
        
        # Loop to check uniqueness
        for unique_config in unique_configurations:
            if config == unique_config:
                is_unique = 1
                break
        
        if is_unique==0:
            unique_configurations.append(config)
    
    # Calculate entropy
    num_coincidence = 0
    for unique_config in unique_configurations:
        num_occurrences = 0
        for config in configurations:
            if unique_config == config:
                num_occurrences += 1
        num_coincidence += (num_occurrences * (num_occurrences - 1)) / 2

    # Calculate the relative number
    relative_number = num_coincidence / num_comparisons
    tau = 1 / relative_number
    
    # Calculate entropy and append to the list
    entropy_values.append(np.log(tau))

# Plotting the results
plt.plot(num_left_particles_list, entropy_values)
plt.xlabel('Number of particles on the left')
plt.ylabel('Entropy')
plt.show()
