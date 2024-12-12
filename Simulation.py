from SolarSystem import SolarSystem
from Sun import Sun
from Planet import Planet
import turtle

class Simulation:
    def __init__(self, solar_system: SolarSystem, width: int, height: int, num_periods: int):
        self.solar_system = solar_system
        self.width = width
        self.height = height
        self.num_periods = num_periods
        #turtle stuff
        self.turt = turtle.Turtle()
        self.turt.hideturtle()
        self.screen = turtle.Screen()
        self.screen.setup(self.width,self.height)

    def run(self):
        for period in range(self.num_periods):
            print(f"Period {period + 1}:")
            self.solar_system.show_planets()
            self.solar_system.move_planets()
            print("-" * 20)
        self.screen.exitonclick()

if __name__ == '__main__':
    solar_system = SolarSystem()

    the_sun = Sun("SOL", 5000, 10000000, 5800)
    solar_system.add_sun(the_sun)

    venus = Planet('Venus', 35.5, 2, 15, 3.5, 300.0, 0.0, 'orange')
    solar_system.add_planet(venus)

    earth = Planet("EARTH", 47.5, 1, 25, 5.0, 200.0, )
    solar_system.add_planet(earth)

    mars = Planet("MARS", 40.5, .1, 62, 11.0, 125.0, 0.0, 'red' )
    solar_system.add_planet(mars)

    simulation = Simulation(solar_system, 500, 500, 2000)
    simulation.run()