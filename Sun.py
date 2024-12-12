import turtle

class Sun:
    def __init__(self, name: str, radius: float, mass: float, temp: float, x: float=0.0, y: float=0.0, color: str='#ebb134'):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.temp = temp
        self.x = x
        self.y = y
        #turtle stuff
        self.turt = turtle.Turtle()
        self.turt.shape('circle')
        self.turt.color(color)
        #turtle positioning
        self.turt.penup()
        self.turt.goto(self.x, self.y)
        self.turt.pendown()


    def get_mass(self) -> float:
        return self.mass

    def get_x_pos(self) -> float:
        return self.x

    def get_y_pos(self) -> float:
        return self.y

    def __str__(self) -> str:
        return f"Sun(name={self.name}, radius={self.radius}, mass={self.mass}, temp={self.temp}, position=({self.x}, {self.y}))"

#Sol = Sun('Sol',10,100.0,10000,0,0)
#print(Sol)