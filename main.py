import pygame,sys
from pygame.locals import *
import time
import random
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
losses = ['U got mauled by basketballs lol', 'u died', 'wow. the ball broke your ankles', 'You lost because of some basketballs']
screen = pygame.display.set_mode((800,600),pygame.RESIZABLE)
clock = pygame.time.Clock()
def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,500))
    screen.blit(floor_surface,(floor_x_pos + 650,500))
#SAVE FUNC FOR ROCKET def rotate_player(player2):
    #new_player2 = pygame.transform.rotozoom(player2,player_mov * 3,1)
    #return new_player2
def player1_animation():
    new_player = anim_frames[anim_index]
    new_player_rect = new_player.get_rect(center = (150,player1_rect.centery))
    return new_player,new_player_rect
def jump_animation():
    jump_player = jump_frames[anim_index]
    jump_player_rect = jump_player.get_rect(center = (150,player1_rect.centery))
    return jump_player,jump_player_rect
def create_ball(surface, tup):
    new_ball = surface.get_rect(midbottom = tup)
    return new_ball
def move_ball(balls, move):
    for ball in balls:
        ball.centerx -= move
    return balls
def draw_ball(balls, surface):
    for ball in balls:
        screen.blit(surface, ball)
def check_collision(balls):
    global running
    global injury
    global score
    global losses
    for ball in balls:
        if player1_rect.colliderect(ball):
            injury = True
            score -= 5
            if score <= 0:
                screen.blit(injury_screen,injury_rect)
                textsurface = myfont.render(f'{random.choice(losses)}', False, (0, 0, 0))
                screen.blit(textsurface,(0,0))
                running = False


def check_opalcollision(balls):
    global score
    global x
    for ball in balls:
        if player1_rect.colliderect(ball):
            x += 90
            score += 5
            balls.remove(ball)

 

bg_surface = pygame.image.load('bg.png').convert()
#start_background = pygame.image.load('documents/game/RUN.png').convert()
bg_surface = pygame.transform.scale(bg_surface, (800,600))
ball_surface = pygame.image.load('ball.png').convert_alpha()
ball_surface = pygame.transform.scale(ball_surface, (75,75))
opal_surface = pygame.image.load('opalball.png').convert_alpha()
opal_surface = pygame.transform.scale(opal_surface, (90,90))
ball_list = []
opal_list = []
SPAWNball = pygame.USEREVENT
SPAWNopal = pygame.USEREVENT
pygame.time.set_timer(SPAWNball, random.randint(100, 8000))
pygame.time.set_timer(SPAWNopal, random.randint(100, 8000))
floor_surface = pygame.image.load('floor.png').convert()
floor_surface = pygame.transform.scale(floor_surface, (800,200))
floor_x_pos = 0
x = 0 
isjump = False
jumpcount = 12
injury = False
anim1 = pygame.image.load('walk1.png').convert_alpha()
anim1 = pygame.transform.scale(anim1, (300,260))
anim2 = pygame.image.load('walk2.png').convert_alpha()
anim2 = pygame.transform.scale(anim2, (300,260))
anim3 = pygame.image.load('walk3.png').convert_alpha()
anim3 = pygame.transform.scale(anim3, (300,260))
anim4 = pygame.image.load('walk4.png').convert_alpha()
anim4 = pygame.transform.scale(anim4, (300,260))
anim5 = pygame.image.load('walk5.png').convert_alpha()
anim5 = pygame.transform.scale(anim5, (300,260))
anim6 = pygame.image.load('walk4.png').convert_alpha()
anim6 = pygame.transform.scale(anim6, (300,260))
anim7 = pygame.image.load('walk3.png').convert_alpha()
anim7 = pygame.transform.scale(anim7, (300,260))
anim8 = pygame.image.load('walk2.png').convert_alpha()
anim8 = pygame.transform.scale(anim8, (300,260))
anim_frames = [anim1,anim2,anim3,anim4,anim5, anim6, anim7, anim8]
anim_index = 0
score = 0
move = 80
player1 = anim_frames[anim_index]
player1_rect = player1.get_rect(center = (300,380))
injury_screen = pygame.image.load('injuryscreen.png').convert_alpha()
injury_screen = pygame.transform.scale(injury_screen,(960,540))
injury_rect = injury_screen.get_rect(center = (400,300))
ANIMRUN = pygame.USEREVENT + 1
pygame.time.set_timer(ANIMRUN,50)

