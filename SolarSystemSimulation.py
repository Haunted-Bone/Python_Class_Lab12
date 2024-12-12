import math







class Planet:

    def __init__(self,name,mass,distance,destination,destinationX,destinationY,positionX,positionY,velocity):
        self.name = name
        self.mass = mass
        self.distance_from_sun = distance
        self.position = positionX,positionY
        self.positionX = positionX
        self.positionY = positionY
        self.velocity = velocity
        self.destination = destination
        self.destinationX = destinationX
        self.destinationY =destinationY

    def __str__(self):

        return f'This is the planet {self.name}. Scanners indicate it has a mass of {self.mass} units, it is {self.distance_from_sun} astronomical-units away from the sun, currently has a position of {self.position}, and is moving at a velocity of {self.velocity}.'

    def get_position(self):
        return f'The current position of the planet is {self.position}'

    def set_positionX(self,new_positionX):
        self.positionX = new_positionX

    def set_positionY(self,new_positionY):
        self.positionY = new_positionY

    def get_velocity(self):

        return f'The planet is currently moving at velocity of {self.velocity} units per hour.'

    def set_velocity(self,new_velocity):

        self.velocity = new_velocity

    def set_destination(self,destX,destY):
        #sets the X and Y coordinates for the destination
        self.set_positionX(destX)
        self.set_positionY(destY)
        self.destination = (self.destinationX,self.destinationY)



    def move_to(self,new_destinationX,new_destinationY,new_velocity,time):

        self.set_velocity(new_velocity)
        self.set_destination(new_destinationX,new_destinationY)


        # Calculate the direction from the current position to the destination
        directionX = self.destinationX - self.positionX
        directionY = self.destinationY - self.positionY

        # calculate the distance to the destination

        distance = math.sqrt(directionX**2 + directionY**2)


        # normalize the direction
        if distance != 0:
            correctionX = directionX / distance
            correctionY = directionY / distance
        else:
            correctionX = 0
            correctionY = 0

        #calculate the change in position base on velocity
        distance_travelled = self.velocity * time
        if distance_travelled >= distance:
            self.positionX = self.destinationX
            self.positionY = self.destinationY

        else:
            self.positionX += correctionX * distance_travelled
            self.positionY += correctionY * distance_travelled


        #update the position
        self.position = (self.positionX, self.positionY)
        return f'Planet {self.name} has moved to {self.position}.'









class Sun:

    def __init__(self,name,mass,position):
        self.name = name
        self.mass = mass
        self.position = position

    def __str__(self):

        return f'This is the star {self.name}, it has a mass of {self.mass} units and is at position {self.position}.'



class Solar_System:

    def __init__(self,sun,planets,name):
        self.sun = sun
        self.planets = planets
        self.name = name

    def __str__(self):

        return f'This is the {self.name} solar system, it is centered around the sun {self.sun}, and includes the following planets, {self.planets}.'


class simulation:

    def __init__(self,solarsystem,sun,planets):

        self.solarsystem = solarsystem
        self.sun = sun
        self.planets =planets

    def __str__(self):

        return f'Our simulation is currently using the {self.solarsystem} solar system, with {self.sun} at the center, and {self.planets} as planets.'


    #Sol = Sun('Sol',100000,(0,0))

    #Mercury = Planet('Mercury',1000,0.25,0,0,0,0.25,0,0)
    #Venus = Planet('Venus',15000,0.5,0,0,0,0.5,0, 0)
    #Earth = Planet('Earth',25000,1,0,5,4,1,0,0)

    #print(Sol)
    #print(Earth)

    #Earth.set_velocity(1)
    #print(Earth.move_to(5,6,1,6))
