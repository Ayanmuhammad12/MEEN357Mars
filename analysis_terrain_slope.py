import numpy as np
from subfunctions import F_net, get_gear_ratio
from scipy.optimize import bisect
import matplotlib.pyplot as plt

motor = {'torque_stall': 170, 
         'torque_noload': 0, 
         'speed_noload': 3.80, 
         'mass': 5.0}
wheel = {'radius': 0.30, 'mass': 1.0}
speed_reducer = {'type': 'reverted', 
                 'diam_pinion': 0.04, 
                 'diam_gear': 0.07, 
                 'mass': 1.5}
wheel_assembly = {'wheel': wheel, 
                  'speed_reducer': speed_reducer, 
                  'motor': motor}
rover = {'wheel_assembly': wheel_assembly,
         'chassis': {'mass': 659},
         'science_payload': {'mass': 75},
         'power_subsys': {'mass': 90}}
planet = {'g': 3.72}

Crr = 0.15
slope_array_deg = np.linspace(-15,35,25)

Ng = get_gear_ratio(speed_reducer)
r = wheel['radius']
omega_noload = motor['speed_noload']

v_max = np.zeros(len(slope_array_deg))

for i,slope in enumerate(slope_array_deg):
    def F_net_of_omega(omega):
        return F_net(np.array([omega]),np.array([slope]),rover, planet, Crr)[0]

    F_lo = F_net_of_omega(0.0)
    F_high = F_net_of_omega(omega_noload)

    if F_lo * F_high > 0:
        v_max[i] = np.nan
    else:
        omega_root = bisect(F_net_of_omega, 0, omega_noload)
        v_max[i] = omega_root * r / Ng

fig, ax = plt.subplots(figsize=(8,5))
ax.plot(slope_array_deg, v_max, marker ='o')
ax.set_xlabel('Terrain Slope [deg]')
ax.set_ylabel('Max Rover Velocity [m/s]')
ax.set_title('Terminal Speed vs Terrain Slope')
ax.grid(True)
fig.tight_layout()
fig.savefig('analysis_terrain_slope.png')
plt.close('all')

