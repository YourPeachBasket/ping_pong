from pygame import *
from random import randint
from time import sleep, time as timer
window = display.set_mode((500, 500))
clock = time.Clock()
display.set_caption('Пин-Понг')
background = transform.scale(image.load('pablo-403.png'), (700, 500))

class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(
            image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

  # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# класс главного игрока


class Player1(GameSprite):
    def update(self):
        speed = 10
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += speed

class Player2(GameSprite):
    def update(self):
        speed = 10
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += speed

lost = 0
font.init()
font1 = font.Font(None, 26)
font2 = font.Font(None, 40)

game = True
finish = False
hero1 = Player1('rocket.png', 0, 200, 40, 100, 8)
hero2 = Player2('rocket.png', 460, 200, 40, 100, 8)
ball = GameSprite('ball.png', 200, 200, 40, 40, 5)
win = 0
num_fire = 0
rel_time = False
speed_x = 3
speed_y = 3
while game:
    if finish != True:
        window.blit(background, (0, 0))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(ball, hero1) or sprite.collide_rect(ball, hero2):
            speed_x *= -1
        if ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.y >450:
            speed_y *= -1
        if ball.rect.x > 480:
            finish = True
            lose = font2.render("player2 lost", 1, (255, 0, 0))
            window.blit(lose, (150, 200))
        if ball.rect.x<5:
            finish = True
            lose2 = font2.render("player1 lost", 1, (255, 0, 0))
            window.blit(lose2, (150, 200))
        hero1.reset()
        hero1.update()
        hero2.reset()
        hero2.update()
        ball.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(50)
    display.update()