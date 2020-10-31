import pygame
import numpy as np


pygame.init()
with open("record.txt", "r") as f:
    record = f.read()
    print("record : ",record)
    f.close
passif_case= pygame.image.load("img\BLK_SQR.png")
actif_case= pygame.image.load("img\RED_SQR.png")
APPLE =pygame.image.load("img\APPLE.png")
LETTER_FONT = pygame.font.SysFont('comicsan',40)
WITH = (255,255,255)
FPS = 5

rdm = (np.random.random_integers(13) * 50,np.random.random_integers(13) * 50)
actif_x = 0
actif_y = 0
actif_coor = []
pos_dir = {
    1 : True
}
size_snake = 1
lateral_direction = True
WIDTH, HEIGHT = 700, 750
win =pygame.display.set_mode((WIDTH,HEIGHT))
run = True
r = 0
clock = pygame.time.Clock()
while run: 
    r += 1
    time = round(r / FPS)
    if time > 120:
        run =False
    LETTER = LETTER_FONT.render("Size : " + str(size_snake),1,WITH)
    LETTER2 = LETTER_FONT.render("Time : " + str(time),1,WITH)
    LETTER3 = LETTER_FONT.render("Record : " + record,1,WITH)
    win.blit(LETTER, (40,40))
    win.blit(LETTER2, (40,90))
    win.blit(LETTER3, (40,140))
    if lateral_direction:
        actif_x += 50
    else:
        actif_y += 50
    actif_coor = []
    pygame.display.update()
    clock.tick(FPS)
    keys = pygame.key.get_pressed()
    win.fill((0,0,0))
    """
    y = 0  
    x = 0
    for n in range(14):
        y= 0
        for i in range(15):

            win.blit(passif_case,(x,y))
            y+= 50
        x += 50
    """
    win.blit(APPLE , rdm)
    x_actu = actif_x
    y_actu = actif_y
    if actif_x > WIDTH - 50:
        actif_x = 0
    if actif_y > HEIGHT- 50:
        actif_y = 0
    if lateral_direction:
        for _ in range(size_snake):
            if x_actu > WIDTH - 50:
                x_actu = 0

            if x_actu < 0:
                x_actu = WIDTH -50

            if y_actu > HEIGHT - 50:
                y_actu = 0

            if y_actu < 0:
                y_actu = HEIGHT-50

            coor = [x_actu,y_actu]
            actif_coor.append(coor)
            win.blit(actif_case,(x_actu,y_actu))
            x_actu -= 50
    else:
        for i in range(size_snake):
            if x_actu > WIDTH - 50:
                x_actu = 0

            if x_actu < 0:
                x_actu = WIDTH - 50

            if y_actu > HEIGHT - 50:
                y_actu = 0

            if y_actu < 0:
                y_actu = HEIGHT - 50
            coor = [x_actu,y_actu]
            actif_coor.append(coor)
            win.blit(actif_case,(x_actu,y_actu))
            y_actu -= 50
            if (actif_x, actif_y) == rdm:
                rdm = (np.random.random_integers(13) * 50,np.random.random_integers(13) * 50)
                actif_y += 50
                size_snake += 1
                win.blit(APPLE , rdm)

    if (actif_x, actif_y) == rdm:
        rdm = (np.random.random_integers(13) * 50,np.random.random_integers(13) * 50)
        actif_x += 50
        size_snake += 1
        win.blit(APPLE , rdm)
    print(rdm)

    

    if keys[pygame.K_SPACE]:
        if lateral_direction:
            lateral_direction = False
        else:
            lateral_direction = True 
        print("direction changed :")
             

    
    if keys[pygame.K_a]:
        actif_x -= 50
        size_snake += 1


    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

if size_snake > int(record):
    with open("record.txt", "w") as f:
        f.write(str(size_snake))