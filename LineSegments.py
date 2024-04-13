# PROGRAMMER: Ryan Lawton

# IMPORT STATEMENTS

import math






class LineSegments:

# CONSTRUCTOR
    
    def __init__(self, point_list):
        if type(point_list) is not list:
            raise TypeError(
                "LineSegments.py __init__ point_list - must be a list."
            )
        if len(point_list) < 2:
            raise ValueError(
                "LineSegments.py __init__ point_list - must contain at least two points in order to constitute a line."
            )
        
        unique_points = set()
        
        for element in point_list:
            if element in unique_points:
                raise ValueError(
                    "LineSegments.py __init__ point_list - cannot contain duplicate points (multiple points with the same X and Y value.)"
                )
            if type(element) is not tuple:
                raise TypeError(
                    "LineSegments.py __init__ point_list - all elements in point_list must be a tuple."
                )
            if len(element) != 2:
                raise ValueError(
                    "LineSegments.py __init__ point_list - each tuple in point_list must contain exactly two values."
                )
            if type(element[0]) is not int and type(element[0]) is not float:
                raise TypeError(
                    "LineSegments.py __init__ point_list - each tuple's X value must be a number."
                )
            if type(element[1]) is not int and type(element[1]) is not float:
                raise TypeError(
                    "LineSegments.py __init__ point_list - each tuple's Y value must be a number."
                )
            
            unique_points.add(element)
        
        self.__point_list = point_list

