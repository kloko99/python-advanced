"""
Read only property example
"""
class Point:
    """Klasse mit read-only property x."""
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property 
    def x(self):
        return self._X 
    

p = Point(3, 5)
p.x = 4


class User:
    """Klasse mit write only property."""
    def __init__(self, name, password):
        self.name = name 
        self.password = password
    
    @property
    def password(self):
        """Getter kann nicht gelesen werden."""
        raise AttributeError("Password ist nur schreibbar")
    
    @password.setter
    def password(self, password):
        """Password kann nur gesetzt werden."""
        self.password = hash(password)