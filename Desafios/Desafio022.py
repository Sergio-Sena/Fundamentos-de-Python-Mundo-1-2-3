#Faça um programa que carregue a reprudiza um audio MP3

import pygame
pygame.init()
pygame.mixer.music.load('Desafio022.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()