
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
#-------FUNCTIONALS----------
# Out
def on_pin_pressed_p1():
    basic.show_number(90)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

# Sing
def on_button_pressed_a2_do_action_sing():
    sing()
input.on_button_pressed(Button.B, on_button_pressed_a2_do_action_sing)

def on_pin_pressed_p0_mute_all_sounds():
    music.stop_all_sounds()
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0_mute_all_sounds)

playcounter = 0
# Play
def on_gesture_shake_start_play_action():
    global playcounter
    if playcounter == 3:
        playcounter = 0
        control.wait_micros(30000000)
    else:
        play()
        playcounter += 1
        basic.show_number(playcounter)
input.on_gesture(Gesture.SHAKE, on_gesture_shake_start_play_action)

#Sleep
blsleep = False
def on_logo_pressed_do_action_sleep():
    global blsleep
    if blsleep == True:
        control.wait_micros(100000000)
        blsleep = False
    else:
        basic.show_icon(IconNames.ASLEEP)
        blsleep = True
        sleep()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed_do_action_sleep)

# Eat
eat_counter = 0
def on_button_pressed_a_start_action_feeding():
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
input.on_button_pressed(Button.A, on_button_pressed_a_start_action_feeding)

# Evolution Timer
timer = 0
def on_forever():
    # is_shaked = input.is_gesture(Gesture.Shake)
    # a_button_is_pressed = input.button_is_pressed(Button.A)
    # b_button_is_pressed = input.button_is_pressed(Button.B)
    while timer < 30:
        basic.show_number(timer)
        
        timer = timer + 5
basic.forever(on_forever)

# if timer == 20:
#     basic.show_number(timer)

# ------------:3---------------
# Never let you go
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



