import pygame
import time
import sys
import random
import pygame.freetype

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

LAVARIABLE = True
level = 1

pygame.init()

sysfont = pygame.font.get_default_font()

font1 = pygame.font.SysFont('chalkduster.ttf', 72)
img1 = font1.render("You've won", True, BLUE)
img2 = font1.render("level:", True, RED)

#pantalla
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego del Círculo y Cuadrados")

#lvl indicator
screen.blit(img2, (780, 20))
pygame.display.update()



#jugador
circle_radius = 20
circle_x, circle_y = screen_width // 2, screen_height // 2
circle_speed = 5
circle_x, circle_y = 0, 0

#circulo2
circle2_radius = 20
circle_x2, circle_y2 = 780, 580

#cuadrados
square_size = 60
squares = []
for _ in range(25):
    square_x = random.randint(0, screen_width - square_size)
    square_y = random.randint(0, screen_height - square_size)
    squares.append((square_x, square_y))

#bucle principal
while LAVARIABLE:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #movimiento jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        circle_x -= circle_speed
    if keys[pygame.K_RIGHT]:
        circle_x += circle_speed
    if keys[pygame.K_UP]:
        circle_y -= circle_speed
    if keys[pygame.K_DOWN]:
        circle_y += circle_speed

    #limitar posicionaminto del juegador a la patalla
    circle_x = max(circle_radius, min(screen_width - circle_radius, circle_x))
    circle_y = max(circle_radius, min(screen_height - circle_radius, circle_y))

    #dibuajar jugador
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 255), (circle_x, circle_y), circle_radius)

    #dibujar circulo2
    pygame.draw.circle(screen, (0, 0, 255), (780, 580), circle2_radius)

    #dibujar cuadrados
    for square_x, square_y in squares:
        pygame.draw.rect(screen, (255, 0, 0), (square_x, square_y, square_size, square_size))

    pygame.display.flip()
    for square_x, square_y in squares:
        pygame.draw.rect(screen, (255, 0, 0), (square_x, square_y, square_size, square_size))

    pygame.display.flip()

    #controlar colision
    for square_x, square_y in squares:
        if square_x < circle_x < square_x + square_size and square_y < circle_y < square_y + square_size:
            circle_x, circle_y = 0, 0

    #jugador llega a circulo2?
    if circle_x + circle_y == circle_x2 + circle_y2:
        screen.blit(img1, (20, 50))
        pygame.display.update()
        time.sleep(2)

        level = level + 1
        screen.blit(img2, (780, 20))

        circle_x = 0
        circle_y = 0

        square_size = 60
        squares = []
        for _ in range(25):
            square_x = random.randint(0, screen_width - square_size)
            square_y = random.randint(0, screen_height - square_size)
            squares.append((square_x, square_y))



    # Controlar la velocidad de actualización
    pygame.time.Clock().tick(60)
