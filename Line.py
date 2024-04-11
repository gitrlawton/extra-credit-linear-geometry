# PROGRAMMER: Ryan Lawton

# IMPORT STATEMENTS

import math






class Line:

# CONSTRUCTOR

    def __init__(self, point_a, point_b):
        if type(point_a) is not tuple:
            raise TypeError(
                "Line.py __init__ point_a - must be a tuple."
            )
        if type(point_b) is not tuple:
            raise TypeError(
                "Line.py __init__ point_b - must be a tuple."
            )
        if type(point_a[0]) is not int and type(point_a[0]) is not float:
            raise TypeError(
                "Line.py __init__ point_a - point_a's X Value must be a number."
            )
        if type(point_a[1]) is not int and type(point_a[1]) is not float:
            raise TypeError(
                "Line.py __init__ point_a - point_a's Y Value must be a number."
            )
        if type(point_b[0]) is not int and type(point_b[0]) is not float:
            raise TypeError(
                "Line.py __init__ point_b - point_b's X Value must be a number."
            )
        if type(point_b[1]) is not int and type(point_b[1]) is not float:
            raise TypeError(
                "Line.py __init__ point_b - point_b's Y Value must be a number."
            )
        self.__point_a = point_a
        self.__point_b = point_b

# INSTANCE METHODS

    def get_point_a(self):
        return self.__point_a
    
    def get_point_b(self):
        return self.__point_b
    
    def set_point_a(self, point_a):
        if type(point_a) is not tuple:
            raise TypeError(
                "Line.py set_point_a point_a - must be a tuple."
            )
        if type(point_a[0]) is not int and type(point_a[0]) is not float:
            raise TypeError(
                "Line.py set_point_a point_a - point_a's X Value must be a number."
            )
        if type(point_a[1]) is not int and type(point_a[1]) is not float:
            raise TypeError(
                "Line.py set_point_a point_a - point_a's Y Value must be a number."
            )  
        self.__point_a = point_a
    
    def set_point_b(self, point_b):
        if type(point_b) is not tuple:
            raise TypeError(
                "Line.py set_point_b point_b - must be a tuple."
            )
        if type(point_b[0]) is not int and type(point_b[0]) is not float:
            raise TypeError(
                "Line.py set_point_b point_b - point_b's X Value must be a number."
            )
        if type(point_b[1]) is not int and type(point_b[1]) is not float:
            raise TypeError(
                "Line.py set_point_b point_b - point_b's Y Value must be a number."
            )   
        self.__point_b = point_b
    
    def delta_x(self):
        return float(self.__point_b[0] - self.__point_a[0])
    
    def delta_y(self):
        return float(self.__point_b[1] - self.__point_a[1])
    
    def slope(self):
        return self.delta_x() / self.delta_y()
    
    def distance(self):
        distance = math.sqrt((self.delta_x() ** 2) + (self.delta_y() ** 2))
        return distance
    
    def traversal_time(self, speed):
        if type(speed) is not int and type(speed) is not float:
            raise TypeError(
                "Line.py traversal_time speed - must be a number."
            )
        if speed <= 0:
            raise ValueError(
                "Line.py traversal_time speed - must be greater than 0."
            )
        
        return self.distance() / speed
    
    def traversal_speed(self, time):
        pass
    
    def midpoint(self):
        pass
    
    def x_intercept(self):
        pass
    
    def y_intercept(self):
        pass
    
    def export_as_comma_separated_values(self, filename):
        pass
    