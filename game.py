from operator import and_
from re import I
from turtle import width
import pygame as pg
import math
import random

import sys 

from sys import exit

# initialise pygame
pg.init()

# screen set

timer = pg.time.Clock()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("new game")

background = pg.image.load("space2.jpg")

bg = pg.transform.scale(background, (800,600))
h = 600
i = 0

icon = pg.image.load("gamepad.png")

pg.display.set_icon(icon)

# player class for generating player


class player(pg.sprite.Sprite):
    player_image = pg.image.load("spaceship1.png")
    rect = player_image.get_rect()
    player_x = 350
    player_y = 480

    def player_display(self, x, y):
        screen.blit(player.player_image , (x, y))

# enemy class to generate variable enemies


class enemy(pg.sprite.Sprite):
    enemy1_icon = pg.image.load("alien1.png")
    e_pos_x = random.randint(0, 745)
    enemy1_x = e_pos_x
    enemy1_y = 20

    def enemy_display(x, y):
        screen.blit(enemy.enemy1_icon, (x, y))

class bullet(pg.sprite.Sprite):
    bullet_icon = pg.image.load("5403059(1).png")
    bullet_x = player.player_x
    bullet_y = player.player_y
    bullet_x_change = 0
    bullet_y_change = 1
    bullet_state = "ready"

    def fire_bullet(x, y):
        global bullet_state
        bullet_state = "fire"
        screen.blit(bullet.bullet_icon, (x + 16,y + 10))

# Game over


game_over_image = pg.image.load("game-over.png")

def game_over_display():
    screen.blit(game_over_image, (150, 75))

game_over = False

player = player()
# Game loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((0, 0, 0))

    #background image loop

    screen.blit(bg,(0,i))
    screen.blit(bg,(0, h + i))
    
    if math.ceil(i) == -h:
        screen.blit(bg,(0, h+i))
        i = 0
    
    i -= 0.2
    
    if event.type == pg.MOUSEBUTTONDOWN:
        mouse_presses = pg.mouse.get_pressed()
        if mouse_presses[0]:
            bullet.fire_bullet(bullet.bullet_x,bullet.bullet_y)

    if event.type == pg.KEYDOWN:
        if event.key == pg.K_RIGHT:
            if player.player_x < 735:
                player.player_x += 1
            else:
                player.player_x = 1

    if event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT:
            if player.player_x > 0:
                player.player_x -= 1
            else:
                player.player_x = 735

    if event.type == pg.KEYDOWN:
        if event.key == pg.K_UP:
            if player.player_y > 25:
                player.player_y -= 1

    if event.type == pg.KEYDOWN:
        if event.key == pg.K_DOWN:
            if player.player_y < 520:
                player.player_y += 1

    if bullet.bullet_state is "fire":
        bullet.fire_bullet(player.player_x,bullet.bullet_y)
        bullet.bullet_y -= 1
    
    if running:
        enemy.enemy1_y += 1

    if (game_over):
      game_over_display()

    player.player_display(player.player_x , player.player_y)
    enemy.enemy_display(enemy.enemy1_x, enemy.enemy1_y)

    pg.display.update()
