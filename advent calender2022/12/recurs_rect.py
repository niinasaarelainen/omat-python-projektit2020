import pygame, time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (231, 21, 21)


def recursive_draw(x, y, width, height):
    #time.sleep(1)   ei toimi täällä !!!!
    """ Recursive rectangle function. """
    #pygame.draw.rect(screen, BLACK, [x, y, width, height], 1)
    pygame.draw.circle(screen, RED, (x, y), height//2, 1)
    # Is the rectangle wide enough to draw again?
    if(x < 750 - width):
        x += width
        y += 0
        recursive_draw(x, y, width, height)
    if (y < 500 - height):
        x -= 250
        y += height
        recursive_draw(x, y, width, height)

pygame.init()
# Set the height and width of the screen
size = [750, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # Set the screen background
    screen.fill(WHITE)
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    recursive_draw(0, 0, 150, 50)
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # Limit to 60 frames per second
    clock.tick(60)
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
pygame.quit()