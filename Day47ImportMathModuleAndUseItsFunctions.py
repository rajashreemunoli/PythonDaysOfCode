#Create a program that imports the math module and uses its functions
import math
try:
    xy_list=input("Enter the length of sides of triangle separated by comma: ").split(',')
    hyp=math.hypot(float(xy_list[0]),float(xy_list[1]))
    print("\nHypotenuse of the triangle=",hyp)
except:
    print("invalid entry")