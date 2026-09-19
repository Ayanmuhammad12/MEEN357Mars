#subfunctions 
### SIGN CONVENTION: POSITIVE (FORWARD OR DOWNHILL) ; NEGATIVE (BACKWARD OR UPHILL)###
import numpy as np
from math import erf

#defining rover dict for testing
# --- Rover component dicts ---

motor = {
    'torque_stall':  170,    # Nm
    'torque_noload':   0,    # Nm
    'speed_noload':  3.80,   # rad/s
    'mass':          5.0     # kg
}
wheel = {
    'radius': 0.30,   # m
    'mass':   1.0     # kg
}
speed_reducer = {
    'type':        'reverted',
    'diam_pinion': 0.04,   # m
    'diam_gear':   0.07,   # m
    'mass':        1.5     # kg
}
wheel_assembly = {
    'wheel':         wheel,
    'speed_reducer': speed_reducer,
    'motor':         motor
}
chassis         = {'mass': 659}   # kg
science_payload = {'mass':  75}   # kg
power_subsys    = {'mass':  90}   # kg
rover = {
    'wheel_assembly':  wheel_assembly,
    'chassis':         chassis,
    'science_payload': science_payload,
    'power_subsys':    power_subsys
}
# --- Planet dict (separate from rover) ---
planet = {'g': 3.72}   # m/s^2, Mars gravity


def get_mass(rover):
    #Computes total mass of rover
    if type(rover) != dict:
        raise Exception('Input rover must be a dict')
    
    #finding mass
    chassis_mass = rover['chassis']['mass']
    wheel_mass = rover['wheel_assembly']['wheel']['mass']
    motor_mass = rover['wheel_assembly']['motor']['mass']
    payload_mass = rover['science_payload']['mass']
    reducer_mass = rover['wheel_assembly']['speed_reducer']['mass']
    power_mass = rover['power_subsys']['mass']
    m = chassis_mass + payload_mass + power_mass + (6 * (wheel_mass + motor_mass + reducer_mass))

    return m



def get_gear_ratio(speed_reducer):
    #Returns the speed reduction ratio
    if type(speed_reducer) != dict:
            raise Exception('Input speed_reducer must be a dict')

    #checing if 'type' = 'reverted'
    if speed_reducer['type'].lower() != 'reverted':
        raise Exception('type of reducer is not what is expected')

    #reducer
    pinion_diam = speed_reducer['diam_pinion']
    gear_diam = speed_reducer['diam_gear']
    Ng = (gear_diam/pinion_diam)**2
    return Ng


def tau_dcmotor(omega,motor):
    #Returns the motor shaft torque given shaft speed and motor specs
    if type(motor) != dict:
        raise Exception('Input motor must be a dict')
    if not isinstance(omega, (int, float, np.ndarray)):
        raise Exception('Input omega must be a scalar or a numpy array')

    tau_stall = motor['torque_stall']
    tau_noload = motor['torque_noload']
    omega_noload = motor['speed_noload']
    slope = ((tau_stall-tau_noload)/omega_noload)

    #torque if scalar
    if isinstance(omega, (int, float)):
         if omega < 0:
              return float(tau_stall)
         elif omega > omega_noload:
              return 0.0
         else:
              return float(tau_stall - (slope * omega))

    #torque for array
    tau = tau_stall - (slope * omega)
    tau[omega < 0] = tau_stall
    tau [omega > omega_noload] = 0

    return tau


def F_drive(omega,rover):
    #Returns the force applied to the rover by the drive system given drive system and shaft speed
    if type(rover) != dict:
        raise Exception('Input rover must be a dict')
    if not isinstance(omega, (int, float, np.ndarray)):
        raise Exception('Input omega must be a scalar or a numpy array')

    motor = rover['wheel_assembly']['motor']
    speed_reducer = rover['wheel_assembly']['speed_reducer']
    r = rover['wheel_assembly']['wheel']['radius']
    Ng = get_gear_ratio(speed_reducer)
    tau = tau_dcmotor(omega,motor)

    Fd = 6 * (Ng * tau)/r

    return Fd
 

def F_gravity():
    #magnitude of the force component acting on the rover in the direction of its
#translational motion due to gravity as a function of terrain inclination angle and rover
#properties
    return

def F_rolling():
    #magnitude of force component due to rolling resistances given the terrain inclination angle, rover properties, and a
#rolling resistance coefficient

    return

def F_net():
    # magnitude of net force acting on the rover
    return
