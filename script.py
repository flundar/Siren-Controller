from pynput import keyboard
import sys
import os

old_stdout = sys.stdout
sys.stdout = open(os.devnull, 'w')

import pygame

# Standart çıktıyı geri yükle
sys.stdout = old_stdout
# Pygame'i başlat
pygame.mixer.init()


print("made by senior with ♥")
base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# Ses dosyalarının yolu
sound1_path = os.path.join(base_path, 'sound1.ogg')
sound2_path = os.path.join(base_path, 'sound2.ogg')
# Ses dosyalarını yükle
sound1 = pygame.mixer.Sound(sound1_path)
sound2 = pygame.mixer.Sound(sound2_path)

# Ses kanallarını oluştur
channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)


listener = keyboard.Listener()

# 'q' ve 'alt' tuşlarına basıldığında ses çalmak için bir işlem tanımla
def on_press(key):
    try:
        if key.char == 'q':
            channel1.play(sound2)
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
        channel2.play(sound1)


# Klavye dinleyicisine tuş basım işlemini ekle
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

# Sonsuz döngü, programın kapatılana kadar çalışmasını sağlar
while True:
    pass
