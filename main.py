
import pygame as pg

pg.init()

width,height = 800,600
screen = pg.display.set_mode((width,height))
pg.display.set_caption("Boid Testing")

circle_x = width // 2
circle_y = height // 2
circle_radius = 25
circle_speed = 5

while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    screen.fill((0,0,0))
    pg.draw.circle(screen,(0,0,255),(250,250),75)

    keys = pg.key.get_pressed()
    
    # Move the circleangle
    if keys[pg.K_LEFT]:
        circle_x -= circle_speed
    if keys[pg.K_RIGHT]:
        circle_x += circle_speed
    if keys[pg.K_UP]:
        circle_y -= circle_speed
    if keys[pg.K_DOWN]:
        circle_y += circle_speed

    pg.display.flip()

    pg.time.Clock().tick(60)

pg.quit()
                    
