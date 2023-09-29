# Arguments for the constructor
# radius -> integer or float (do not round it)
# mass -> integer or float (do not round it)
# Methods to be defined
# get_radius()       =>  radius of the Sphere (do not round it)
# get_mass()         =>  mass of the Sphere (do not round it)
# get_volume()       =>  volume of the Sphere (rounded to 5 place after the decimal)
# get_surface_area() =>  surface area of the Sphere (rounded to 5 place after the decimal)
# get_density()      =>  density of the Sphere (rounded to 5 place after the decimal)

class Sphere(object):
    def __init__(self, rad, mass):
        self.rad = rad
        self.mass = mass

    def get_radius(self):
        return self.rad

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round((4 / 3) * 3.1415926535 * self.rad ** 3, 5)

    def get_surface_area(self):
        return round(4 * 3.1415926535 * self.rad ** 2, 5)

    def get_density(self):
        v = round((4 / 3) * 3.1415926535 * self.rad ** 3, 5)
        return round(self.mass / v, 5)