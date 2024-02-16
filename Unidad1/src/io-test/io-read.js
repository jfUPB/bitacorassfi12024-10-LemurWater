pins.onPulsed(DigitalPin.P0, PulseValue.High, function () {
	
})
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P0) == 1) {
        basic.showLeds(`
            . . # . .
            # # # . .
            . . # . .
            . . # . .
            # # # # #
            `)
    } else {
        basic.showLeds(`
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            `)
    }
})
