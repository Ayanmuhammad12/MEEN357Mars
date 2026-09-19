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



def get_gear_ratio():
    #Returns the speed reduction ratio
    return


def tau_dcmotor():
    #Returns the motor shaft torque given shaft speed and motor specs
    return


def F_drive():
    #Returns the force applied to the rover by the drive system given drive system and shaft speed
    return
 

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


print(get_mass(rover))