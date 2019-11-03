import serial

ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM3'
print(ser)
ser.open()
x = ser.read(1)
print("Respuesta Serial=" + str(x))
ser.close()
