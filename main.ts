function poop() {
    //  bao
    
}

function sing() {
    //  bao
    
}

function play() {
    //  play 
    
}

function sleep() {
    //  sleep
    
}

//  emotions animation (state)
//  def happy():
//  display.show_leds("""
//  . . . . .
//  . . . . .
//  . . # . .
//  . . . . .
//  . . . . .
//  """)
//  sleep(400)
//  def sad():
//  display.show_leds("""
//  . . . . .
//  . . . . .
//  . . # . .
//  . . . . .
//  . . . . .
//  """)
//  sleep(400)
//  activties
function feed() {
    //  phuc
    
}

basic.forever(function on_forever() {
    for (let index = 0; index < 4; index++) {
        basic.showLeds(`
            # . . . .
                        . # . . .
                        . . # . .
                        . . . # .
                        . . . . #
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
