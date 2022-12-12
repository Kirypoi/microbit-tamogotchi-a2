//  bao
// -------ANIMATIONS--------
function poop() {
    
}

function play() {
    
}

function sleep() {
    
}

function feed_to_overfed_action(): number {
    basic.showLeds(`
        # . . . .
                . # . . .
                . . # . .
                . # . # .
                # . . . #
    `)
    return 0
}

// -------FUNCTIONS----------
//  Sing
input.onButtonPressed(Button.B, function on_button_pressed_a2() {
    sing()
})
input.onPinPressed(TouchPin.P0, function on_pin_pressed_p0() {
    music.stopAllSounds()
})
let playcounter = 0
//  Play
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    if (playcounter == 3) {
        playcounter = 0
        control.waitMicros(30000000)
    } else {
        play()
        playcounter += 1
        basic.showNumber(playcounter)
    }
    
})
// Sleep
let blsleep = false
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    
    if (blsleep == true) {
        control.waitMicros(100000000)
        blsleep = false
    } else {
        blsleep = true
        sleep()
    }
    
})
//  Eat
let eat_counter = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (eat_counter == 8) {
        eat_counter = 0
        //  do something fun
        control.waitMicros(30000000)
    } else {
        //  feed_to_overfed_action()
        eat_counter += 1
        basic.showNumber(eat_counter)
    }
    
    
})
//  def on_forever():
//      for index in range(4):
//          basic.show_leds("""
//              # . . . .
//                          . # . . .
//                          . . # . .
//                          . . . # .
//                          . . . # #
//          """)
//          basic.show_leds("""
//              # . . . #
//                          . # . # .
//                          . . # . .
//                          . # . # .
//                          # . . . #
//          """)
//  basic.forever(on_forever)
function sing() {
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
}

