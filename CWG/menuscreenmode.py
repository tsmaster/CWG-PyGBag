import os
import pygame
import json

import Engine.UI.button

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
        
        self.fontcharwidth = self.fontimg.get_width() // self.fontcharswide
        self.fontcharheight = self.fontimg.get_height() // self.fontcharshigh

        self.bg_img = pygame.image.load(os.path.join('Assets/Images/Screens', bg_image_name))

        self.ui = []
        self.action_queue = []
        
        self.json = json.loads(open('Assets/JSON/layoutmainmenu.json').read())

        self.layout_ui(self.json)
        

    def update(self):
        timenow = pygame.time.get_ticks()
        elapsed = (timenow - self.init_time) / 1000.0

        for w in self.ui:
            w.update(elapsed)

        while self.action_queue:
            msg = self.action_queue.pop(0)
            print("action:", msg)

            if msg.startswith("modemgr:goto:"):
                tokens = msg.split(':')
                if len(tokens) != 3:
                    print("should have 3 tokens")
                    exit(-1)
                print("going to", tokens[2])
                modemgr.g_modemgr.set_mode_by_name(tokens[2])
                return
            if msg.startswith("game:"):
                tokens = msg.split(':')
                if tokens[1] == "new-game":
                    # DO NEW GAME
                    self.newGame()
                    return
                elif tokens[1] == "load-game":
                    # DO LOAD GAME
                    self.loadGame()
                    return
                elif tokens[1] == "restart":
                    # DO RESTART
                    # do we need to do more restarting?
                    modemgr.g_modemgr.set_mode_by_index(0)
                    return
            

    def draw(self, screen):
        screen.blit(self.bg_img, (0, 0))

        for w in self.ui:
            w.draw(screen)

    def mousedown(self, mouse_event):
        timenow = pygame.time.get_ticks()
        elapsed = (timenow - self.init_time) / 1000.0

        for w in self.ui:
            bHandled, action = w.mousedown(mouse_event)
            if bHandled:
                self.action_queue.append(action)
                return
            

    def keydown(self, key):
        timenow = pygame.time.get_ticks()
        elapsed = (timenow - self.init_time) / 1000.0

            
    def drawtext(self, x, y, s):
        for i, c in enumerate(s):
            asc = ord(c)

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

    def layout_ui(self, ui_desc):
        for w_desc in ui_desc["widgets"]:
            w_type = w_desc.get("type", None)
            if w_type == "button-group":
                w = self.make_button_group(w_desc)
                #self.ui.append(w)
            elif w_type == "button":
                b = self.make_button(w_desc)
                self.ui.append(b)
            elif w_type == "background":
                self.bg_img = self.make_background(w_desc)
            else:
                print("error: unknown type:", w_type)
                exit(-1)

    def make_button_group(self, widget_desc):
        name = widget_desc.get("name", "no name")

        args = {}
        args["name"] = widget_desc.get("name", "button_group")
        args["layout"] = widget_desc.get("layout", "vertical")
        args["align"] = widget_desc.get("align", "left")
        left_pos = convertToPixels(widget_desc.get("left-pos", "0px"))
        top_pos = convertToPixels(widget_desc.get("top-pos", "0px"))
        spacing = convertToPixels(widget_desc.get("spacing", "10px"))
        child_height = convertToPixels(widget_desc.get("child-height", None))
        child_width = convertToPixels(widget_desc.get("child-width", None))

        for wi, w in enumerate(widget_desc.get("widgets", [])):
            arg_dict = {"width": child_width,
                        "height": child_height,
                        "pos": (left_pos,
                                top_pos + wi * (spacing + child_height)) #TODO make this smarter
                        }
            for k,v in w.items():
                arg_dict[k] = v
            child = self.make_widget(arg_dict)
            # TODO add child to button group object
            self.ui.append(child)

        return None
            

    def make_button(self, widget_desc):
        name = widget_desc.get("name", "no name")
        but = Engine.UI.button.Button(widget_desc)

        return but

    def make_widget(self, widget_desc):
        name = widget_desc.get("name", "no name")
        if "type" not in widget_desc:
            print("can't figure out what type of widget to make for", name)
            exit(-1)
        wt = widget_desc["type"]
        if wt == "button":
            return self.make_button(widget_desc)

        return None

def convertToPixels(spc_str):
    if spc_str.endswith("px"):
        return float(spc_str[:-2])
    else:
        print("don't understand this spacing string:", spc_str)
        exit(-1)
        
