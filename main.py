import math
import matplotlib.pyplot as plt

n = int(input("Enter Total number of Forces : "))

# Variables
i, Efx, Efy, forces, angles = 0, 0, 0, [], []

while i < n:
    force = int(input(f"Enter Value of Force {i + 1} : "))
    angle = math.radians(int(input(f"Enter Value of Angle {i + 1} w.r.t X-Axis : ")))
    forces.append(force)
    angles.append(angle)
    Efx = Efx + forces[i] * math.cos(angles[i])
    Efy += forces[i] * math.sin(angles[i])
    plt.arrow(0, 0, forces[i] * math.cos(angles[i]), forces[i] * math.sin(angles[i]), width=0.3, color='blue')
    i += 1

Resultant = round(math.sqrt((Efx ** 2) + (Efy ** 2)), 2)
direction = round(math.degrees(math.atan(Efy / Efx)), 2)

# X-Axis
plt.hlines(0, -abs(max(Efx, Efy, max(forces))), abs(max(Efx, Efy, max(forces))), color='black')
# Y-Axis
plt.vlines(0, -abs(max(Efx, Efy, max(forces))), abs(max(Efx, Efy, max(forces))), color='black')

# Resultant vector
plt.arrow(0, 0, Efx, Efy, width=0.4, color='red')
plt.title("Force Vectors")

print(f'\nSummation of Forces along X-axis = {round(Efx, 2)} N')
print(f'Summation of Forces along Y-axis = {round(Efy, 2)} N')
print(f'Magnitude of Resultant = {Resultant} N')
print(f'Direction of Resultant = {direction} °')
plt.show()
