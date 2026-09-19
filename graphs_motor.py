# graphs_motor.py
import numpy as np
import matplotlib.pyplot as plt
from subfunctions import tau_dcmotor

motor = {'torque_stall': 170, 'torque_noload': 0, 'speed_noload': 3.80, 'mass': 5.0}
omega = np.linspace(0, motor['speed_noload'], 100)
tau = tau_dcmotor(omega, motor)
power = tau * omega

fig, axes = plt.subplots(3, 1, figsize=(7, 10))

# speed vs torque
axes[0].plot(tau, omega)
axes[0].set_xlabel('Motor Shaft Torque [Nm]')
axes[0].set_ylabel('Motor Shaft Speed [rad/s]')
axes[0].set_title('Speed vs Torque')

# power vs torque
axes[1].plot(tau, power)
axes[1].set_xlabel('Motor Shaft Torque [Nm]')
axes[1].set_ylabel('Motor Power [W]')
axes[1].set_title('Power vs Torque')

#power vs speed
axes[2].plot(omega, power)
axes[2].set_xlabel('Motor Shaft Speed [rad/s]')
axes[2].set_ylabel('Motor Power [W]')
axes[2].set_title('Power vs Speed')

fig.tight_layout()
fig.savefig('graphs_motor.png')
plt.close('all')
