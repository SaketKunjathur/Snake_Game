import pygame
import random

pygame.init()

display_width = 800
display_height = 600

win = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("SNAKE GAME")

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

def snake(block_size, snakelist):
    for xy in snakelist:
        pygame.draw.rect(win, green, (xy[0], xy[1], block_size, block_size))

def message_to_screen(fnt, size, text, color, coordinates):
    font = pygame.font.SysFont(fnt, size)
    text = font.render(text, True, color)
    textRect = text.get_rect()
    textRect.center = coordinates
    win.blit(text, textRect)

def message_to_screen2(font, size, txt, color, coordinates):
    font = pygame.font.SysFont(font, size)
    text = font.render(txt, True, color)
    win.blit(text, coordinates)

def score(score_value):
    message_to_screen2("lucidaconsole", 20, "Score = "+str(score_value), white, (10, 10))

def mainloop():
                
    snake_x = display_width/2
    snake_y = display_height/2
    snake_x_change = 0
    snake_y_change = 0
    FPS = 10
    block_size = 20

    score_value = 0
   
    snakeList = []
    snakeLength = 1

    clock = pygame.time.Clock()

    food_x = round(random.randint(0, display_width - block_size) / block_size) * block_size
    food_y = round(random.randint(0, display_height - block_size) / block_size) * block_size

    run = True
    menu = True
    gameover = False
    paused = False
    rules = False

    while run:

        while menu:
            win.fill(white)
            logo = pygame.image.load("SnakeLoading.png")
            logo = pygame.transform.scale(logo, (400, 400))
            logoRect = logo.get_rect()
            logoRect.center = (display_width//2, 250)
            win.blit(logo, logoRect)
            message_to_screen("comicsansms", 25, "Press S-Start or R-Rules or Q-Quit", black, (display_width//2, 450))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    menu = False
                    rules = False
                    gameover = False
                    paused = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        rules = True
                        menu = False
                    if event.key == pygame.K_s:
                        menu = False
                        rules = False
                    if event.key == pygame.K_q:
                        run = False
                        menu = False
                        rules = False
                        gameover = False
                        paused = False
            pygame.display.update()

        while rules:
            win.fill(white)
            rulz = pygame.image.load("rulesIImg.png")
            rulz = pygame.transform.scale(rulz, (100, 100))
            rulzRect= rulz.get_rect()
            rulzRect.center = (display_width//2, 27)
            message_to_screen2("comicsansms", 25, "1)Use arrow keys to move.", black, (40, 56))
            message_to_screen2("comicsansms", 25, "2)Press Q to quit the game while playing.", black, (40, 86))
            message_to_screen2("comicsansms", 25, "3)Press P or Space to pause the game while playing.", black, (40, 116))
            message_to_screen2("comicsansms", 25, "4)If you hit the walls you are out.", black, (40, 146))
            message_to_screen2("comicsansms", 25, "5)After every time your score reaches to a number", black, (40, 176))
            message_to_screen2("comicsansms", 25, "  divisible to 5, the game speed will increase", black, (40, 206))
            message_to_screen2("comicsansms", 25, "6)The speed will increase until your score is above 20", black, (40, 236))
            message_to_screen("comicsansms", 20, "Press B - Back to Menu or Q - Quit", black, (display_width//2, 405))
            win.blit(rulz, rulzRect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    menu = False
                    rules = False
                    gameover = False
                    paused = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:
                        rules = False
                        menu = True
                    if event.key == pygame.K_q:
                        run = False
                        menu = False
                        rules = False
                        gameover = False
                        paused = False
            pygame.display.update()

        while gameover:
            win.fill(white)
            gameOver = pygame.image.load('GAMEOVER.png')
            gameOver = pygame.transform.scale(gameOver, (500, 420))
            gameOverRect = gameOver.get_rect()
            gameOverRect.center = (display_width//2, 250)
            win.blit(gameOver, gameOverRect)
            message_to_screen("comicsansms", 20, "Press Q - Quit or P - Play Again", black, (display_width//2, 550))
           
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    menu = False
                    rules = False
                    gameover = False
                    paused = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        run = False
                        menu = False
                        rules = False
                        gameover = False
                        paused = False
                    if event.key == pygame.K_p:
                        mainloop()
                   
            pygame.display.update()

        while paused:
            win.fill(white)

            gamePaused = pygame.image.load('GamePause.png')
            gamePaused = pygame.transform.scale(gamePaused, (340, 300))
            gamePausedRect = gamePaused.get_rect()
            gamePausedRect.center = (display_width//2, 150)
            win.blit(gamePaused, gamePausedRect)

            message_to_screen("comicsansms", 20, "Press R-Resume or Q-Quit or M-Menu", black, (display_width//2, 450))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    menu = False
                    rules = False
                    gameover = False
                    paused = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        paused = False
                    if event.key == pygame.K_q:
                        run = False
                        menu = False
                        rules = False
                        gameover = False
                        paused = False
                    if event.key == pygame.K_SPACE:
                        pause = False
                    if event.key == pygame.K_p:
                        pause == False
                    if event.key == pygame.K_m:
                        menu = True

            pygame.display.update()
                   
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                menu = False
                rules = False
                gameover = False
                paused = False
               
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if snake_x_change == -block_size:
                        snake_y_change = 0
                    else:
                        snake_x_change = block_size
                        snake_y_change = 0
                if event.key == pygame.K_LEFT:
                    if snake_x_change == block_size:
                        snake_y_change = 0
                    else:
                        snake_x_change = -block_size
                        snake_y_change = 0
                if event.key == pygame.K_DOWN:
                    if snake_y_change == -block_size:
                        snake_x_change = 0
                    else:
                        snake_y_change = block_size
                        snake_x_change = 0
                if event.key == pygame.K_UP:
                    if snake_y_change == block_size:
                        snake_x_change = 0
                    else:
                        snake_y_change = -block_size
                        snake_x_change = 0

                if event.key == pygame.K_p:
                    paused = True
                if event.key == pygame.K_SPACE:
                    paused = True
                if event.key == pygame.K_q:
                    run = False
                    menu = False
                    rules = False
                    gameover = False
                    paused = False
                   

        snake_x += snake_x_change
        snake_y += snake_y_change

        if snake_x < 0 or snake_x > display_width - block_size or snake_y < 0 or snake_y > display_height - block_size:
            gameover = True

        snakeHead = []
        snakeHead.append(snake_x)
        snakeHead.append(snake_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameover = True

        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randint(0, display_width - block_size) / block_size) * block_size
            food_y = round(random.randint(0, display_height - block_size) / block_size) * block_size
            snakeLength += 1
            score_value += 1
            if score_value < 5 and score_value >= 0:
                FPS = 10
            if score_value < 10 and score_value >= 5:
                FPS = 15
            if score_value < 15 and score_value >= 10:
                FPS = 20
            if score_value < 20 and score_value >= 15:
                FPS = 25

        win.fill(black)
        pygame.draw.rect(win, (red), (food_x, food_y, block_size, block_size))
        pygame.draw.rect(win, green, (snake_x, snake_y, block_size, block_size))
        snake(block_size, snakeList)

        clock.tick(FPS)

        score(score_value)
       
        pygame.display.update()

mainloop()
    
pygame.quit()
quit()
 
