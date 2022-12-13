# camryn echevarria
# 11/15/2022

# problem 1 is to find the radius of the circle.
# Import statements should come first
import math


def area_circle():
    radius = int(input(" What is the radius you pick?"))
    area = math.pi * (radius ** 2)
    print(area)

area_circle()