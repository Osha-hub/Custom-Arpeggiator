from microbit import *
from machine import time_pulse_us
import math

trig = pin13
echo = pin14

trig.write_digital(0)
echo.read_digital()

def midiControlChange(chan, n, value):
    MIDI_CC = 0xB0
    if chan > 15:
        return
    if n > 127:
        return
    if value > 127:
        return
    msg = bytes([MIDI_CC | chan, n, value])
    uart.write(msg)

def Start():
        uart.init(baudrate=31250, bits=8, parity=None, stop=1, tx=pin16)

Start()
last_pot_1 = 0
last_pot_2 = 0
last_depth = 0
current_depth = 0
lastA = False
lastB = False
hold = 0
sync = 0
while True:
    # bottons declaration
    a = button_a.is_pressed()
    b = button_b.is_pressed()
    # Arpeggiator's Hold function
    if a is True and lastA is False:
        hold += 1
        if hold > 1:
            hold = 0
    if hold == 0:
        # Depth Sensor
        trig.write_digital(1)
        trig.write_digital(0)
        micros = time_pulse_us(echo, 1)
        t_echo = micros/1000000
        dist = (t_echo / 2) * 34300
        if dist < 20:
            current_depth = int(127*dist/20)
        if last_depth != current_depth:
            midiControlChange(0, 23, current_depth)
        last_depth = current_depth
    # Arpeggiator's Sync function
    if b is True and lastB is False:
        sync += 1
        if sync > 1:
            sync = 0
        midiControlChange(0, 20, sync)
    # Pottenciometers
    pot1 = pin2.read_analog()
    if last_pot_1 != pot1:
        knob_cc = math.floor(pot1 / 1024 * 127)
        midiControlChange(0, 22, knob_cc)
    pot2 = pin1.read_analog()
    if last_pot_2 != pot2:
        knob_cc = math.floor(pot2 / 1024 * 127)
        midiControlChange(0, 21, knob_cc)

    # Preparing next loop
    lastA = a
    lastB = b
    last_pot_1 = pot1
    last_pot_2 = pot2

    sleep(50)
