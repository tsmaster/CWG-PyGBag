import pygame

id_counter = 0

def generate_unique_id(prefix):
    global id_counter
    label = "{0}_{1:04}".format(prefix, id_counter)
    id_counter += 1
    return label


class Button:
    def __init__(self, param_dict):
        self.pos = param_dict.get("pos", (0, 0))
        self.width = param_dict.get("width", 100)
        self.height = param_dict.get("height", 32)
        self.bg_color = param_dict.get("bg_color", (50, 50, 50))
        self.hover_color = param_dict.get("hover_color", (200, 200, 200))
        self.label_color = param_dict.get("label_color", (255, 255, 255))
        self.action = param_dict.get("action", None)
        if "name" in param_dict:
            self.name = param_dict["name"]
        else:
            self.name = generate_unique_id("button")
        self.label = param_dict.get("label", self.name)
        self.activation = 0.0
        self.isHovered = False
        
        # TODO use pygame.font.Font.render
        temp_font = pygame.font.SysFont("helvetica", int(self.height))
        self.temp_label = temp_font.render(self.label, False, (0, 0, 0))

        print("made button {0} at pos {1}".format(self.label, self.pos))
        

    def draw(self, target_surface):
        if self.isHovered:
            bg_col = self.hover_color
        else:
            bg_col = self.bg_color
            
        pygame.draw.rect(target_surface, bg_col,
                         (self.pos[0], self.pos[1],
                          self.width, self.height))
        # TODO draw real label
        target_surface.blit(self.temp_label,
                            self.pos)

    def update(self, dt):
        mp = pygame.mouse.get_pos()
        mp_x, mp_y = mp
        isInside = self.isPointInside(mp_x, mp_y)
        self.isHovered = isInside

    def isPointInside(self, x, y):
        return (x >= self.pos[0] and x < self.pos[0] + self.width and
                y >= self.pos[1] and y < self.pos[1] + self.height)        

    def mousedown(self, mouse_event):
        if mouse_event.type != pygame.MOUSEBUTTONDOWN:
            print("wrong event", mouse_event)
            exit(-1)
        mouse_pos = mouse_event.pos
        mouse_button = mouse_event.button

        mp_x, mp_y = mouse_pos
        if not self.isPointInside(mp_x, mp_y):
            return (False, None)

        return (True, self.action)
        
        

if __name__ == "__main__":
    print("test gen id")
    print(generate_unique_id("test"))
    print(generate_unique_id("foo"))
    print(generate_unique_id("bar"))
    print(generate_unique_id("baz"))

    test_dict = {"name": "jeff"}
    print(test_dict.get("name", generate_unique_id("fallback")))

    print(generate_unique_id("after"))
