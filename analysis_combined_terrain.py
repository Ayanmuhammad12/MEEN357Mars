import numpy as np
from subfunctions import F_net, get_gear_ratio
from scipy.optimize import bisect
import matplotlib.pyplot as plt

#define constants
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

#set up array
Crr_array = np.linspace(0.01,0.5,25)
slope_array_deg = np.linspace(-15,35,25)

Ng = get_gear_ratio(speed_reducer)
r = wheel['radius']
omega_noload = motor['speed_noload']

#set up matrix
CRR, SLOPE = np.meshgrid(Crr_array, slope_array_deg)

VMAX = np.zeros(np.shape(CRR), dtype = float)

#loop
N = np.shape(CRR)[0]
for i in range(N):
    for j in range(N):
        Crr_sample = float(CRR[i,j])
        slope_sample = float(SLOPE[i,j])
        def F_net_of_omega(omega):
            return F_net(np.array([omega]),np.array([slope_sample]),rover, planet, Crr_sample)[0]
        
        F_lo = F_net_of_omega(0.0)
        F_high = F_net_of_omega(omega_noload)
        if F_lo * F_high > 0:
            VMAX[i,j] = np.nan
        else:
            omega_root = bisect(F_net_of_omega, 0, omega_noload)
            VMAX[i,j] = omega_root * r / Ng


fig, ax = plt.subplots(figsize=(9,6))
cs = ax.contourf(CRR, SLOPE, VMAX, levels=20, cmap='viridis')
fig.colorbar(cs, label='Terminal Speed [m/s]')
ax.set_xlabel('Rolling Resistance Coefficient')
ax.set_ylabel('Terrain Slope [deg]')
ax.set_title('Terminal Speed vs Slope and Rolling Resistance')
fig.tight_layout()
fig.savefig('analysis_combined_terrain.png')
plt.close('all')
