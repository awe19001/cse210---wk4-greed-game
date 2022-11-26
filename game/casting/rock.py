import random
from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

# a child class 
class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.
    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        x = random.randint(1, 60)
        y = random.randint(1, 40)
        position = Point(x, y)
        position = position.scale(15)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
    
        self._font_size = 20
        self._color = color
        self._position = position
        
        dy = random.randint(int(VERT_SPEED / 3), VERT_SPEED)
        dx = random.randint(- HOR_SPEED, HOR_SPEED)
        self._velocity = Point(dx, dy)