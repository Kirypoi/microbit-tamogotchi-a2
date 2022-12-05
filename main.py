
# bao
def poop():
    pass
# bao
def sing():
    pass
# play
def play():
    pass
# sleep
def sleep():
    pass
# emotions animation (state)
# def happy():
# display.show_leds("""
# . . . . .
# . . . . .
# . . # . .
# . . . . .
# . . . . .
# """)
# sleep(400)
# def sad():
# display.show_leds("""
# . . . . .
# . . . . .
# . . # . .
# . . . . .
# . . . . .
# """)
# sleep(400)
# activties
# phuc
def feed():
    pass

def on_gesture_shake():
    global playcounter
    if playcounter == 3:
        playcounter = 0
        control.wait_micros(30000000)
    else:
        play()
        playcounter += 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    global blsleep
    if blsleep == True:
        control.wait_micros(100000000)
        blsleep = False
    else:
        blsleep = True
    sleep()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

playcounter = 0
blsleep = False
blsleep = False
playcounter = 0

def on_forever():
    for index in range(4):
        basic.show_leds("""
            # . . . .
                        . # . . .
                        . . # . .
                        . . . # .
                        . . . # #
        """)
        basic.show_leds("""
            # . . . #
                        . # . # .
                        . . # . .
                        . # . # .
                        # . . . #
        """)
basic.forever(on_forever)
