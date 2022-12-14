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

// -------FUNCTIONALS----------
//  Out
input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
    basic.showNumber(90)
})
//  Sing
input.onButtonPressed(Button.B, function on_button_pressed_a2_do_action_sing() {
    sing()
})
input.onPinPressed(TouchPin.P0, function on_pin_pressed_p0_mute_all_sounds() {
    music.stopAllSounds()
})
let playcounter = 0
//  Play
input.onGesture(Gesture.Shake, function on_gesture_shake_start_play_action() {
    
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
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed_do_action_sleep() {
    
    if (blsleep == true) {
        control.waitMicros(100000000)
        blsleep = false
    } else {
        basic.showIcon(IconNames.Asleep)
        blsleep = true
        sleep()
    }
    
})
//  Eat
let eat_counter = 0
input.onButtonPressed(Button.A, function on_button_pressed_a_start_action_feeding() {
    
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
//  Evolution Timer
let timer = 0
basic.forever(function on_forever() {
    let timer: number;
    //  is_shaked = input.is_gesture(Gesture.Shake)
    //  a_button_is_pressed = input.button_is_pressed(Button.A)
    //  b_button_is_pressed = input.button_is_pressed(Button.B)
    while (timer < 30) {
        basic.showNumber(timer)
        timer = timer + 5
    }
})
//  if timer == 20:
//      basic.show_number(timer)
//  ------------:3---------------
//  Never let you go
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

