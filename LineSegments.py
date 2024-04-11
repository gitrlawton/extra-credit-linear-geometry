# PROGRAMMER: Ryan Lawton

# IMPORT STATEMENTS





class LineSegments:

# CONSTRUCTOR
    
    def __init__(self, point_list):
        if type(point_list) is not list:
            raise TypeError(
                "LineSegments.py __init__ point_list - must be a list."
            )
        for element in point_list:
            if type(element) is not tuple:
                raise TypeError(
                    "LineSegments.py __init__ point_list - all elements in point_list must be a tuple."
                )
            if len(element) is not 2:
                raise ValueError(
                    "LineSegments.py __init__ point_list - each tuple in point_list must contain two values."
                )
            if type(element[0]) is not int and type(element[0]) is not float:
                raise TypeError(
                    "LineSegments.py __init__ point_list - each tuple's X Value must be a number."
                )
            if type(element[1]) is not int and type(element[1]) is not float:
                raise TypeError(
                    "LineSegments.py __init__ point_list - each tuple's Y Value must be a number."
                )
        
        self.__point_list = point_list

# INSTANCE METHODS

    def get_point(self, index):
        return self.__point_list[index]
    
    def set_point(self, point, index):
        if type(point) is not tuple:
            raise TypeError(
                "LineSegments.py set_point point - must be a tuple."
            )
        if len(point) is not 2:
            raise ValueError(
                "LineSegments.py set_point point - must contain two values."
            )
        if type(point[0]) is not int and type(point[0]) is not float:
            raise TypeError(
                "LineSegments.py set_point point - point's X Value must be a number."
            )
        if type(point[1]) is not int and type(point[1]) is not float:
            raise TypeError(
                "LineSegments.py set_point point - point's Y Value must be a number."
            )
        
        self.__point_list[index] = point
    
    def get_all_points(self):
        return self.__point_list
    
    def endpoint_distance(self):
        pass
    
    def endpoint_midpoint(self):
        pass
    
    def segment_distance(self, first_point_index, second_point_index):
        pass
    
    def segment_midpoint(self, first_point_index, second_point_index):
        pass
    
    def total_distance_traversed(self):
        pass
    
    def traversal_time(self, speed):
        pass
    
    def traversal_speed(self, time):
        pass
    
    def traversal_efficiency_percentage(self):
        pass
    
    def export_as_comma_separated_values(self, filename):
        pass