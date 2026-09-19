# graphs_sr.py
import numpy as np
import matplotlib.pyplot as plt
from subfunctions import tau_dcmotor, get_gear_ratio

motor = {'torque_stall': 170, 'torque_noload': 0, 'speed_noload': 3.80, 'mass': 5.0}
speed_reducer = {'type': 'reverted', 'diam_pinion': 0.04, 'diam_gear': 0.07, 'mass': 1.5}

Ng = get_gear_ratio(speed_reducer)

omega_motor = np.linspace(0, motor['speed_noload'], 100)
tau_motor = tau_dcmotor(omega_motor, motor)

tau_out = Ng * tau_motor
omega_out = omega_motor/Ng
power_out = omega_out * tau_out


fig, axes = plt.subplots(3, 1, figsize=(7, 10))

# speed vs torque
axes[0].plot(tau_out, omega_out)
axes[0].set_xlabel('Speed Reducer Output Torque [Nm]')
axes[0].set_ylabel('Speed Reducer Output Speed [rad/s]')
axes[0].set_title('Output Speed vs Output Torque')

# power vs torque
axes[1].plot(tau_out, power_out)
axes[1].set_xlabel('Speed Reducer Output Torque [Nm]')
axes[1].set_ylabel('Speed Reducer Output Power [W]')
axes[1].set_title('Output Power vs Output Torque')

#power vs speed
axes[2].plot(omega_out, power_out)
axes[2].set_xlabel('Speed Reducer Output Speed [rad/s]')
axes[2].set_ylabel('Speed Reducer Output Power [W]')
axes[2].set_title('Output Power vs Output Speed')

fig.tight_layout()
fig.savefig('graphs_sr.png')
plt.close('all')