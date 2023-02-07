import math

g = 9.81
v = 44
deg = 80
theta = (deg * (math.pi/180))
x = 0.5
y = 1

tan0 = math.tan(theta)
x2 = x*tan0
firstSection = y+x2

numerator = g*(x**2)
denominator = 2*((v*math.cos(theta))**2)

secondSection = (numerator/denominator)

print(firstSection - secondSection)
