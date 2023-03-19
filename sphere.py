import math
from gameobjects.vector2 import Vector2
from pygame.color import Color
from ray import Ray
from hitinfo import HitInfo
from typing import *

class Sphere:

    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color = color

    def hit(self, ray) -> List:

        oc = ray.origin - self.center
        a = ray.direction.dot(ray.direction)
        b = 2.0 * ray.direction.dot(oc)
        c = oc.dot(oc) - self.radius ** 2

        descriminant = b ** 2 - 4 * a * c
        if descriminant < 0:
            return []

        t0 = (-b - math.sqrt(descriminant)) / (2 * a)
        t1 = (-b + math.sqrt(descriminant)) / (2 * a)

        n0 = (ray.get_point_at(t0) - self.center).get_normalized()
        n1 = (ray.get_point_at(t1) - self.center).get_normalized()

        h1 = HitInfo(t0, self.color, n0)
        h2 = HitInfo(t1, self.color, n1)

        return [h1, h2]

