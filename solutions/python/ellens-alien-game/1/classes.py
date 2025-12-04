"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    total_aliens_created = 0
    def __init__(self, x_coordinate, y_coordinate, health=3):
        '''Alien initialization function.'''
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = health
        Alien.total_aliens_created += 1


    def hit(self):
        '''Method to decrement the healthpoint attribute.'''
        if self.health > 0: self.health -= 1


    def is_alive(self):
        '''Method to check if the alien is alive.'''
        if self.health > 0: return True
        return False


    def teleport(self, new_x_coordinate, new_y_coordinate):
        '''Method to change x and y coordinates of the alien.'''
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate


    def collision_detection(*other):
        '''Method for collision detection.'''
        pass

        
#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
def new_aliens_collection(positions_list):
    '''Function to create a list of Alien() objects, given a list of positions as tuples.'''
    result = []
    for position in positions_list:
        position_x, position_y = position
        result.append(Alien(position_x, position_y))
    return result