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
# When fed shows emotion
def feedToDefaultAction():
    basic.show_leds("""
        # . . . .
        . # . . .
        . . # . .
        . . . # .
        . . . . #
    """)
    return 0

def feedToOverFedAction():
    basic.show_leds("""
            # . . . .
            . # . . .
            . . # . .
            . # . # .
            # . . . #
        """)
    return 0

def feedRecorder(counter:int) -> int:
    result = counter
    result += 1
    return result

def feedACtionChangesToInputNumber():
    counter = 0
    input.on_pin_pressed(TouchPin.P0, feedRecorder(counter))
        
    if (counter > 0 & counter <= 4):
        feedToDefaultAction()
    if (counter > 4 & counter <= 8):
        feedToOverFedAction()
    else: basic.show_string("It's dead.")
    
    return 0    

def main():
    feedACtionChangesToInputNumber()
    return 0

main()