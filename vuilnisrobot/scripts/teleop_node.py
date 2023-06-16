#!/usr/bin/env python3

import serial
import time

# Open the serial port with the appropriate baud rate
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

# Delay to allow time for the serial port to initialize
time.sleep(2)

# Send commands over the serial port
try:
    while True:
        command = input("Enter a command (w: forward, s: stop, x: Reverse, a: turn left, d: turn right, q: open gripper, e: close gripper): ")
        if command in ['w', 's', 'x', 'a', 'd', 'q', 'e']:
            ser.write(command.encode())
            print(f"Sent command: {command}")
            response = ser.readline().decode(errors='ignore').strip()
            print("Response:", response)
        else:
            print("Invalid command. Please enter a valid command.")

except KeyboardInterrupt:
    pass

# Close the serial port
ser.close()