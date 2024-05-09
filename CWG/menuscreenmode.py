import os
import pygame

import mode
import modemgr


class MenuScreenMode(mode.Mode):
    def __init__(self, name, bg_image_name):
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

        self.bg_img = pygame.image.load(os.path.join('Assets/Images/Screens', bg_image_name))

        button_x = 400
        button_y = 64
        button_spc = 16
        
        self.drawtext(button_x, button_y, "New Game")
        button_y += button_spc
        self.drawtext(button_x, button_y, "Load Game")
        button_y += button_spc
        self.drawtext(button_x, button_y, "Options")
        button_y += button_spc
        self.drawtext(button_x, button_y, "Credits")
        button_y += button_spc
        self.drawtext(button_x, button_y, "About")
        button_y += button_spc
        self.drawtext(button_x, button_y, "Restart")
        

    def update(self):
        timenow = pygame.time.get_ticks()
        elapsed = (timenow - self.init_time) / 1000.0

    def draw(self, screen):
        screen.blit(self.bg_img, (0, 0))

    def mouseclick(self, x, y):
        timenow = pygame.time.get_ticks()
        elapsed = (timenow - self.init_time) / 1000.0

    def keydown(self, key):
        timenow = pygame.time.get_ticks()
        elapsed = (timenow - self.init_time) / 1000.0

            
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
            
            self.bg_img.blit(self.fontimg,
                             (x + i * self.fontcharwidth, y),
                             src_rect)
