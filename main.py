import serial
import time

print("Serial coms connecting...")
ser = serial.Serial('com4', 9600, timeout=10) # create Serial Object, baud = 9600, read times out after 10s
time.sleep(3)  # delay 3 seconds to allow serial com to get established
print("Serial com connected")

while (True):
    while ser.in_waiting:
        print(ser.readline())

    #bytes = str(input())
    input_num = str(input())
    msg=bytes(input_num, 'UTF-8')
    print(msg)
    ser.write(msg)

    time.sleep(1)