# coding=utf-8

import pygame,sys
from random import *

def main():
    """飞机大战游戏窗口设置"""
    pygame.init()
    #初始化参数
    size = width,height = 480,780
    color = 255,255,255
    fsp = 60
    #导入图片
    program_icon = pygame.image.load("Sprites/hero/fly/hero1.png")
    background = pygame.image.load("images/background.png")
    #设置窗口
    screen = pygame.display.set_mode(size)
    pygame.display.set_icon(program_icon)
    pygame.display.set_caption("飞机大战")

    # 设置刷新时间函数
    fclock = pygame.time.Clock()

    #延迟哨兵
    delay = 100

    #分数统计
    score = 0
    score_font = pygame.font.Font("C://Windows//Fonts//msyh.ttc",24)

    #生成我方飞机
    hero = Hero(size)

    #生成英雄子弹
    hero_bullet = []
    hero_bullet_index = 0
    BULLET_NUM = 8
    for i in range(BULLET_NUM):
        hero_bullet.append(Hero_bullet(hero.rect.midtop))


    #生成敌方飞机
    def add_enemies(group1,num):
        for i in range(num):
            e1 = Enemy(size)
            group1.add(e1)

    enemies = pygame.sprite.Group()
    add_enemies(enemies, 20)

    #生成敌方子弹
    enemy_bullets = []
    #enemy_bullet_index = 0
    BULLET_NUM1 = 1
    for i in range(BULLET_NUM1):
        for b in enemies:
            enemy_bullets.append(Enemy_bullte(b.rect.midtop))


    #其他显示

    win = Window(size)

    stop_key = True

    #设置循环
    while True:
        #事件监听
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                sys.exit()

        screen.fill(color)
        screen.blit(background,(0,0))

        if hero.active:
            #绘制敌机子弹
            for y in enemy_bullets:
                for each in enemies:
                    if each.rect.top > 0:
                        if y.rect.top > 800 or y.rect.top < 0:
                            y.reset(each.rect.midtop)
                        else:
                            y.move()
                    #else:
                        #y.reset(each.rect.midtop)

                screen.blit(y.enemy_bullet, y.rect)

            #绘制敌机
            for each in enemies:
                enemy_hit = pygame.sprite.spritecollide(each,hero_bullet,False,pygame.sprite.collide_mask)
                if enemy_hit:
                    each.active = False
                if each.active:
                    each.move()
                    screen.blit(each.enemy,each.rect)
                else:
                    each.enemy_blast(screen)
                    score += 1




            #碰撞测试
            hero_hit = pygame.sprite.spritecollide(hero,enemy_bullets,False,pygame.sprite.collide_mask)
            hero_hit1 = pygame.sprite.spritecollide(hero,enemies,False,pygame.sprite.collide_mask)

            if hero_hit or hero_hit1:
                hero.active = False


            # hero飞机绘制和控制
            hero.hero_show(screen)
            hero.hero_move()

            # hero子弹发射和绘制
            if not (delay % 10):
                hero_bullets = hero_bullet
                hero_bullets[hero_bullet_index].reset(hero.rect.midtop)
                hero_bullet_index = (hero_bullet_index + 1) % BULLET_NUM

            for i in hero_bullets:
                i.move()
                screen.blit(i.hero_bullet, i.rect)


            delay -= 1
            if not (delay):
                delay = 100

            score_text = score_font.render("分数：%s" % str(score), True, (255, 255, 255))
            screen.blit(score_text, (5, 5))
        else:
            if stop_key:
                hero.hero_blast(screen)
                if delay % 80 == 1:
                    stop_key = False
                delay -= 1


            else:
                screen.blit(win.logo,win.logo_rect)
                screen.blit(win.over,win.over_rect)
                screen.blit(win.again,win.again_rect)
                score_font = pygame.font.Font("C://Windows//Fonts//msyh.ttc", 32)
                score_text = score_font.render("分数：%s" % str(score), True, (255, 255, 255))
                screen.blit(score_text, (size[0] // 2 - 70 , size[1] // 2 - 20))


        pygame.display.update()
        fclock.tick(fsp)




class Hero(pygame.sprite.Sprite):
    """hero"""
    def __init__(self,size):
        """初始hero属性"""
        pygame.sprite.Sprite.__init__(self)

        self.size = size
        #引入hero图片
        self.hero1 = pygame.image.load("Sprites/hero/fly/hero1.png").convert_alpha()
        self.hero2 = pygame.image.load("Sprites/hero/fly/hero2.png").convert_alpha()

        self.hero_blast_list = []
        self.hero_blast_list.extend([\
            pygame.image.load("Sprites/hero/down/hero_blowup_n1.png").convert_alpha(),\
            pygame.image.load("Sprites/hero/down/hero_blowup_n2.png").convert_alpha(),\
            pygame.image.load("Sprites/hero/down/hero_blowup_n3.png").convert_alpha(),\
            pygame.image.load("Sprites/hero/down/hero_blowup_n4.png").convert_alpha(),\
            ])

        self.rect = self.hero1.get_rect()
        self.rect.center = self.size[0] // 2,self.size[1] // 2 + 320

        self.dealy = 100
        self.dealy_key = 100

        self.active = True

        self.mask = pygame.mask.from_surface(self.hero1)



    def hero_show(self,screen):
        """hero 动画"""
        if self.dealy % 2 == 0:
            screen.blit(self.hero1,self.rect)
        elif self.dealy % 2 == 1:
            screen.blit(self.hero2,self.rect)

        if not(self.dealy_key % 10):
            self.dealy -= 1
        self.dealy_key -= 1

        if self.dealy == 0:
            self.dealy = 100
        if self.dealy_key == 0:
            self.dealy_key = 100

    def hero_move(self):
        """hero移动控制方法"""
        self.key_pressed = pygame.key.get_pressed()
        if self.key_pressed[pygame.K_LEFT]:
            if self.rect.left > 0:
                self.rect.left -= 4
            else:
                pass
        if self.key_pressed[pygame.K_RIGHT]:
            if self.rect.right < self.size[0]:
                self.rect.right += 4
            else:
                pass
        if self.key_pressed[pygame.K_UP]:
            if self.rect.top > 0:
                self.rect.top -= 4
            else:
                pass
        if self.key_pressed[pygame.K_DOWN]:
            if self.rect.top < self.size[1] - 130:
                self.rect.top += 4
            else:
                pass


    def hero_down(self):
        """hero碰撞检测"""
        pass

    def hero_blast(self,screen):
        """hero爆炸方法"""
        if self.dealy % 4 == 0:
            screen.blit(self.hero_blast_list[0], self.rect)
        elif self.dealy % 4 == 3:
            screen.blit(self.hero_blast_list[1], self.rect)
        elif self.dealy % 4 == 2:
            screen.blit(self.hero_blast_list[2], self.rect)
        elif self.dealy % 4 == 1:
            screen.blit(self.hero_blast_list[3], self.rect)

        if not (self.dealy_key % 10):
            self.dealy -= 1
        self.dealy_key -= 1

        if self.dealy == 0:
            self.dealy = 100
        if self.dealy_key == 0:
            self.dealy_key = 100

class Enemy(pygame.sprite.Sprite):
    """enemy"""
    def __init__(self,size):
        """enemy属性"""
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        #导入图片
        self.enemy = pygame.image.load("Sprites/Enemy1/fly/enemy1.png").convert_alpha()
        self.enemy_blast_list = []
        self.enemy_blast_list.extend([\
            pygame.image.load("Sprites/Enemy1/down/enemy1_down1.png").convert_alpha(),\
            pygame.image.load("Sprites/Enemy1/down/enemy1_down2.png").convert_alpha(),\
            pygame.image.load("Sprites/Enemy1/down/enemy1_down3.png").convert_alpha(),\
            pygame.image.load("Sprites/Enemy1/down/enemy1_down4.png").convert_alpha(),\
            ])

        self.rect = self.enemy.get_rect()
        self.speed = 2

        self.active = True

        self.dealy = 100
        self.dealy_key = 50

        self.rect.center = randint(0,self.size[0]),randint(-5*self.size[1],0)

        self.mask = pygame.mask.from_surface(self.enemy)

    def move(self):
        """enemy move"""
        if self.rect.top < self.size[1]:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        """出画回到机库"""
        self.rect.center = randint(0,self.size[0]),randint(-5*self.size[1],0)
        self.active = True

    def enemy_blast(self,screen):
        """hero爆炸方法"""
        if self.dealy % 4 == 0:
            screen.blit(self.enemy_blast_list[0], self.rect)
        elif self.dealy % 4 == 3:
            screen.blit(self.enemy_blast_list[1], self.rect)
        elif self.dealy % 4 == 2:
            screen.blit(self.enemy_blast_list[2], self.rect)
        elif self.dealy % 4 == 1:
            screen.blit(self.enemy_blast_list[3], self.rect)

        if not (self.dealy_key % 10):
            self.dealy -= 1
        self.dealy_key -= 1

        if self.dealy == 0:
            self.dealy = 100
        if self.dealy_key == 0:
            self.dealy_key = 50
            self.reset()




class Hero_bullet(pygame.sprite.Sprite):
    """hero bullte"""
    def __init__(self,pos):
        """bullte 属性"""
        pygame.sprite.Sprite.__init__(self)

        self.hero_bullet = pygame.image.load("Sprites/bullet/fly/bullet2.png").convert_alpha()
        self.rect = self.hero_bullet.get_rect()
        self.rect.center = pos

        self.speed = 8

        self.active = True

        self.mask = pygame.mask.from_surface(self.hero_bullet)

    def move(self):
        self.rect.top -= self.speed

    def reset(self,pos):
        self.posx,self.posy = pos
        self.rect.center = self.posx,self.posy+10




class Enemy_bullte(pygame.sprite.Sprite):
    """enemy bullte"""
    def __init__(self,pos):
        """bullte 属性"""
        pygame.sprite.Sprite.__init__(self)

        self.enemy_bullet = pygame.image.load("Sprites/bullet/fly/bullet1.png").convert_alpha()
        self.rect = self.enemy_bullet.get_rect()
        self.rect.center = pos

        self.speed = 2

        self.active = True

        self.mask = pygame.mask.from_surface(self.enemy_bullet)

    def move(self):
        self.rect.top += self.speed

    def reset(self, pos):
        self.posx,self.posy = pos[0],pos[1]+10
        self.rect.center = self.posx,self.posy






class Window(object):
    """窗口显示"""
    def __init__(self,size):
        """窗口属性"""

        self.size = size
        self.again = pygame.image.load("images/game_again.png").convert_alpha()
        self.continue_ = pygame.image.load("images/game_continue.png").convert_alpha()
        self.over = pygame.image.load("images/game_over.png").convert_alpha()
        self.pause_nor = pygame.image.load("images/game_pause_nor.png").convert_alpha()
        self.pause_pressed = pygame.image.load("images/game_pause_pressed.png").convert_alpha()
        self.resume_nor = pygame.image.load("images/game_resume_nor.png").convert_alpha()
        self.resume_nor = pygame.image.load("images/game_resume_pressed.png").convert_alpha()
        self.logo = pygame.image.load("images/logo.png").convert_alpha()


        self.again_rect = self.again.get_rect()
        self.continue_rect = self.continue_.get_rect()
        self.over_rect = self.over.get_rect()
        self.logo_rect = self.logo.get_rect()

        self.again_rect.center = self.size[0] // 2,self.size[1] // 2 + 100
        self.over_rect.center = self.size[0] // 2,self.size[1] // 2 + 50
        self.logo_rect.center = self.size[0] //2,200




main()