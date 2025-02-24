from pint import UnitRegistry
from numpy import pi,sin,cos
from numpy import sqrt

#1.1
ureg = UnitRegistry()
units = UnitRegistry()

# distance = 10 * ureg.meter
# meters = ureg.meter
# time = 5 * ureg.second

# speed = distance / time 


# print(speed)

#1.2

# answer = (sin(pi/4))**2 + (cos(pi/4))**2

# print(answer)

#1.3
# foot = 12 * ureg.inch

# h = 381 * meters

# pole_height = foot * 10

# h = 381 * meters
# total_height = pole_height + h

# print(total_height.to('feet'))

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
# print(t)

# v = a * t

# print(v)