import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)
#pins : A,B,C switches oif demux

char= {'a': (1,1), 'b' : (1,2), 'c' : (1,3), 'd' : (1,4), 'e' : (1,5),
        'f' : (2,1), 'g' : (2,2), 'h' : (2,3), 'i' : (2,4), 'j' : (2,5),
       'l' : (3,1), 'm' : (3,2), 'n' : (3,3), 'o' : (3,4), 'p' : (3,5),
       'q' : (4,1), 'r' : (4,2), 's' : (4,3), 't' : (4,4), 'u' : (4,5),
       'v' : (5,1), 'w' : (5,2), 'x' : (5,3), 'y' : (5,4), 'z' : (5,5)}

string = 'helloworld'
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW) 
i = 0
while i < len(string):
    temp = string[i]
    if temp == 'k':
    	count = 3
    else:
        count = char[string[i]][0]

    setting = count
    while(count > 0):
        if setting == 1:
            GPIO.output(13, GPIO.HIGH)
            sleep(0.5)
        elif setting == 2:
            GPIO.output(12, GPIO.HIGH)
            sleep(0.5)
        elif setting == 3:
            GPIO.output(12, GPIO.HIGH)
            GPIO.output(13, GPIO.HIGH) #check working
            sleep(0.5)
        elif setting == 4:
            GPIO.output(11, GPIO.HIGH)
            sleep(0.5)
        elif setting == 5:
            GPIO.output(11, GPIO.HIGH)
            GPIO.output(13, GPIO.HIGH) #?
            sleep(0.5)
        else:
            GPIO.output(11, GPIO.HIGH)
            GPIO.output(12, GPIO.HIGH)
            sleep(0.5)
           
        print(char[string[i]][1])
        count = count - 1
        GPIO.output(11, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        sleep(0.5)
    sleep(2)
    i = i + 1

print('end')