jump1 = pygame.image.load('jump6.png').convert_alpha()
jump1 = pygame.transform.scale(jump1, (300,260))
jump2 = pygame.image.load('jump6.png').convert_alpha()
jump2 = pygame.transform.scale(jump2, (300,260))
jump3 = pygame.image.load('jump6.png').convert_alpha()
jump3 = pygame.transform.scale(jump3, (300,260))
jump4 = pygame.image.load('jump6.png').convert_alpha()
jump4 = pygame.transform.scale(jump4, (300,260))
jump5 = pygame.image.load('jump6.png').convert_alpha()
jump5 = pygame.transform.scale(jump5, (300,260))
jump6 = pygame.image.load('jump6.png').convert_alpha()
jump6 = pygame.transform.scale(jump6, (300,260))
jump7 = pygame.image.load('jump6.png').convert_alpha()
jump7 = pygame.transform.scale(jump7, (300,260))
jump8 = pygame.image.load('jump6.png').convert_alpha()
jump8 = pygame.transform.scale(jump8, (300,260))
jump_frames = [jump1,jump2,jump3,jump4,jump5, jump6, jump7, jump8]
anim_index = 0
jumpy = jump_frames[anim_index]
ANIMJUMP = pygame.USEREVENT + 1
pygame.time.set_timer(ANIMJUMP,50)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()         
        if event.type == ANIMRUN:
            if anim_index < 3:
                anim_index += 1
            else:
                anim_index = 0
            player1,player1_rect = player1_animation()
            
        if event.type == ANIMJUMP:
            if anim_index < 3:
                anim_index += 1
            else:
                anim_index = 0
            player_jump,player1_rect = jump_animation()
            
        if event.type == SPAWNball:
            ball_list.append(create_ball(ball_surface, tup=(900,500)))
        if event.type == SPAWNopal:
            opal_list.append(create_ball(opal_surface, tup=(900, 400)))
            
            
        if not(isjump):
            if event.type == pygame.KEYDOWN:
                move += 0.5
                if event.key == pygame.K_SPACE:
                    isjump = True
                if event.key == pygame.K_UP:
                    isjump = True
        else:
            if jumpcount >= -12:
                neg = 1
                if jumpcount < 0:
                    neg = -1
                player1_rect.centery -= (jumpcount ** 2) * 1 * neg
                jumpcount -= 2
            else:
                isjump = False
                jumpcount = 12

        
    rel_x = x % bg_surface.get_rect().width
    screen.blit(bg_surface,(rel_x - bg_surface.get_rect().width ,0))
    if rel_x <= 800:
        screen.blit(bg_surface,(rel_x,0))
    x -= random.randint(1, 30)
    floor_x_pos -= 20
    draw_floor()
    if floor_x_pos <= -100:
        floor_x_pos = 0
    ball_list = move_ball(ball_list, move)
    opal_list = move_ball(opal_list, 10)
    draw_ball(ball_list, ball_surface)
    draw_ball(opal_list, opal_surface)
    injury = check_collision(ball_list)
    check_opalcollision(opal_list)
    if isjump:
        screen.blit(player_jump, player1_rect)
    else:
        screen.blit(player1,player1_rect) 
    screen.blit(floor_surface,(floor_x_pos,500))
    textsurface = myfont.render(f'Score: {score}', False, (0, 0, 0))
    screen.blit(textsurface,(500,0))
    pygame.display.update()
    clock.tick(15)
        
    
