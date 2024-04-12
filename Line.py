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
        if len(point_a) != 2:
            raise ValueError(
                "Line.py __init__ point_a - must contain exactly two values."
            )     
        if len(point_b) != 2:
            raise ValueError(
                "Line.py __init__ point_b - must contain exactly two values."
            )          
        if type(point_a[0]) is not int and type(point_a[0]) is not float:
            raise TypeError(
                "Line.py __init__ point_a - point_a's X value must be a number."
            )
        if type(point_a[1]) is not int and type(point_a[1]) is not float:
            raise TypeError(
                "Line.py __init__ point_a - point_a's Y value must be a number."
            )
        if type(point_b[0]) is not int and type(point_b[0]) is not float:
            raise TypeError(
                "Line.py __init__ point_b - point_b's X value must be a number."
            )
        if type(point_b[1]) is not int and type(point_b[1]) is not float:
            raise TypeError(
                "Line.py __init__ point_b - point_b's Y value must be a number."
            )
        if point_a == point_b:
            raise ValueError(
                "Line.py __init__ point_b - cannot have the same X and Y value as point_a."
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
        if len(point_a) != 2:
            raise ValueError(
                "Line.py set_point_a point_a - must contain exactly two values."
            )        
        if type(point_a[0]) is not int and type(point_a[0]) is not float:
            raise TypeError(
                "Line.py set_point_a point_a - point_a's X value must be a number."
            )
        if type(point_a[1]) is not int and type(point_a[1]) is not float:
            raise TypeError(
                "Line.py set_point_a point_a - point_a's Y value must be a number."
            )
        if point_a == self.__point_b:
            raise ValueError(
                "Line.py set_point_a point_a - cannot have the same X and Y value as point_b."
            )          
        
        self.__point_a = point_a
    
    def set_point_b(self, point_b):        
        if type(point_b) is not tuple:
            raise TypeError(
                "Line.py set_point_b point_b - must be a tuple."
            )
        if len(point_b) != 2:
            raise ValueError(
                "Line.py set_point_b point_b - must contain exactly two values."
            )           
        if type(point_b[0]) is not int and type(point_b[0]) is not float:
            raise TypeError(
                "Line.py set_point_b point_b - point_b's X value must be a number."
            )
        if type(point_b[1]) is not int and type(point_b[1]) is not float:
            raise TypeError(
                "Line.py set_point_b point_b - point_b's Y value must be a number."
            )   
        if point_b == self.__point_a:
            raise ValueError(
                "Line.py set_point_b point_b - cannot have the same X and Y value as point_a."
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
        if type(speed) is not float:
            raise TypeError(
                "Line.py traversal_time speed - must be a float."
            )
        if speed <= 0:
            raise ValueError(
                "Line.py traversal_time speed - must be greater than 0."
            )
        
        return self.distance() / speed
    
    def traversal_speed(self, time):
        if type(time) is not float:
            raise TypeError(
                "Line.py traversal_speed time - must be a float."
            )
        if time <= 0:
            raise ValueError(
                "Line.py traversal_speed time - must be greater than 0."
            )
        
        return self.distance() / time
    
    def midpoint(self):
        midpoint_x = (self.__point_a[0] + self.__point_b[0]) / 2
        midpoint_y = (self.__point_a[1] + self.__point_b[1]) / 2
        
        return (midpoint_x, midpoint_y)
    
    def x_intercept(self):
        x_intercept = -1 * self.y_intercept() / self.slope()
        
        return x_intercept
    
    def y_intercept(self):
        y_intercept = self.slope() * (0 - self.__point_a[0]) + self.__point_a[1]
        
        return y_intercept
    
    def export_as_comma_separated_values(self, filename):
        if type(filename) is not str:
            raise TypeError(
                "Line.py export_as_comma_separated_values filename - must be a string."
            )
        if not filename.endswith(".csv"):
            raise ValueError(
                "Line.py export_as_comma_separated_values filename - must end with .csv"
            )
        try:
            with open(filename, "w") as output_file:
                output_file.write("X,Y" + "\n")
                output_file.write(str(self.__point_a[0]) + "," + str(self.__point_a[1]) + "\n")
                output_file.write(str(self.__point_b[0]) + "," + str(self.__point_b[1]) + "\n")
                
        except FileNotFoundError:
            print("The specified file was not found.")
        except PermissionError:
            print("You do not have the necessary permissions required to access file.")
        except Exception as exception_object:
            print("An error occurred:", str(exception_object))
            