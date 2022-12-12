

# bao
#-------ANIMATIONS--------
def poop(): 
    pass
def play(): 
    pass
def sleep(): 
    pass
def feed_to_overfed_action():
    basic.show_leds("""
        # . . . .
                . # . . .
                . . # . .
                . # . # .
                # . . . #
    """)
    return 0
#-------FUNCTIONS----------

# Sing
def on_button_pressed_a2():
    sing()
input.on_button_pressed(Button.B, on_button_pressed_a2)

def on_pin_pressed_p0():
    music.stop_all_sounds()
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

playcounter = 0
# Play
def on_gesture_shake():
    global playcounter
    if playcounter == 3:
        playcounter = 0
        control.wait_micros(30000000)
    else:
        play()
        playcounter += 1
        basic.show_number(playcounter)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

#Sleep
blsleep = False
def on_logo_pressed():
    global blsleep
    if blsleep == True:
        control.wait_micros(100000000)
        blsleep = False
    else:
        blsleep = True
        sleep()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

# Eat
eat_counter = 0
def on_button_pressed_a():
    global eat_counter
    if eat_counter == 8:
        eat_counter = 0
        # do something fun
        control.wait_micros(30000000)
    else:
        # feed_to_overfed_action()
        eat_counter += 1
        basic.show_number(eat_counter)
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)


# def on_forever():
#     for index in range(4):
#         basic.show_leds("""
#             # . . . .
#                         . # . . .
#                         . . # . .
#                         . . . # .
#                         . . . # #
#         """)
#         basic.show_leds("""
#             # . . . #
#                         . # . # .
#                         . . # . .
#                         . # . # .
#                         # . . . #
#         """)
# basic.forever(on_forever)

