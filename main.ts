//  bao
function poop() {
    
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

//  When fed shows emotion
function feedToDefaultAction(): number {
    basic.showLeds(`
        # . . . .
        . # . . .
        . . # . .
        . . . # .
        . . . . #
    `)
    return 0
}

function feedToOverFedAction(): number {
    basic.showLeds(`
            # . . . .
            . # . . .
            . . # . .
            . # . # .
            # . . . #
        `)
    return 0
}

function feedRecorder(counter: () => void): () => void {
    let result = counter
    result += 1
    return result
}

function main(): number {
    feedACtionChangesToInputNumber
    return 0
}

