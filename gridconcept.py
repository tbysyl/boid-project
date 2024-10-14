
import pygame as pg
import random
import sys

pg.init()

width,height = 800,600
screen = pg.display.set_mode((width,height))
pg.display.set_caption("Boids")

def grid(square_count):
    square_width = width // square_count
    square_height = height // square_count

    for x in range(0,width,square_width):
        for y in range(0,height,square_height):
            pg.draw.line(screen,(255,255,255),(x,0),(x,height))
            pg.draw.line(screen,(255,255,255),(0,y),(width,y))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit() 
    
    screen.fill((255,255,255))

    grid(50)

    pg.display.flip()



