import serial

serial_port='/dev/ttyUSB0'
baud_rate=9600
data_bits=8
parity=serial.PARITY_NONE
stop_bits=1
flow_control=False

def serial_connection(port,baud,data,parity,stop,flow):
    ser=serial.Serial(
            port=port,
            baudrate=baud,
            bytesize=data,
            parity=parity,
            stopbits=stop,
            xonxoff=flow,
            rtscts=flow)
    return ser

ser=serial_connection(serial_port,baud_rate,data_bits,parity,stop_bits,flow_control)


