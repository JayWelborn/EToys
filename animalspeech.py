import io
import os
import pygame
import time
import vlc
from gtts import gTTS

ENDED = 6


def get_user_input(prompt: str):
    """
    Gets user input using provided prompt.
    """
    play_message(prompt)
    return input()


def play_message(message: str):
    """
    Use google speech to text to convert message to mp3, then play it using
    VLC
    """
    print(message)
    tts = gTTS(message, lang="en-uk")
    pygame.mixer.init()
    tts.save("/tmp/tmp.mp3")
    player = vlc.MediaPlayer("/tmp/tmp.mp3")
    player.play()
    while player.get_state() != ENDED:
        continue
    os.unlink("/tmp/tmp.mp3")


if __name__ == "__main__":
    prompt = "What is your favorite animal?"
    animal = get_user_input(prompt)
    play_message(f"Your favorite animal is a {animal}.")
