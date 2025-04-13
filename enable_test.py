import serial
import time

ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=2)


#global serial object to be used in all functions
ser=None

def sleep():
    time.sleep(5)

def serial_connector():
    global ser
    ser = serial.Serial('dev/ttyUSB0', baudrate=9600, timeout=2)

def enable_mode():
    ser.write(b'enable\r\n')

def command_outputs():
    response = ser.read(100)
    print(f"Response after command: {response.decode(errors='ignore')}")

def close_connection():
    ser.close()

if __name__ == "__main__":
    serial_connector()
    sleep()
    enable_mode()
    sleep()
    command_outputs()
    close_connection()
