# Class definition for a Rectangle
class Rectangle:
    # Initializer for the Rectangle class
    def __init__(self, x, y, side1, side2):
        self.x = x  # x-coordinate of the rectangle's center
        self.y = y  # y-coordinate of the rectangle's center
        self.side1 = side1  # Length of the first side
        self.side2 = side2  # Length of the second side
        # Precompute area and circumference for efficiency
        self._area = side1 * side2  # Area of the rectangle
        self._omkrets = 2 * (side1 + side2)  # Circumference of the rectangle

    # Property to get the area of the rectangle
    @property
    def area(self):
        return self._area

    # Property to get the circumference of the rectangle
    @property
    def omkrets(self):
        return self._omkrets

    # Check if a point (point_x, point_y) is inside the rectangle
    def is_point_inside(self, point_x, point_y):
        half_side1 = self.side1 / 2
        half_side2 = self.side2 / 2
        return (
            self.x - half_side1 <= point_x <= self.x + half_side1 and
            self.y - half_side2 <= point_y <= self.y + half_side2
        )

    # Method to update the position of the rectangle's center
    def translate(self, new_x, new_y):
        # Check for valid numeric input for coordinates
        if isinstance(new_x, (int, float)) and isinstance(new_y, (int, float)):
            self.x = new_x
            self.y = new_y
        else:
            print("Invalid coordinates. Please provide numeric values.")

    # Check if the rectangle is a square (both sides are equal)
    def is_square(self):
        return self.side1 == self.side2

    # Equality check based on area
    def __eq__(self, other):
        return self.area == other.area

    # Overloading comparison operators based on area
    def __lt__(self, other):
        return self.area < other.area

    def __gt__(self, other):
        return self.area > other.area

    def __le__(self, other):
        return self.area <= other.area

    def __ge__(self, other):
        return self.area >= other.area

    # Representation of the rectangle object for developers
    def __repr__(self):
        return f'Rectangle class({self.side1}, {self.side2})'

    # String representation of the rectangle object
    def __str__(self):
        return f'Rectangle class with sides: {self.side1} and {self.side2}'


# Class definition for a Circle
class Circle:
    # Initializer for the Circle class
    def __init__(self, x, y, radius):
        self.x = x  # x-coordinate of the circle's center
        self.y = y  # y-coordinate of the circle's center
        self.radius = radius  # Radius of the circle
        # Precompute area and circumference for efficiency
        self._area = 3.14159265359 * radius ** 2  # Area of the circle
        self._omkrets = 2 * 3.14159265359 * radius  # Circumference of the circle

    # Property to get the area of the circle
    @property
    def area(self):
        return self._area

    # Property to get the circumference of the circle
    @property
    def omkrets(self):
        return self._omkrets

    # Property to get the radius of the circle
    @property
    def radius(self):
        return self._radius

    # Setter to update the radius value (ensuring non-negative)
    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            print("Radius must be a non-negative value.")

    # Method to update the position of the circle's center
    def translate(self, new_x, new_y):
        # Check for valid numeric input for coordinates
        if isinstance(new_x, (int, float)) and isinstance(new_y, (int, float)):
            self.x = new_x
            self.y = new_y
        else:
            print("Invalid coordinates. Please provide numeric values.")

    # Check if a point (point_x, point_y) is inside the circle
    def is_point_inside(self, point_x, point_y):
        distance = ((point_x - self.x) ** 2 + (point_y - self.y) ** 2) ** 0.5
        return distance <= self.radius

    # Check if the circle is a unit circle (radius = 1)
    def is_unit_circle(self):
        return self.radius == 1

    # Equality check based on area
    def __eq__(self, other):
        return self.area == other.area

    # Overloading comparison operators based on area
    def __lt__(self, other):
        return self.area < other.area

    def __gt__(self, other):
        return self.area > other.area

    def __le__(self, other):
        return self.area <= other.area

    def __ge__(self, other):
        return self.area >= other.area

    # Representation of the circle object for developers
    def __repr__(self):
        return f'Circle class({self.radius})'

    # String representation of the circle object
    def __str__(self):
        return f'Circle class with radius: {self.radius}'
