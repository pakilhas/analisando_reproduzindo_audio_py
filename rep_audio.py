import pygame

pygame.init() #iniciando o pygame
pygame.mixer.music.load('X2Download.app - Ive Brussel - Jorge Ben Jor - Karaokê Violão (128 kbps).mp3') #pegando o audio
pygame.mixer.music.play()#reproduzindo o audio
input()
pygame.event.wait()

