import pygame
from random import randrange
import helper
from gameobjects.vector3 import Vector3
import math


class Renderer:

    def __init__(self):
        pass
    @helper.profile
    def render(self, objects):
        size = pygame.display.get_surface().get_rect()
        size.width = size.width / 2
        size.height = size.height / 2
        surf = pygame.surface.Surface((size.width, size.height))

        for y in range(size.height):
            for x in range(size.width):
                u = x / size.width 
                u = 2 * u - 1

                v = (size.height - y) / size.height
                v = 2 * v - 1

                color = self.per_pixel(u, v, objects)
                surf.set_at((x, y), color)
        return surf

    def per_pixel(self, u, v, objects):
        screen_width = float(pygame.display.get_surface().get_rect().width)
        screen_height = pygame.display.get_surface().get_rect().height

        aspect = screen_width / screen_height

        black = pygame.color.Color(0, 0, 0)
        sphere_color = pygame.color.Color(200, 100, 255)
        sphere_pos = Vector3(0, 0, -2)
        sphere_radius = 1

        light_dir = Vector3(1, -1, -1)

        fov = math.pi / 2.0
        flen = 1 / (2 * math.tan(fov))

        right = Vector3(1, 0, 0)
        up = Vector3(0, 1, 0)
        z = Vector3(0, 0, 1)

        camera_pos = Vector3(0, 0, flen)
        
        pixel_coord = right * u * aspect + up * v - z

        ray_dir = pixel_coord - camera_pos

        # a = dot(r.d, r.d)
        # b = 2.0 * dot(r.d, r.o)
        # c = dot(r.o, r.o) - r**2

        # r = max(0, int(ray_dir.x * 255))
        # g = max(0, int(ray_dir.y * 255))
        # b = max(0, -int(ray_dir.z * 255))

        a = ray_dir.dot(ray_dir)
        b = 2.0 * ray_dir.dot(camera_pos - sphere_pos)
        c = (camera_pos - sphere_pos).dot(camera_pos - sphere_pos) - sphere_radius ** 2

        descriminant = b ** 2 - 4 * a * c

        if descriminant < 0:
            return black

        t = (-b - math.sqrt(descriminant)) / (2 * a)
        point = camera_pos + ray_dir * t
        normal = (point - sphere_pos).get_normalized()

        fac = max(normal.dot(-light_dir.get_normalized()), 0)
        sphere_color.r = int(sphere_color.r * fac)
        sphere_color.g = int(sphere_color.g * fac)
        sphere_color.b = int(sphere_color.b * fac)
        
        return sphere_color
