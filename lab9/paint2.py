import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    black_points = []
    modeOfShape = 1

    isrect = False

    while True:

        pressed = pygame.key.get_pressed()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():

            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_w:
                    mode = 'white'
                elif event.key == pygame.K_y:
                    mode = 'yellow'
                elif event.key == pygame.K_p:
                    mode = 'pink'
                elif event.key == pygame.K_1:
                    modeOfShape = 1
                elif event.key == pygame.K_2:
                    modeOfShape = 2
                elif event.key == pygame.K_3:
                    modeOfShape = 3
                elif event.key == pygame.K_4:
                    modeOfShape = 4
                elif event.key == pygame.K_5:
                    modeOfShape = 5
                elif event.key == pygame.K_BACKSPACE:
                    points = []


            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3:  # right click shrinks radius
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]

        screen.fill((0, 0, 0))

        # draw all points
        i = 0
        while i < len(points) - 1:
            if modeOfShape == 1:
                drawLineBetweenAsCircle(screen, i, points[i], points[i + 1], radius, mode)
            elif modeOfShape == 2:
                drawLineBetweenAsSquare(screen, i, points[i], points[i + 1], radius, mode)
            elif modeOfShape == 3:
                drawLineBetweenAsRightTriangle(screen, i, points[i], points[i + 1], radius, mode)
            elif modeOfShape == 4:
                drawLineBetweenAsEquilateralTriangle(screen, i, points[i], points[i + 1], radius, mode)
            elif modeOfShape == 5:
                drawLineBetweenAsRhombus(screen, i, points[i], points[i + 1], radius, mode)
            i += 1

        pygame.display.flip()

        clock.tick(60)


def drawLineBetweenAsCircle(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'white':
        color = (c1, c1, c1)
    elif color_mode == 'yellow':
        color = (c2, c2, c1)
    elif color_mode == 'pink':
        color = (c2, c1, c2)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)


def drawLineBetweenAsSquare(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'white':
        color = (c1, c1, c1)
    elif color_mode == 'yellow':
        color = (c2, c2, c1)
    elif color_mode == 'pink':
        color = (c2, c1, c2)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.rect(screen, color, (x - width/2, y - width/2, width * 2, width * 2))

def drawLineBetweenAsRightTriangle(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'white':
        color = (c1, c1, c1)
    elif color_mode == 'yellow':
        color = (c2, c2, c1)
    elif color_mode == 'pink':
        color = (c2, c1, c2)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.polygon(screen, color, [(x,y), (x, y+width*2), (x+width*2, y+width*2)])

def drawLineBetweenAsEquilateralTriangle(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'white':
        color = (c1, c1, c1)
    elif color_mode == 'yellow':
        color = (c2, c2, c1)
    elif color_mode == 'pink':
        color = (c2, c1, c2)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.polygon(screen, color, [(x,y), (x-width*1.5, y+width*2), (x+width*1.5, y+width*2)])

def drawLineBetweenAsRhombus(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'white':
        color = (c1, c1, c1)
    elif color_mode == 'yellow':
        color = (c2, c2, c1)
    elif color_mode == 'pink':
        color = (c2, c1, c2)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.polygon(screen, color, [(x,y), (x-width*1.5, y+width*2), (x+width*1.5, y+width*2)])
        pygame.draw.polygon(screen, color, [(x-width*1.5, y+width*2), (x+width*1.5, y+width*2), (x, y+width*4)])

main()