import pygame
import serial
import time
import math

#
pygame.init()
pygame.joystick.init()
js = pygame.joystick.Joystick(0)
js.init()


print(js.get_numaxes())
print(js.get_numbuttons())
print(js.get_name())
print(js.get_init())

ser = serial.Serial('/dev/ttyUSB1',baudrate=9600) #opens the serial port
print(ser.name)#prints out the serial name
degree = 3 

while(True):
	pygame.event.get()
	send = js.get_button(0)
	time.sleep(.1)
	s=""
	curr_instruction = ""
	
	axis1 = int(math.floor(js.get_axis(0) + .5))
	if axis1 == 0 :
		axis1 = int(math.floor(js.get_axis(2) + .5))
	axis2 = int(math.floor(js.get_axis(1) + .5))
	axis3 = js.get_hat(0)[1]
	
	if( js.get_button(6) == 1 ) :
		degree = 4 
	if( js.get_button(7) == 1 ):  
		degree = 1
	if( js.get_button(8) == 1 ) :
		degree = 5 
	if( js.get_button(9) == 1 ):  
		degree = 2
	if( js.get_button(10) == 1 ) :
		degree = 6 
	if( js.get_button(11) == 1 ):  
		degree = 3

	print degree 
	
	if(axis1 == -1):
		curr_instruction += "left    "
	elif(axis1 == 1):
		curr_instruction += "right   "
	else:
		curr_instruction += "------- "
	if(axis2 == -1):
		curr_instruction += "forward "
	elif(axis2 == 1):
		curr_instruction += "back    "
	else:
		curr_instruction += "------- " 
	if(axis3 == -1):
		curr_instruction += "down    "
	elif(axis3 == 1):
		curr_instruction += "up      "
	else:
		curr_instruction += "------- "
	s+= str(degree) + ' ' + str(axis1) + ' ' + str(axis2) +" "+ str(axis3)+'\n'  
	#s = str(js.get_axis(0))+" "+str(js.get_axis(1))+" "+str(js.get_hat(0)[1])
	print(curr_instruction)
	if(send == 1) :
		ser.write(s)
		print "\nSent\n"

