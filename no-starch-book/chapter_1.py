from pint import UnitRegistry
from numpy import pi,sin,cos
from numpy import sqrt

#1.1
print("1.1")
ureg = UnitRegistry()
units = UnitRegistry()

distance = 10 * ureg.meter
meters = ureg.meter
time = 5 * ureg.second

speed = distance / time 


print(speed)

#1.2
print("1.2")
answer = (sin(pi/4))**2 + (cos(pi/4))**2

print(answer)

#1.3
print("1.3")
foot = 12 * ureg.inch

h = 381 * meters

pole_height = foot * 10

h = 381 * meters
total_height = pole_height + h

print(total_height.to('feet'))

#1.4
#ignore  just an example

#1.5

meter = units.meter
second = units.second
meter_per_second = (units.meter / units.second**2) * 29
a = (9.8 * meter / second**2) + meter_per_second
print(a)
print("with out dropping")
print(a - meter_per_second)
a.magnitude
a.units


t = 3.4 * second



h = 381 * meter

t = sqrt(2 * h / a)

print("It was", t, "seconds to reach the ground")


#1.6
print("1.6")
meter = units.meter
second = units.second
g = 9.8 * meter / second**2  # acceleration due to gravity
terminal_velocity = 29 * meter / second  # terminal velocity
initial_height = 381 * meter

# Part 1: Time to reach terminal velocity
time_to_terminal = terminal_velocity.magnitude / g.magnitude * second
print(f"Time to reach terminal velocity: {time_to_terminal}")

# Part 2: Distance fallen during acceleration
distance_during_acceleration = 0.5 * g * time_to_terminal**2
print(f"Distance fallen during acceleration: {distance_during_acceleration}")

# Part 3: Remaining distance and time at terminal velocity
remaining_distance = initial_height - distance_during_acceleration
time_at_terminal = remaining_distance / terminal_velocity

# Total time
total_time = time_to_terminal + time_at_terminal
print(f"Total time to fall {initial_height}: {total_time}")

#1.7
print("1.7")

# Baseball pitch trajectory analysis
meter = units.meter
second = units.second

# Initial conditions
release_height = 2.0 * meter  # Typical pitcher release height
plate_height = 0.9 * meter    # Height of strike zone center
plate_distance = 18.44 * meter  # Distance from pitcher's mound to home plate
pitch_speed = 40 * meter / second  # ~90 mph fastball

# Time to reach home plate
time_to_plate = plate_distance / pitch_speed

# Calculate required initial vertical velocity for a straight-line path
height_difference = plate_height - release_height
initial_vertical_velocity = height_difference / time_to_plate

# Calculate the angle in degrees
angle_radians = sin(initial_vertical_velocity.magnitude / pitch_speed.magnitude)
angle_degrees = angle_radians * (180/pi)

print(f"\nBaseball Pitch Analysis:")
print(f"Time to reach plate: {time_to_plate:.3f}")
print(f"Required initial vertical velocity: {initial_vertical_velocity:.2f}")
print(f"Launch angle: {angle_degrees:.1f} degrees")

#1.8
print("1.8")

mile = units.mile
kilometer = units.kilometer
minute = units.minute

distance = 10 * kilometer
time = minute * 44.52
speed = distance / time
print(speed)

speed_in_miles = speed.to(mile / minute)
print(f"Speed converted to miles per minute: {speed_in_miles}")









