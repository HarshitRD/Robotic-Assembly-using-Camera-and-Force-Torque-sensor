import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
time_steps = 100  # Number of simulation steps
force_Rz = 1.0  # Simulated constant reaction force in Z direction (N)
m_x = 0.5  # Simulated torque around X (Nm)
m_y = 0.5  # Simulated torque around Y (Nm)

# Function to calculate the position vector p_R
def calculate_pR(m_x, m_y, f_Rz):
    """Calculate the position vector p_R based on moments and force."""
    if f_Rz != 0:  # Avoid division by zero
        p_R = np.array([-m_y / f_Rz, m_x / f_Rz])
        return p_R
    else:
        return None  # Handle the case where f_Rz is zero

# Simulate robot movements and calculations
positions = []
for step in range(time_steps):
    # Example of modifying force and torque values dynamically
    if step < time_steps // 2:
        force_Rz = 1.0 + 0.01 * step  # Gradually increasing force
    else:
        force_Rz = 1.5  # Steady force in the second half

    # Calculate position vector p_R
    p_R = calculate_pR(m_x, m_y, force_Rz)
    
    if p_R is not None:
        positions.append(p_R)
        print(f"Step {step + 1}: Position vector p_R: {p_R}")
    else:
        print(f"Step {step + 1}: Invalid force input")

# Convert positions list to a NumPy array for plotting
positions = np.array(positions)

# Visualize the results
plt.figure(figsize=(10, 6))
plt.plot(positions[:, 0], positions[:, 1], marker='o', linestyle='-', color='b', markersize=5)
plt.title('Simulated Position Vector p_R Over Time')
plt.xlabel('p_R_x (m)')
plt.ylabel('p_R_y (m)')
plt.grid()
plt.axis('equal')
plt.xlim(-1, 1)  # Set x limits for better visualization
plt.ylim(-1, 1)  # Set y limits for better visualization
plt.axhline(0, color='k', lw=0.5, ls='--')  # Add a horizontal line at y=0
plt.axvline(0, color='k', lw=0.5, ls='--')  # Add a vertical line at x=0
plt.show()

