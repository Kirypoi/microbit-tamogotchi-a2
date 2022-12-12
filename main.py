def feed_to_overfed_action():
    basic.show_leds("""
        # . . . .
                . # . . .
                . . # . .
                . # . # .
                # . . . #
    """)
    return 0
# When fed shows emotion
def feed_to_default_action():
    basic.show_leds("""
        # # . . .
        . # # . .
        . . # . .
        . . . # .
        . . . . #
    """)
    return 0
# bao
def poop():
    pass

def feed_action_changes_to_input_number(counter:int):
    # basic.show_number(9)
    if counter > 0 and counter <= 4:
        feed_to_default_action()
    if counter > 4 and counter <= 8:
        feed_to_overfed_action()
    if counter > 8:
        basic.show_string("It's dead.")
    
def feed_input():
    # input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)
    input.on_pin_pressed(TouchPin.P0, feed_to_default_action)

counter = 0
def on_pin_pressed_p0():
    feed_action_changes_to_input_number(counter)
    counter = counter + 1
    
# bao
def sing():
    pass
# play
def play():
    pass
# sleep
def sleep():
    pass

def main():
    feed_input()
    # basic.show_number(9)
    return 0

main()

input.onButtonPressed(Button.A, function () {
    basic.showString("Pls Subscribe!")
})
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
basic.forever(function () {
	
})
