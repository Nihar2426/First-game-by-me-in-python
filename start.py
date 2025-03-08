import pygame
import time
import random
pygame.font.init()
pygame.init() 
from pygame import mixer

WIDTH, HEIGHT = 760, 480
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A game by Nihar2426")

BG = pygame.transform.scale(pygame.image.load("bg1.jpg"),(WIDTH, HEIGHT))

mixer.music.load('06. Full Moon.wav')
mixer.music.play(-1)

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 35

PLAYER_VEL = 5
PLAYER_VEL2 = 8

STAR_WIDTH = 15
STAR_HEIGHT = 25
STAR_VEL = 7.5

FONT = pygame.font.SysFont("comicsans",20)

def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0,0))
    
    time_text = FONT.render(f"Time : {round(elapsed_time)}s", 1, "White")
    WIN.blit(time_text,(8,8))
    
    pygame.draw.rect(WIN, "red", player)
    
    for star in stars:
        pygame.draw.rect(WIN, "white", star)
    
    pygame.display.update()

def main() :
    run = True
    
    player = pygame.Rect(360, HEIGHT-PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    
    Clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    
    star_add_increment = 1000
    star_count = 0
    
    stars = []
    hit = False
        
    while run :
        star_count += Clock.tick(60)
        elapsed_time = time.time() - start_time
        
        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x , -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
                
            star_add_increment = max(200,star_add_increment-50)    
            star_count=0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                run = False
                break
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL +PLAYER_WIDTH <= WIDTH:
            player.x += PLAYER_VEL
        if keys[pygame.K_LEFT] and (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) and player.x - PLAYER_VEL2 >=0:
            player.x -= PLAYER_VEL2
        if keys[pygame.K_RIGHT] and (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) and player.x + PLAYER_WIDTH + PLAYER_VEL2 <= WIDTH:
            player.x += PLAYER_VEL2
            
        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit =True
                break
            
        if hit :
            mixer.music.load('Lose.wav')
            mixer.music.play()
            lost_text = FONT.render("! YOU LOST !", 1, "White")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 -lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(8500)
            break
        draw(player, elapsed_time, stars)
            
    python.quit()
    
if __name__ == "__main__":
    main()
