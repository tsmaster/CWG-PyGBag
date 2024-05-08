import os
import pygame

import mode
import modemgr


class TextScreenMode(mode.Mode):
    def __init__(self, name, next_name):
        super().__init__(name)
        fontname = "40col.png"
        self.buff = pygame.Surface((640, 480))
        self.fontimg = pygame.image.load(os.path.join('Assets/Images/Fonts', fontname))
        self.fontfirstchar = 32
        self.fontcharswide = 16
        self.fontcharshigh = 6
        
        #print("Font size:", self.fontimg.get_size())
        self.fontcharwidth = self.fontimg.get_width() // self.fontcharswide
        self.fontcharheight = self.fontimg.get_height() // self.fontcharshigh
        #print("char width:", self.fontcharwidth)
        #print("char height:", self.fontcharheight)
        self.next_name = next_name
        self.min_time = 0.5 # seconds
        self.max_time = 10.0

    def update(self):
        timenow = pygame.time.get_ticks()
        elapsed = (timenow - self.init_time) / 1000.0

        if (elapsed >= self.max_time):
            self.advance()

    def draw(self, screen):
        screen.blit(self.buff, (0, 0))

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
        
    def drawtext(self, x, y, s):
        for i, c in enumerate(s):
            asc = ord(c)
            #print("drawing char", c, asc)

            char_off = asc - self.fontfirstchar
            
            font_col = char_off % self.fontcharswide
            font_row = (char_off - font_col) // self.fontcharswide
            
            src_rect = (font_col * self.fontcharwidth,
                        font_row * self.fontcharheight,
                        self.fontcharwidth,
                        self.fontcharheight)
            
            self.buff.blit(self.fontimg,
                           (x + i * self.fontcharwidth, y),
                           src_rect)
