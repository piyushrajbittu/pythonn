import pygame
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pac-Man Game")

black = (0, 0, 0)
yellow = (255, 255, 0)

pacman_radius = 20
pacman_x = width // 2
pacman_y = height // 2
pacman_speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_x -= pacman_speed
    if keys[pygame.K_RIGHT]:
        pacman_x += pacman_speed
    if keys[pygame.K_UP]:
        pacman_y -= pacman_speed
    if keys[pygame.K_DOWN]:
        pacman_y += pacman_speed

    pacman_x = max(pacman_radius, min(width - pacman_radius, pacman_x))
    pacman_y = max(pacman_radius, min(height - pacman_radius, pacman_y))

    screen.fill(black)

    pygame.draw.circle(screen, yellow, (pacman_x, pacman_y), pacman_radius)

    pygame.display.flip()

pygame.quit()
