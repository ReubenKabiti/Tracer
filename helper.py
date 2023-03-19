import time
import pygame

# todo: fix this
def debug(msg, x, y):
    msg = str(msg)
    font = pygame.font.SysFont("arial", 32)
    surface = pygame.display.get_surface()

    text = font.render("Hello world longer", (255, 255, 255), True, 32)
    print(text.get_rect().width)
    surface.blit(text, (x, 10))

def profile(func):
        def out(*args, **kwargs):
            t = time.time()
            op = func(*args, **kwargs)
            t = time.time() - t
            print(round(t, 3), "s", sep="")
            return op
        return out

