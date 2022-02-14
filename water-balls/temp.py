for x in range(-2, 2):   # oli 12
    for y in range(1, -1, -1):  # oli 02    
        print(y)

points = [(150, 150), (200, 120), (260, 140), (210, 250)]
pygame.draw.polygon(naytto, turkoosi, points, 1)
