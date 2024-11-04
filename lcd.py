import time
from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO

trig=23
echo=24

# Define LCD setup
lcd = CharLCD(
    numbering_mode=GPIO.BCM,
    cols=16,
    rows=2,
    pin_rs=26,
    pin_e=19,
    pins_data=[13,6,5,11]
)

GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

try:
	while True:
		GPIO.output(trig,True)
		time.sleep(0.00001)
		GPIO.output(trig,False)
		
		while GPIO.input(echo)==0:
			start_time=time.time()
		while GPIO.input(echo)==1:
			end_time=time.time()
		duration = end_time -start_time
		distance = (duration*34300)/2
		
		
		lcd.write_string(f"Dist : {distance:.2f} cm")	
		
		print(distance)	
		time.sleep(1)
		lcd.clear()

except KeyboardInterrupt:
	print('stopped')
	lcd.clear()
	GPIO.cleanup()
