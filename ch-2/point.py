import math


class Point:
    'Represents a position of a point in a two-dimensional geometric coordinates.'

    def __init__(self, x=0, y=0):
        """
        Initialize position of a new point with specified x and y 
        coordinates which default to 0 if not specified.
        """
        self.move(x, y)

    def move(self, x, y):
        "Move Location to a new location in 2D space."
        self.x = x
        self.y = y

    def reset(self):
        'Reset the point back to geometric origin (0,0).'
        self.move(0, 0)

    def calculate_distance(self, other_point):
        """
        Calculates the distance from this point to a second point that is received as a parameter.

        This function uses the pythagorean Theorem to calculate the distance between the two points.

        @param Point other_point

        @return the results as a float
        """

        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


def main():
    pass


if __name__ == "__main__":
    main()
