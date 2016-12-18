import pygame

import sprite_module 
import unit_module


unit_types = unit_module.read_units_xml("Data/units.xml")
blobby_type = unit_types[0]
blobby = unit_module.UnitInstance(blobby_type, (500,500))
screen = pygame.display.set_mode((1000, 1000)) #Create the screen

clock = pygame.time.Clock() 
while True:
    screen.fill((0, 0, 0))
    blobby.animate(screen, 1/60.)
    pygame.display.flip()
    clock.tick(60)
