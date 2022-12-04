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
        control.waitMicros(30000000)
        playcounter = 0
    } else {
        play()
        playcounter += 1
    }
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    if (blsleep == true) {
        blsleep = false
        control.waitMicros(100000000)
    } else {
        blsleep = true
    }
    sleep()
})
let playcounter = 0
let blsleep = false
blsleep = false
playcounter = 0
basic.forever(function () {
    for (let index = 0; index < 4; index++) {
        basic.showLeds(`
            # . . . .
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
