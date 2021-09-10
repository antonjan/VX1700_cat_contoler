import serial
import struct

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=4800,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.EIGHTBITS
)

print(ser.isOpen())
#thestring = "7E FF 03 00 01 00 02 0A 01 C8 04 D0 01 02 80 00 00 00 00 8E E7 7E"
thestring = "\x7E\xFF\x03\x00\x0A\"
data = struct.pack(hex(thestring))
#data = struct.pack(hex, 0x7E, 0xFF, 0x03, 0x00, 0x01, 0x00, 0x02, 0x0A, 0x01, 0xC8,      0x04, 0xD0, 0x01, 0x02, 0x80, 0x00, 0x00, 0x00, 0x00, 0x8E, 0xE7, 0x7E)

ser.write(data)
s = ser.read(1)
print(s)
ser.close()
