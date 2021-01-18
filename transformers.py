import io
import os
import time
import vlc
from gtts import gTTS

ENDED = 6

def play_message(message: str):
    """
    Use google speech to text to convert message to mp3, then play it using
    VLC
    """
    print(message)
    tts = gTTS(message, lang="en-us")
    tts.save("/tmp/tmp.mp3")
    player = vlc.MediaPlayer("/tmp/tmp.mp3")
    player.play()
    while player.get_state() != ENDED:
        continue
    os.unlink("/tmp/tmp.mp3")

def get_user_input(prompt: str):
    """
    Gets user input using provided prompt.
    """
    play_message(prompt)
    return input()


if __name__ == '__main__':
    prompt = """
The Rescue Bots are in trouble! They need your help! Blades and Chase are at the station. Which one
will you help?

A) Chase
B) Blades
"""
    choice = {
        'a': 'Chase',
        'b': 'Blades'
    }[get_user_input(prompt).lower()];
    play_message(f'You chose {choice}');
    
