import math as m

n = int(input("Enter Total number of Forces : "))
i = 0
forces = []
angle = []
Efx = 0
Efy = 0

while i < n:
    f = int(input(f"Enter Value of Force {i+1} : "))
    a = m.radians(int(input(f"Enter Value of Angle {i+1} w.r.t X-Axis : ")))
    forces.append(f)
    angle.append(a)
    Efx = Efx + forces[i] * m.cos(angle[i])
    Efy += forces[i] * m.sin(angle[i])
    i += 1

Resultant = m.sqrt((Efx**2) + (Efy**2))
direction = m.degrees(m.atan(Efy/Efx))

print(f'\nSummation of Forces along X-axis = {Efx} N')
print(f'Summation of Forces along Y-axis = {Efy} N')
print(f'Magnitude of Resultant = {Resultant} N')
print(f'Direction of Resultant = {direction} °')
