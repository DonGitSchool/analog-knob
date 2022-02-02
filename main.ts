input.onButtonPressed(Button.B, function () {
    music.setVolume(pins.map(
    pins.analogReadPin(AnalogPin.P2),
    800,
    1020,
    50,
    255
    ))
})
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P0) == 0) {
        music.startMelody(music.builtInMelody(Melodies.Funk), MelodyOptions.Once)
        pins.digitalWritePin(DigitalPin.P0, 1)
    }
    if (pins.analogReadPin(AnalogPin.P2) < 850) {
        images.createImage(`
            . . . . .
            . . . . .
            . . . . .
            . # . # .
            # # # # #
            `).showImage(0)
    }
    if (pins.analogReadPin(AnalogPin.P2) >= 850 && pins.analogReadPin(AnalogPin.P2) <= 900) {
        images.createImage(`
            . . . . .
            . . . . .
            . # . # .
            # # # # #
            # # # # #
            `).showImage(0)
    }
    if (pins.analogReadPin(AnalogPin.P2) < 900 && pins.analogReadPin(AnalogPin.P2) <= 950) {
        images.createImage(`
            . . . . .
            . . . . .
            . # . # .
            # # # # #
            # # # # #
            `).showImage(0)
    }
    if (pins.analogReadPin(AnalogPin.P2) > 950 && pins.analogReadPin(AnalogPin.P2) <= 1000) {
        images.createImage(`
            . . . . .
            . # . # .
            # # # # #
            # # # # #
            # # # # #
            `).showImage(0)
    }
    if (pins.analogReadPin(AnalogPin.P2) > 1000) {
        images.createImage(`
            . # . # .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `).showImage(0)
    }
})
