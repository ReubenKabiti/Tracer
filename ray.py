class Ray:

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def get_point_at(self, t):
        return self.origin + self.direction * t
