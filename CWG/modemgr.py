import pygame

class ModeManager:
    def __init__(self):
        self.modes = []
        self.mode_index = -1

    def current_mode(self):
        return self.modes[self.mode_index]

    def set_mode_by_name(self, name):
        for i, mode_i in enumerate(self.modes):
            if mode_i.name == name:
                self.mode_index = i
                self.modes[i].init(pygame.time.get_ticks())
                return
        print("no mode named", name)
        self.mode_index = -1

    def set_mode_by_index(self, index):
        if ((index >= 0) and
            (index < len(self.modes))):
            self.mode_index = index
            self.modes[index].init(pygame.time.get_ticks())
        else:
            print("invalid index:", index)
            self.mode_index = -1

    def add_mode(self, mode):
        self.modes.append(mode)
            


g_modemgr = ModeManager()
