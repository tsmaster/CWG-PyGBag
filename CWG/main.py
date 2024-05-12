import pygame
import random
import modemgr
import mode
import textscreenmode
import menuscreenmode

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480



# Set up the screen and clock
#displayflags = pygame.SCALED
displayflags = 0
#displayflags = pygame.OPENGL

screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT),
                                 flags=displayflags)
pygame.display.set_caption("Cars With Guns 2024 w PyGBag")
clock = pygame.time.Clock()

# create modes
modemgr.g_modemgr.add_mode(mode.SimpleScreenMode("bdg", "bdg.png", "title"))
modemgr.g_modemgr.add_mode(mode.SimpleScreenMode("title", "cwg_screen.png", "main_menu"))

menuscreen = menuscreenmode.MenuScreenMode("main_menu", "main_menu.png")
modemgr.g_modemgr.add_mode(menuscreen)

aboutscreen = textscreenmode.TextScreenMode("about", "main_menu")
aboutscreen.drawtext(16, 16, "About")
aboutscreen.drawtext(16, 96, "Click to continue")
modemgr.g_modemgr.add_mode(aboutscreen)

creditsscreen = textscreenmode.TextScreenMode("credits", "main_menu")
creditsscreen.drawtext(16, 16, "Credits")
creditsscreen.drawtext(16, 32, "Programming: Dave LeCompte")
creditsscreen.drawtext(16, 40, "Art(?): Dave LeCompte")
creditsscreen.drawtext(16, 48, "Design: Dave LeCompte")
creditsscreen.drawtext(16, 64, "Uses PyGame, PyGBag")
creditsscreen.drawtext(16, 96, "Click to continue")
modemgr.g_modemgr.add_mode(creditsscreen)

options_screen = textscreenmode.TextScreenMode("options", "main_menu")
options_screen.drawtext(16, 16, "Options")
options_screen.drawtext(16, 96, "Click to continue")
modemgr.g_modemgr.add_mode(options_screen)

# choose starting mode
modemgr.g_modemgr.set_mode_by_name("bdg")

running = True
while running:
    screen.fill((0, 0, 0))

    mode = modemgr.g_modemgr.current_mode()
    mode.update()
    mode.draw(screen)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mode.mousedown(event)
        elif event.type == pygame.KEYDOWN:
            mode.keydown(event.key)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
