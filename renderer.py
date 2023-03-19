import pygame
from random import randrange
import helper
from gameobjects.vector3 import Vector3
import math
from ray import Ray
from threading import Thread


class Renderer:

    def __init__(self):

        self.fov = math.pi / 2.0
        self.flen = 1 / (2 * math.tan(self.fov))
        self.camera_pos = Vector3(0, 0, self.flen)
        self.aspect = 0
        self.black = pygame.color.Color(0, 0, 0)
        self.light_dir = Vector3(1, -1, -1)

    @helper.profile
    def render(self, objects):
        size = pygame.display.get_surface().get_rect()
        size.width = size.width
        size.height = size.height
        surf = pygame.surface.Surface((size.width, size.height))

        screen_width = float(size.width)
        screen_height = size.height

        self.aspect = screen_width / screen_height

        max_threads = 40
        threads = []

        for y in range(size.height):
            for x in range(size.width):
                u = x / size.width 
                u = 2 * u - 1

                v = (size.height - y) / size.height
                v = 2 * v - 1
                self.per_pixel(surf, x, y, u, v, objects)
                   
        return surf

    def per_pixel(self, surf, x, y, u, v, objects):
        
        
        right = Vector3(1, 0, 0)
        up = Vector3(0, 1, 0)
        z = Vector3(0, 0, 1)

        pixel_coord = right * u * self.aspect + up * v - z

        ray_dir = pixel_coord - self.camera_pos
        ray = Ray(self.camera_pos, ray_dir)

        # a = dot(r.d, r.d)
        # b = 2.0 * dot(r.d, r.o)
        # c = dot(r.o, r.o) - r**2

        hit_infos = []

        for obj in objects:
            hit_infos_obj = obj.hit(ray)
            [hit_infos.append(hit_info) for hit_info in hit_infos_obj]
        
        if not hit_infos:
            return self.black

        hit_info = min(hit_infos, key=lambda x: x.t)

        sphere_color = hit_info.color
        normal = hit_info.normal

        fac = max(normal.dot(-self.light_dir.get_normalized()), 0)

        r = int(sphere_color.r * fac)
        g = int(sphere_color.g * fac)
        b = int(sphere_color.b * fac)

        color = pygame.color.Color(r, g, b)
    
        surf.set_at((x, y), color)
