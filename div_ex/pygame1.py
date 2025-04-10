import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
player_width = 40
speed = 300
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")

    pygame.draw.circle(screen, "white", player_pos, player_width)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if player_pos.y <= player_width:
            player_pos.y=player_pos.y
        else:
            player_pos.y -= speed * dt
    if keys[pygame.K_s]:
        if player_pos.y >= screen.get_height() - player_width:
            player_pos.y=player_pos.y
        else:
            player_pos.y += speed * dt
    if keys[pygame.K_a]:
        if player_pos.x <= player_width:
            player_pos.x=player_pos.x
        else:
            player_pos.x -= speed * dt
    if keys[pygame.K_d]:
        if player_pos.x >= screen.get_width() - player_width:
            player_pos.x=player_pos.x
        else:
            player_pos.x += speed * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()