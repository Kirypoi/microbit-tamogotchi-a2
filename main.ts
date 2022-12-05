// bao
function poop () {
	
}
// bao
function sing () {
	
}
// play
function play () {
	
}
// sleep
function sleep () {
	
}
// emotions animation (state)
// def happy():
// display.show_leds("""
// . . . . .
// . . . . .
// . . # . .
// . . . . .
// . . . . .
// """)
// sleep(400)
// def sad():
// display.show_leds("""
// . . . . .
// . . . . .
// . . # . .
// . . . . .
// . . . . .
// """)
// sleep(400)
// activties
// phuc
function feed () {
	
}
input.onGesture(Gesture.Shake, function () {
    if (playcounter == 3) {
        playcounter = 0
        control.waitMicros(30000000)
    } else {
        if (blplay == true) {
            play()
            playcounter += 1
            control.waitMicros(1000000)
            blplay = false
        } else {
            blplay = true
        }
    }
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    if (blsleep == true) {
        sleep()
        control.waitMicros(100000000)
        blplay = false
    } else {
        blsleep = true
    }
})
let blplay = false
let playcounter = 0
let blsleep = false
blsleep = true
playcounter = 0
blplay = true
basic.forever(function () {
    for (let index = 0; index < 4; index++) {
        basic.showLeds(`
            # . . # .
            . # . . .
            . . # . .
            . . . # .
            . . . # #
            `)
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
    }
})
