import pygame

# Inicializa o mixer do pygame
pygame.mixer.init()

# Carrega o arquivo MP3
pygame.mixer.music.load("Mundo1/exer21.mp3")

# Toca o arquivo
pygame.mixer.music.play()

# Mantém o programa rodando até o som terminar
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)



