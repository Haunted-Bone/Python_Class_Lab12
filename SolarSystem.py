from Planet import Planet

from Sun import Sun

from Gravity import UniversalGravity as u
import math




class SolarSystem:
    def __init__(self):
        self.the_sun = None
        self.planets = []

    def get_sun(self):
        return self.the_sun

    def add_planet(self, new_planet: Planet):
        self.planets.append(new_planet)

    def add_sun(self, the_sun: Sun):
        self.the_sun = the_sun

    def get_planets(self):
        for planet in self.planets:
            return planet.name

    def show_planets(self):
        for planet in self.planets:
            print (planet)

    def move_planets(self):
        dt = .001  # Constant time interval for each solar system iteration.

        for planet in self.planets:
            # Move the distance covered in the interval dt
            planet.move_to(
                planet.get_x_pos() + dt * planet.get_x_vel(),
                planet.get_y_pos() + dt * planet.get_y_vel())

            # After move, we need to calculate the new distance from the sun using the distance formula.
            dist_x = self.the_sun.get_x_pos() - planet.get_x_pos()
            dist_y = self.the_sun.get_y_pos() - planet.get_y_pos()
            new_distance = math.sqrt(dist_x ** 2 + dist_y ** 2)

            # Let's calculate our new acceleration so we can set our new velocity
            acc_x = u.G * self.the_sun.get_mass() * dist_x / new_distance ** 3
            acc_y = u.G * self.the_sun.get_mass() * dist_y / new_distance ** 3

            # Now let's calculate the new x and y velocities and update them for the planet
            planet.set_x_vel(planet.get_x_vel() + dt * acc_x)
            planet.set_y_vel(planet.get_y_vel() + dt * acc_y)


    def __str__(self):
        return f'Scanners indicate that this solar system is centered around the star, {self.the_sun.name}. It includes the planets, {self.get_planets()}'


'''Mars = Planet('Mars',1,1.5,1.5,0,0)
Tester = SolarSystem()
Tester.add_sun(Sol)
Tester.add_planet(Earth)
Tester.add_planet(Mars)


print(Tester)'''


