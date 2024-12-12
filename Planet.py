import math
import turtle

class Planet:
    def __init__(self, name: str,  mass: float, distance: float, x: float, vel_x: float, vel_y: float, y: float=0.0, color: str='#34ebba'):
        self.name = name
        self.mass = mass
        self.distance = x
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        #Turtle Graphics Stuff
        self.turt = turtle.Turtle()
        self.turt.shape('circle')
        self.turt.color(color)
        #positioning for turtle
        self.turt.penup()
        self.turt.goto(self.x,self.y)
        self.turt.pendown()


    def get_mass(self) -> float:
        return self.mass

    def get_distance(self) -> float:
        return self.distance

    def get_x_pos(self) -> float:
        return self.x

    def get_x_vel(self) -> float:
        return self.vel_x

    def get_y_pos(self) -> float:
        return self.y

    def get_y_vel(self) -> float:
        return self.vel_y

    def set_x_vel(self, new_x_vel: float):
        self.vel_x = new_x_vel

    def set_y_vel(self, new_y_vel: float):
        self.vel_y = new_y_vel

    def move_to(self, new_x: float, new_y: float):
        self.x = new_x
        self.y = new_y
        self.turt.goto(new_x,new_y)


    def set_distance(self,distance):
        self.distance = distance


    def __str__(self) -> str:
        return f"Planet(name={self.name}, mass={self.mass}, position=({self.x}, {self.y}), velocity=({self.vel_x}, {self.vel_y}))"


#Earth = Planet('Earth',1.0,5,5,0,0)
#print(Earth)