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

//  When fed shows emotion
function feed_to_default_action(): number {
    basic.showLeds(`
        # # . . .
        . # # . .
        . . # . .
        . . . # .
        . . . . #
    `)
    return 0
}

//  bao
function poop() {
    
}

function feed_action_changes_to_input_number(counter: number) {
    //  basic.show_number(9)
    if (counter > 0 && counter <= 4) {
        feed_to_default_action()
    }
    
    if (counter > 4 && counter <= 8) {
        feed_to_overfed_action()
    }
    
    if (counter > 8) {
        basic.showString("It's dead.")
    }
    
}

function feed_input() {
    //  input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)
    input.onPinPressed(TouchPin.P0, feed_to_default_action)
}

let counter = 0
function on_pin_pressed_p0() {
    let counter: number;
    feed_action_changes_to_input_number(counter)
    counter = counter + 1
}

//  bao
function sing() {
    
}

//  play
function play() {
    
}

//  sleep
function sleep() {
    
}

function main(): number {
    feed_input()
    //  basic.show_number(9)
    return 0
}

main()
