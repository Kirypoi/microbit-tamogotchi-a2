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
    basic.show_leds("""
        . . # # #
                # # # # .
                # # # # .
                # # # # .
                # # . . .
    """)
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
        control.wait_micros(30000000)
        playcounter = 0
    else:
        play()
        playcounter +=1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    global blsleep
    if blsleep == True:
        blsleep = False
        control.wait_micros(100000000)
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
