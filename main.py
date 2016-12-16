import pygame

import drawing_module


screen = pygame.display.set_mode((1000, 1000)) #Create the screen
blob = drawing_module.UnitSprite("./Data/blob.png", (100, 100), None)

clock = pygame.time.Clock() 
i = 0
while True:
    screen.fill((0, 0, 0))
    blob.draw_idle((100, 100), screen, 1/60.)
    pygame.display.flip()
    clock.tick(60)
    i += 1