# INSTANCE METHODS

    def get_point(self, index):
        if type(index) is not int:
            raise TypeError(
                "LineSegments.py get_point index - must be an int."
            )
        if index < 0:
            raise ValueError(
                "LineSegments.py get_point index - cannot be less than 0."
            )
        if index >= len(self.__point_list):
            raise ValueError(
                "LineSegments.py get_point index - cannot be greater than " + str(len(self.__point_list) - 1) + "."
            )
        
        return self.__point_list[index]
    
    def set_point(self, point, index):    
        if type(index) is not int:
            raise TypeError(
                "LineSegments.py set_point index - must be an int."
            )
        if index < 0:
            raise ValueError(
                "LineSegments.py set_point index - cannot be less than 0."
            )
        if index >= len(self.__point_list):
            raise ValueError(
                "LineSegments.py set_point index - cannot be greater than " + str(len(self.__point_list) - 1) + "."
            )         
        if type(point) is not tuple:
            raise TypeError(
                "LineSegments.py set_point point - must be a tuple."
            )
        if len(point) != 2:
            raise ValueError(
                "LineSegments.py set_point point - must contain exactly two values."
            )
        if type(point[0]) is not int and type(point[0]) is not float:
            raise TypeError(
                "LineSegments.py set_point point - point's X value must be a number."
            )
        if type(point[1]) is not int and type(point[1]) is not float:
            raise TypeError(
                "LineSegments.py set_point point - point's Y value must be a number."
            )
        if point in self.__point_list and self.__point_list[index] != point:
            raise ValueError(
                "LineSegments.py set_point point - this point is already in the list of points. Cannot add duplicate points."
            )           
        
        self.__point_list[index] = point
    
    def get_all_points(self):
        return self.__point_list
    
    def endpoint_distance(self):
        point_a = self.__point_list[0]
        point_b = self.__point_list[len(self.__point_list) - 1]
        
        delta_x = point_b[0] - point_a[0]
        delta_y = point_b[1] - point_a[1]
            
        distance = math.sqrt((delta_x ** 2) + (delta_y ** 2))
        
        return distance
    
    def endpoint_midpoint(self):
        point_a = self.__point_list[0]
        point_b = self.__point_list[len(self.__point_list) - 1]
        
        midpoint_x = (point_a[0] + point_b[0]) / 2
        midpoint_y = (point_a[1] + point_b[1]) / 2
        
        return (midpoint_x, midpoint_y)
    
    def segment_distance(self, first_point_index, second_point_index):
        if type(first_point_index) is not int:
            raise TypeError(
                "LineSegments.py segment_distance first_point_index - must be an int."
            )
        if type(second_point_index) is not int:
            raise TypeError(
                "LineSegments.py segment_distance second_point_index - must be an int."
            )        
        if first_point_index < 0:
            raise ValueError(
                "LineSegments.py segment_distance first_point_index - cannot be less than 0."
            )
        if first_point_index >= len(self.__point_list):
            raise ValueError(
                "LineSegments.py segment_distance first_point_index - cannot be greater than " + str(len(self.__point_list) - 1) + "."
            )    
        if second_point_index < 0:
            raise ValueError(
                "LineSegments.py segment_distance second_point_index - cannot be less than 0."
            )
        if second_point_index >= len(self.__point_list):
            raise ValueError(
                "LineSegments.py segment_distance second_point_index - cannot be greater than " + str(len(self.__point_list) - 1) + "."
            )
        if first_point_index == second_point_index:
            raise ValueError(
                "LineSegments.py segment_distance second_point_index - cannot use the same index for both first_point_index and second_point_index."
            )
        
        point_a = self.__point_list[first_point_index]
        point_b = self.__point_list[second_point_index]
        
        delta_x = point_b[0] - point_a[0]
        delta_y = point_b[1] - point_a[1]
            
        distance = math.sqrt((delta_x ** 2) + (delta_y ** 2))
        
        return distance
    
    def segment_midpoint(self, first_point_index, second_point_index):
        if type(first_point_index) is not int:
            raise TypeError(
                "LineSegments.py segment_midpoint first_point_index - must be an int."
            )
        if type(second_point_index) is not int:
            raise TypeError(
                "LineSegments.py segment_midpoint second_point_index - must be an int."
            )        
        if first_point_index < 0:
            raise ValueError(
                "LineSegments.py segment_midpoint first_point_index - cannot be less than 0."
            )
        if first_point_index >= len(self.__point_list):
            raise ValueError(
                "LineSegments.py segment_midpoint first_point_index - cannot be greater than " + str(len(self.__point_list) - 1) + "."
            )    
        if second_point_index < 0:
            raise ValueError(
                "LineSegments.py segment_midpoint second_point_index - cannot be less than 0."
            )
        if second_point_index >= len(self.__point_list):
            raise ValueError(
                "LineSegments.py segment_midpoint second_point_index - cannot be greater than " + str(len(self.__point_list) - 1) + "."
            )   
        if first_point_index == second_point_index:
            raise ValueError(
                "LineSegments.py segment_midpoint second_point_index - cannot use the same index for both first_point_index and second_point_index."
            )        
        
        point_a = self.__point_list[first_point_index]
        point_b = self.__point_list[second_point_index]
        
        midpoint_x = (point_a[0] + point_b[0]) / 2
        midpoint_y = (point_a[1] + point_b[1]) / 2
        
        return (midpoint_x, midpoint_y)
    
    def total_distance_traversed(self):
        total_distance = 0
        
        for index in range(1, len(self.__point_list), 1):
            previous_point = self.__point_list[index - 1]
            current_point = self.__point_list[index]
        
            delta_x = current_point[0] - previous_point[0]
            delta_y = current_point[1] - previous_point[1]
            
            distance = math.sqrt((delta_x ** 2) + (delta_y ** 2))
            
            total_distance += distance
        
        return total_distance
    
    def traversal_time(self, speed):
        if type(speed) is not float:
            raise TypeError(
                "LineSegments.py traversal_time speed - must be a float."
            )
        if speed <= 0:
            raise ValueError(
                "LineSegments.py traversal_time speed - must be greater than 0."
            )        
        
        return self.total_distance_traversed() / speed
    
    def traversal_speed(self, time):
        if type(time) is not float:
            raise TypeError(
                "LineSegments.py traversal_speed time - must be a float."
            )
        if time <= 0:
            raise ValueError(
                "LineSegments.py traversal_speed time - must be greater than 0."
            )
        
        return self.total_distance_traversed() / time
    
    def traversal_efficiency_percentage(self):
        return (self.endpoint_distance() / self.total_distance_traversed()) * 100
    
    def export_as_comma_separated_values(self, filename):
        if type(filename) is not str:
            raise TypeError(
                "LineSegments.py export_as_comma_separated_values filename - must be a string."
            )
        if not filename.endswith(".csv"):
            raise ValueError(
                "LineSegments.py export_as_comma_separated_values filename - must end with .csv"
            )
        try:
            with open(filename, "w") as output_file:
                output_file.write("X,Y" + "\n")
                for point in self.__point_list:
                    output_file.write(str(point[0]) + "," + str(point[1]) + "\n")
                
        except FileNotFoundError:
            print("The specified file was not found.")
        except PermissionError:
            print("You do not have the necessary permissions required to perform this action.")
        except Exception as exception_object:
            print("An error occurred:", str(exception_object))