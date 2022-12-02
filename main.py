def poop(): # bao
    pass
def sing(): # bao
    pass
def play(): # play 
    pass
def sleep(): # sleep
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
def feed(): # phuc
    pass

def on_forever():
    for index in range(4):
        basic.show_leds("""
            # . . . .
                        . # . . .
                        . . # . .
                        . . . # .
                        . . . . #
        """)
        basic.show_leds("""
            # . . . #
                        . # . # .
                        . . # . .
                        . # . # .
                        # . . . #
        """)
basic.forever(on_forever)
