# coding=utf-8

import pygame


class Ship():

    def __init__(self, screen):
        """初始化飞船"""
        self.screen = screen

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #新船放在底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):

        self.screen.blit(self.image, self.rect)