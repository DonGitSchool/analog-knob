def on_button_pressed_b():
    music.set_volume(pins.map(pins.analog_read_pin(AnalogPin.P3), 800, 1020, 50, 255))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    if pins.digital_read_pin(DigitalPin.P0) == 0:
        music.start_melody(music.built_in_melody(Melodies.FUNK), MelodyOptions.ONCE)
        pins.digital_write_pin(DigitalPin.P0, 1)
    if pins.digital_read_pin(DigitalPin.P3) < 850:
        images.create_image("""
            . . . . .
                        . . . . .
                        . . . . .
                        . # . # .
                        # # # # #
        """).show_image(0)
    if pins.digital_read_pin(DigitalPin.P3) >= 850 and pins.digital_read_pin(DigitalPin.P3) <= 900:
        images.create_image("""
            . . . . .
                        . . . . .
                        . # . # .
                        # # # # #
                        # # # # #
        """).show_image(0)
    if pins.digital_read_pin(DigitalPin.P3) < 900 and pins.digital_read_pin(DigitalPin.P3) <= 950:
        images.create_image("""
            . . . . .
                        . . . . .
                        . # . # .
                        # # # # #
                        # # # # #
        """).show_image(0)
    if pins.digital_read_pin(DigitalPin.P3) > 950 and pins.digital_read_pin(DigitalPin.P3) <= 1000:
        images.create_image("""
            . . . . .
                        . # . # .
                        # # # # #
                        # # # # #
                        # # # # #
        """).show_image(0)
    if pins.digital_read_pin(DigitalPin.P3) > 1000:
        images.create_image("""
            . # . # .
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """).show_image(0)
basic.forever(on_forever)
