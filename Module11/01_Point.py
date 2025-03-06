import math

class Point:
    def __init__(self, x, y, z):  # Constructor to initialize point
        self.x = x
        self.y = y
        self.z = z

    def increment(self, dx, dy, dz):  
        """Increment point coordinates"""
        self.x += dx
        self.y += dy
        self.z += dz

    def decrement(self, dx, dy, dz):
        """Decrement point coordinates"""
        self.x -= dx
        self.y -= dy
        self.z -= dz

    def add(self, other):
        """Add two points"""
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __lt__(self, other):
        """Less than comparison based on distance from origin"""
        return self.distance() < other.distance()

    def __gt__(self, other):
        """Greater than comparison"""
        return self.distance() > other.distance()

    def __eq__(self, other):
        """Check if two points are equal"""
        return self.x == other.x and self.y == other.y and self.z == other.z

    def distance(self):
        """Calculate distance from origin"""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def quadrant(self):
        """Determine which quadrant the point is in (for 2D analysis)"""
        if self.x > 0 and self.y > 0:
            return "First Quadrant"
        elif self.x < 0 and self.y > 0:
            return "Second Quadrant"
        elif self.x < 0 and self.y < 0:
            return "Third Quadrant"
        elif self.x > 0 and self.y < 0:
            return "Fourth Quadrant"
        else:
            return "On an axis or at origin"

    def is_collinear(self, p1, p2):
        """Check if three points are collinear"""
        return (self.x * (p1.y - p2.y) + p1.x * (p2.y - self.y) + p2.x * (self.y - p1.y)) == 0

    def __str__(self):
        """Return string representation of point"""
        return f"Point({self.x}, {self.y}, {self.z})"

# Example usage
p1 = Point(1, 2, 3)
p2 = Point(2, 3, 4)
print(p1 < p2)
print(p1.quadrant())
print(p1.is_collinear(Point(2, 4, 6), Point(3, 6, 9)))  # Should return True
