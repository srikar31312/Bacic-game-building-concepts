import pygame

def main():
    pygame.init()
    screen_width, screen_height = 500, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Color Changing Sprite')

    # Define colors
    colors = {
        'red': pygame.Color('red'),
        'green': pygame.Color('green'),
        'blue': pygame.Color('blue'),
        'yellow': pygame.Color('yellow'),
        'white': pygame.Color('white')
    }
    current_color = colors['white']

    # Sprite properties
    x, y = 30, 30
    sprite_width, sprite_height = 60, 60
    speed = 3  # Movement speed

    clock = pygame.time.Clock()
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Get keys pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: 
            x -= speed
        if keys[pygame.K_RIGHT]: 
            x += speed
        if keys[pygame.K_UP]: 
            y -= speed
        if keys[pygame.K_DOWN]: 
            y += speed

        # Ensure sprite stays within screen boundaries
        x = max(0, min(x, screen_width - sprite_width))
        y = max(0, min(y, screen_height - sprite_height))

        # Change color based on boundary contact
        if x == 0:
            current_color = colors['red']
        elif x == screen_width - sprite_width:
            current_color = colors['blue']
        elif y == 0:
            current_color = colors['yellow']
        elif y == screen_height - sprite_height:
            current_color = colors['green']
        else:
            current_color = colors['white']

        # Render everything
        screen.fill((0, 0, 0))  # Clear screen
        pygame.draw.rect(screen, current_color, (x, y, sprite_width, sprite_height))
        pygame.display.flip()
        clock.tick(60)  # Limit FPS

    pygame.quit()

if __name__ == "__main__":
    main()