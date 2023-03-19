import pygame
import sys
from renderer import *
from sphere import Sphere
import helper

class Tracer:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((200, 200), pygame.RESIZABLE)
        pygame.display.set_caption("Tracer")
        self.objects = [
                Sphere(Vector3(0, 0, -1), 0.4, pygame.color.Color(255, 0, 0))
        ]

    def run(self):

        renderer = Renderer() 

        while True:

            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            image = renderer.render(self.objects)

            image_width = image.get_rect().width
            screen_width = pygame.display.get_surface().get_rect().width
            image_x = screen_width - image_width

            self.screen.blit(image, (image_x, 0))
            pygame.display.update()
if __name__ == "__main__":
    Tracer().run()

