"""
Jouer sons avec boutons et LEDs
"""
from time import sleep
import pygame
from gpiozero import LED, Button, MCP3008
# from pydub import AudioSegment

# LEDs et boutons
led_red = LED(17)         # gpio17
led_yellow = LED(27)      # gpio27
led_green = LED(22)       # gpio22

button_red = Button(2)    # gpio2
button_yellow = Button(3)  # gpio3
button_green = Button(4)  # gpio4

potentiometer = MCP3008(channel=0)

# Initialisation de pygame
# Voir https://projects.raspberrypi.org/en/projects/gpio-music-box/1
# pygame.mixer.init()
# sound_red = pygame.mixer.Sound("chemin/vers/son/rouge.wav")
# sound_yellow = pygame.mixer.Sound("chemin/vers/son/jaune.wav")
# sound_green = pygame.mixer.Sound("chemin/vers/son/vert.wav")


# Fonctions pour allumer les LEDs
def toggle_red():
    """
    Allume la LED rouge
    """
    led_red.toggle()


def toggle_yellow():
    """
    Allume la LED jaune
    """
    led_yellow.toggle()


def toggle_green():
    """
    Allume la LED verte
    """
    led_green.toggle()


# Fonctions pour jouer les sons
def play_red():
    """
    Joue le son rouge
    """
    # sound_red.play()


def play_yellow():
    """
    Joue le son jaune
    """
    # sound_yellow.play()


def play_green():
    """
    Joue le son vert
    """
    # sound_green.play()


def get_potentiometer_value():
    """
    Récupère la valeur du potentiomètre en secondes
    """
    # Transformer la valeur du potentiomètre entre 0 et 1 en secondes
    val_in_seconds = potentiometer.value * 10
    return round(val_in_seconds)


# Associer les fonctions aux boutons
button_red.when_pressed = toggle_red
button_yellow.when_pressed = toggle_yellow
button_green.when_pressed = toggle_green


def export_sound():
    """
    Exporte les sons avec pydub (à tester)
    """
    # nb_sounds_to_play = 0

    # Trouver quels leds sont allumées
    # if led_red.value == 1:
    #     nb_sounds_to_play += 1

    # if led_yellow.value == 1:
    #     nb_sounds_to_play += 1

    # if led_green.value == 1:
    #     nb_sounds_to_play += 1

    # Loader sons avec pydub
    # sound = AudioSegment.from_wav("kick2.wav")
    # delay = AudioSegment.silent(duration=get_potentiometer_value() * 1000)

    # sound = None
    # Combiner les sons avec un delay
    # for i in range(nb_sounds_to_play):
    # sound += sound + delay

    # Exporter le son
    # combined.export("output.wav", format="wav")
    return True


# Boucle infinie pour jouer les sons
while True:
    # Si led rouge est allumée, jouer le son rouge
    if led_red.value == 1:
        play_red()
        sleep(get_potentiometer_value())

    # Si led jaune est allumée, jouer le son jaune
    if led_yellow.value == 1:
        play_yellow()
        sleep(get_potentiometer_value())

    # Si led verte est allumée, jouer le son vert
    if led_green.value == 1:
        play_green()
        sleep(get_potentiometer_value())

    # Attendre 0.1 seconde
    sleep(0.1)
    # pygame.time.wait(1000)

