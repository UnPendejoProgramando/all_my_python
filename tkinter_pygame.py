import pygame
from tkinter import *


def audio_play():
    pygame.mixer.music.load("audio.wav")
    pygame.mixer.music.play(-1)

    

screen = Tk()
pygame.init()

play = Button(screen, text = "Play", command = audio_play)
play.grid(row = 0, column = 0)
stop = Button(screen, text = "Stop")
stop.grid(row = 0, column = 1)
screen.mainloop()