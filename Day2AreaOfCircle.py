#Create a program to calculate the area of a circle given its radius
from math import pi

radius = float(input('Enter value of radius: '))
area=pi*radius**2
print("Area of Circle with radius "+str(radius)+" is: "+str(round(area,2)))

#plot the circle using matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

center = (0.5, 0.5)
circle = Circle(center, radius)
fig, ax = plt.subplots()
ax.add_patch(circle)
ax.set_aspect('equal')
#ax.set_box_aspect(0.5)
ax.autoscale()
plt.show()