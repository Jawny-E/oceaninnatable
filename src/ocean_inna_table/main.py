import pygame as pg
from ocean_inna_table.creature import Creature

def main():
    pg.init()
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("Test Window")
    running = True
    myCreature = Creature(screen)
    
    while running:
        for event in pg.event.get():
            myCreature.drawCreature()
            if event.type == pg.QUIT:
                running = False

    pg.quit()
