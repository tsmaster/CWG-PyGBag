import pygame
import os
import modemgr

class Mode:
    def __init__(self, name):
        self.name = name
        self.init_time = -1

    def init(self, time):
        self.init_time = time
        
    def update(self):
        pass

    def draw(self, screen):
        pass

    def mouseclick(self, x, y):
        pass

    def keydown(self, key):
        pass



class SimpleScreenMode(Mode):
    def __init__(self, name, fn, next_name):
        super().__init__(name)
        self.img = pygame.image.load(os.path.join('Assets/Images/Screens', fn))
        self.next_name = next_name
        self.min_time = 0.5 # seconds
        self.max_time = 10.0

    def update(self):
        timenow = pygame.time.get_ticks()
        elapsed = (timenow - self.init_time) / 1000.0

        if (elapsed >= self.max_time):
            self.advance()

    def draw(self, screen):
        screen.blit(self.img, (0, 0))

    def mouseclick(self, x, y):
        timenow = pygame.time.get_ticks()
        elapsed = (timenow - self.init_time) / 1000.0

        if (elapsed >= self.min_time):
            self.advance()

    def keydown(self, key):
        timenow = pygame.time.get_ticks()
        elapsed = (timenow - self.init_time) / 1000.0

        if (elapsed >= self.min_time):
            self.advance()
    def advance(self):
        modemgr.g_modemgr.set_mode_by_name(self.next_name)
        
        