def sing():
    music.playTone(277, music.beat(BeatFraction.Whole))
    basic.pause(200)
    music.playTone(311, music.beat(BeatFraction.Whole))
    basic.pause(200)
    music.playTone(208, music.beat(BeatFraction.Whole))
    basic.pause(100)
    music.playTone(311, music.beat(BeatFraction.Whole))
    basic.pause(200)
    music.playTone(349, music.beat(BeatFraction.Whole))
    basic.pause(100)
    music.playTone(415, music.beat(BeatFraction.Quarter))
    music.playTone(370, music.beat(BeatFraction.Quarter))
    music.playTone(349, music.beat(BeatFraction.Quarter))
    music.playTone(311, music.beat(BeatFraction.Quarter))
    music.playTone(277, music.beat(BeatFraction.Whole))
    basic.pause(100)
    music.playTone(311, music.beat(BeatFraction.Whole))
    basic.pause(100)
    music.playTone(208, music.beat(BeatFraction.Double))
    music.playTone(415, music.beat(BeatFraction.Quarter))
    music.playTone(370, music.beat(BeatFraction.Quarter))
    music.playTone(349, music.beat(BeatFraction.Quarter))
    music.playTone(311, music.beat(BeatFraction.Quarter))
    music.playTone(277, music.beat(BeatFraction.Whole))
    basic.pause(200)
    music.playTone(311, music.beat(BeatFraction.Whole))
    basic.pause(200)
    music.playTone(208, music.beat(BeatFraction.Whole))
    basic.pause(100)
    music.playTone(311, music.beat(BeatFraction.Whole))
    basic.pause(200)
    music.playTone(349, music.beat(BeatFraction.Whole))
    basic.pause(100)
    music.playTone(415, music.beat(BeatFraction.Quarter))
    music.playTone(370, music.beat(BeatFraction.Quarter))
    music.playTone(349, music.beat(BeatFraction.Quarter))
    music.playTone(311, music.beat(BeatFraction.Quarter))
    music.playTone(277, music.beat(BeatFraction.Whole))
    basic.pause(100)
    music.playTone(311, music.beat(BeatFraction.Whole))
    basic.pause(100)
    music.playTone(208, music.beat(BeatFraction.Double))
    music.playTone(277, music.beat(BeatFraction.Quarter))
    music.playTone(277, music.beat(BeatFraction.Quarter))
    basic.pause(200)
    music.playTone(277, music.beat(BeatFraction.Quarter))
    music.playTone(277, music.beat(BeatFraction.Quarter))
    basic.pause(500)
    music.playTone(233, music.beat(BeatFraction.Half))
    music.playTone(262, music.beat(BeatFraction.Half))
    music.playTone(277, music.beat(BeatFraction.Half))
    music.playTone(277, music.beat(BeatFraction.Half))
    music.playTone(311, music.beat(BeatFraction.Half))
    music.playTone(262, music.beat(BeatFraction.Half))
    music.playTone(233, music.beat(BeatFraction.Half))
    music.playTone(208, music.beat(BeatFraction.Double))
    basic.pause(200)
    music.playTone(233, music.beat(BeatFraction.Half))
    music.playTone(233, music.beat(BeatFraction.Half))
    music.playTone(262, music.beat(BeatFraction.Half))
    music.playTone(277, music.beat(BeatFraction.Half))
    music.playTone(233, music.beat(BeatFraction.Half))
    music.playTone(208, music.beat(BeatFraction.Half))
    music.playTone(415, music.beat(BeatFraction.Whole))
    music.playTone(415, music.beat(BeatFraction.Half))
    music.playTone(311, music.beat(BeatFraction.Double))
    basic.pause(200)
    music.playTone(233, music.beat(BeatFraction.Half))
    music.playTone(233, music.beat(BeatFraction.Half))
    music.playTone(262, music.beat(BeatFraction.Half))
    music.playTone(277, music.beat(BeatFraction.Half))
    music.playTone(233, music.beat(BeatFraction.Half))
    music.playTone(277, music.beat(BeatFraction.Half))
    music.playTone(311, music.beat(BeatFraction.Half))
    music.playTone(262, music.beat(BeatFraction.Half))
    music.playTone(233, music.beat(BeatFraction.Half))
    music.playTone(208, music.beat(BeatFraction.Double))
    basic.pause(200)
    music.playTone(233, music.beat(BeatFraction.Half))
    music.playTone(233, music.beat(BeatFraction.Half))
    music.playTone(262, music.beat(BeatFraction.Half))
    music.playTone(277, music.beat(BeatFraction.Half))
    music.playTone(233, music.beat(BeatFraction.Half))
    music.playTone(208, music.beat(BeatFraction.Half))
    music.playTone(311, music.beat(BeatFraction.Half))
    music.playTone(311, music.beat(BeatFraction.Half))
    music.playTone(311, music.beat(BeatFraction.Half))
    music.playTone(349, music.beat(BeatFraction.Half))
    music.playTone(311, music.beat(BeatFraction.Double))
    basic.pause(200)
    music.playTone(277, music.beat(BeatFraction.Double))
    music.playTone(311, music.beat(BeatFraction.Half))
    music.playTone(349, music.beat(BeatFraction.Half))
    music.playTone(277, music.beat(BeatFraction.Half))
    music.playTone(311, music.beat(BeatFraction.Half))
    music.playTone(311, music.beat(BeatFraction.Half))
    music.playTone(311, music.beat(BeatFraction.Half))
    music.playTone(349, music.beat(BeatFraction.Half))
    music.playTone(311, music.beat(BeatFraction.Half))
    music.playTone(208, music.beat(BeatFraction.Half))
    music.playTone(208, music.beat(BeatFraction.Double))
    basic.pause(200)
    music.playTone(233, music.beat(BeatFraction.Half))
    music.playTone(262, music.beat(BeatFraction.Half))
    music.playTone(277, music.beat(BeatFraction.Half))
    music.playTone(233, music.beat(BeatFraction.Half))
    music.playTone(311, music.beat(BeatFraction.Half))
    music.playTone(349, music.beat(BeatFraction.Half))
    music.playTone(311, music.beat(BeatFraction.Double))
    basic.pause(200)
    music.playTone(233, music.beat(BeatFraction.Quarter))
    music.playTone(262, music.beat(BeatFraction.Quarter))
    music.playTone(277, music.beat(BeatFraction.Quarter))
    music.playTone(233, music.beat(BeatFraction.Quarter))
    music.playTone(349, music.beat(BeatFraction.Half))
    music.playTone(349, music.beat(BeatFraction.Half))
    music.playTone(311, music.beat(BeatFraction.Double))
    basic.pause(200)
    music.playTone(208, music.beat(BeatFraction.Quarter))
    music.playTone(233, music.beat(BeatFraction.Quarter))
    music.playTone(262, music.beat(BeatFraction.Quarter))
    music.playTone(208, music.beat(BeatFraction.Quarter))
    music.playTone(311, music.beat(BeatFraction.Half))
    music.playTone(311, music.beat(BeatFraction.Half))
    music.playTone(277, music.beat(BeatFraction.Half))
    music.playTone(262, music.beat(BeatFraction.Half))
    music.playTone(233, music.beat(BeatFraction.Half))
    music.playTone(233, music.beat(BeatFraction.Quarter))
    music.playTone(262, music.beat(BeatFraction.Quarter))
    music.playTone(277, music.beat(BeatFraction.Quarter))
    music.playTone(233, music.beat(BeatFraction.Quarter))
    music.playTone(277, music.beat(BeatFraction.Half))
    music.playTone(311, music.beat(BeatFraction.Quarter))
    music.playTone(262, music.beat(BeatFraction.Half))
    music.playTone(233, music.beat(BeatFraction.Half))
    music.playTone(208, music.beat(BeatFraction.Half))
    music.playTone(175, music.beat(BeatFraction.Half))
    music.playTone(311, music.beat(BeatFraction.Half))
    music.playTone(277, music.beat(BeatFraction.Double))
    basic.pause(200)
    music.playTone(233, music.beat(BeatFraction.Quarter))
    music.playTone(262, music.beat(BeatFraction.Quarter))
    music.playTone(277, music.beat(BeatFraction.Quarter))
    music.playTone(233, music.beat(BeatFraction.Quarter))
    music.playTone(349, music.beat(BeatFraction.Half))
    music.playTone(349, music.beat(BeatFraction.Half))
    music.playTone(311, music.beat(BeatFraction.Double))
    basic.pause(200)
    music.playTone(208, music.beat(BeatFraction.Quarter))
    music.playTone(233, music.beat(BeatFraction.Quarter))
    music.playTone(262, music.beat(BeatFraction.Quarter))
    music.playTone(208, music.beat(BeatFraction.Quarter))
    music.playTone(277, music.beat(BeatFraction.Whole))
    music.playTone(262, music.beat(BeatFraction.Half))
    music.playTone(277, music.beat(BeatFraction.Half))
    music.playTone(262, music.beat(BeatFraction.Half))
    music.playTone(233, music.beat(BeatFraction.Half))
    music.playTone(208, music.beat(BeatFraction.Quarter))
    music.playTone(233, music.beat(BeatFraction.Quarter))
    music.playTone(262, music.beat(BeatFraction.Quarter))
    music.playTone(208, music.beat(BeatFraction.Quarter))
    music.playTone(277, music.beat(BeatFraction.Half))
    music.playTone(311, music.beat(BeatFraction.Quarter))
    music.playTone(262, music.beat(BeatFraction.Half))
    music.playTone(233, music.beat(BeatFraction.Half))
    music.playTone(208, music.beat(BeatFraction.Half))
    music.playTone(175, music.beat(BeatFraction.Half))
    music.playTone(311, music.beat(BeatFraction.Half))
    music.playTone(277, music.beat(BeatFraction.Double))