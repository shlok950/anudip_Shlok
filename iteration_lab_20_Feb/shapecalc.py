# 1. create a module that contains the functions to perform all the operation on threedfigures(cube,cuboid,cylinder,cone,sphere,hemisphere).
#2. create a python program to find out curvedsurfacearea, totalsurfacearea and volume of cylinder.
#3. create a python program to find out curvedsurfacearea, totalsurfacearea and volume of cone.
#4. create a python program to find out curvedsurfacearea, totalsurfacearea and volume of cuboid.
import math

def calculate_cube(side):
    print("surface_area is : ", 6 * (side ** 2))
    print("volume is : ", side ** 3)
    #surface_area = 6 * (side ** 2)
    #volume = side ** 3
    #return surface_area, volume


def calculate_cuboid(length, width, height):
    print("surface_area is : ", 2 * ((length * width) + (length * height) + (width * height)))
    print("volume is : ", length * width * height)
    #surface_area = 2 * ((length * width) + (length * height) + (width * height))
    #volume = length * width * height
    #return surface_area, volume


def calculate_cylinder(radius, height):
    print("curved_surface_area is : ", 2 * math.pi * radius * height)
    print("total_surface_area is : ", 2 * math.pi * radius * height + 2 * math.pi * (radius ** 2))
    print("volume is : ", math.pi * (radius ** 2) * height)
    #curved_surface_area = 2 * math.pi * radius * height
    #total_surface_area = curved_surface_area + 2 * math.pi * (radius ** 2)
    #volume = math.pi * (radius ** 2) * height
    #return curved_surface_area, total_surface_area, volume


def calculate_cone(radius, height):
    print("curved_surface_area is : ", math.pi * radius * math.sqrt(radius ** 2 + height ** 2))
    print("total_surface_area is : ", math.pi * radius * math.sqrt(radius ** 2 + height ** 2) + math.pi * (radius ** 2))
    print("volume is : ", (1/3) * math.pi * (radius ** 2) * height)
    #slant_height = math.sqrt(radius ** 2 + height ** 2)
    #curved_surface_area = math.pi * radius * slant_height
    #total_surface_area = curved_surface_area + math.pi * (radius ** 2)
    #volume = (1/3) * math.pi * (radius ** 2) * height
    #return curved_surface_area, total_surface_area, volume


def calculate_sphere(radius):
    print("surface_area is : ", 4 * math.pi * (radius ** 2))
    print("volume is : ", (4/3) * math.pi * (radius ** 3))
    #surface_area = 4 * math.pi * (radius ** 2)
    #volume = (4/3) * math.pi * (radius ** 3)
    #return surface_area, surface_area, volume


def calculate_hemisphere(radius):
    print("surface_area is : ", 3 * math.pi * (radius ** 2))
    print("volume is : ", (2/3) * math.pi * (radius ** 3))
    print("curved_surface_area is : ", 2 * math.pi * (radius ** 2))
    print("total_surface_area is : ", 3 * math.pi * (radius ** 2))
    #surface_area = 3 * math.pi * (radius ** 2)
    #curved_surface_area = 2 * math.pi * (radius ** 2)
    #total_surface_area = curved_surface_area + math.pi * (radius ** 2)
    #volume = (2/3) * math.pi * (radius ** 3)
    #return curved_surface_area, total_surface_area, volume