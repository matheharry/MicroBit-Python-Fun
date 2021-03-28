from microbit import *
import music
import random


TOLERANCE = 3000
nummer=0


def get_accelerometer_total():
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    return x + y + z


def wait_for_shake():
    shaken = False
    last = get_accelerometer_total()
    while not shaken:
        this = get_accelerometer_total()
        diff = last - this
        if diff < 0:
            diff = diff * -1
        if diff > TOLERANCE:
            shaken = True
        last = this
        sleep(50)


twinkle_twinkle = ['c4:4', 'c', 'g', 'g', 'a', 'a', 'g:8',
                    'f:4', 'f', 'e', 'e', 'd', 'd', 'c:8',
                    'g:4', 'g', 'f', 'f', 'e', 'e', 'd:8',
                    'g:4', 'g', 'f', 'f', 'e', 'e', 'd:8',
                    'c:4', 'c', 'g', 'g', 'a', 'a', 'g:8',
                    'f:4', 'f', 'e', 'e', 'd', 'd', 'c:8']

list_of_songs = [twinkle_twinkle, music.FUNERAL, music.DADADADUM, music.BIRTHDAY, music.ENTERTAINER, music.ODE,
music.PRELUDE, music.BLUES, music.PYTHON, music.NYAN]

while True:
    # display.show(Image.MUSIC_QUAVER)
    display.show(nummer)
    wait_for_shake()
    music.stop()
    nummer = random.randint(0, len(list_of_songs)-1)
    music.play(list_of_songs[nummer], wait=False)