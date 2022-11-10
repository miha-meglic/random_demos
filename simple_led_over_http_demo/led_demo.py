from serial import Serial
import time


def led_set(ser: Serial, led_id: int, red: int, green: int, blue: int, white: int):
    msg = led_id
    msg = (msg << 8) + red
    msg = (msg << 8) + green
    msg = (msg << 8) + blue
    msg = (msg << 8) + white

    ser.write(msg.to_bytes(5))


def led_set_all(ser: Serial, led_count: int,  red: int, green: int, blue: int, white: int):
    for led in range(led_count):
        led_set(ser, led, red, green, blue, white)


if __name__ == '__main__':
    s = Serial('COM4', 9600)

    time.sleep(2)
    led_set_all(s, 30, 128, 0, 64, 0)
