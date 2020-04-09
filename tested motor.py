import os     
import time   
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) 
import pigpio #importing GPIO library

ESC=4  #Connect the ESC in this GPIO pin 

pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC, 0) 

max_value = 2000 
min_value = 700  
print ("For first time launch, select calibrate")
print ("Type the exact word for the function you want")
print ("calibrate OR manual OR control OR arm OR stop")

def manual_drive(): 
    print ("You have selected manual option so give a value between 0 and you max value")    
    while True:
        inp = input()
        if inp == "stop":
            stop()
            break
        elif inp == "control":
            control()
            break
        elif inp == "arm":
            arm()
            break   
        else:
            pi.set_servo_pulsewidth(ESC,inp)
def calibrate():   
    pi.set_servo_pulsewidth(ESC, 0)
    print("Disconnect the battery and press Enter")
    inp = input()
    if inp == '':
        pi.set_servo_pulsewidth(ESC, max_value)
        print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
        inp = input()
        if inp == '':            
            pi.set_servo_pulsewidth(ESC, min_value)
            print ("Wierd eh! Special tone")
            time.sleep(7)
            print ("Wait for it ....")
            time.sleep (5)
            print ("Im working on it, DONT WORRY JUST WAIT.....")
            pi.set_servo_pulsewidth(ESC, 0)
            time.sleep(2)
            print ("Arming ESC now...")
            pi.set_servo_pulsewidth(ESC, min_value)
            time.sleep(1)
            print ("See.... uhhhhh")
            control() 
            
def control(): 
    print ("I'm Starting the motor, I hope its calibrated and armed, if not restart by giving 'x'")
    time.sleep(1)
    speed = 1500   
    print ("Controls - a to decrease speed & d to increase speed OR q to decrease a lot of speed & e to increase a lot of speed")
    while True:
        pi.set_servo_pulsewidth(ESC, speed)
        inp = input()
        
        if inp == "q":
            speed -= 100    # decrementing the speed like hell
            print ("speed = %d") % speed
        elif inp == "e":    
            speed += 100    # incrementing the speed like hell
            print ("speed = %d") % speed
        elif inp == "d":
            speed += 10     # incrementing the speed 
            print ("speed = %d") % speed
        elif inp == "a":
            speed -= 10     # decrementing the speed
            print ("speed = %d") % speed
        elif inp == "stop":
            stop()          #going for the stop function
            break
        elif inp == "manual":
            manual_drive()
            break
        elif inp == "arm":
            arm()
            break   
        else:
            print ("WHAT DID I SAID!! Press a,q,d or e")
            
def arm(): #The arming procedure of an ESC 
    print ("Connect the battery and press Enter")
    inp = input()    
    if inp == '':
        pi.set_servo_pulsewidth(ESC, 0)
        time.sleep(1)
        pi.set_servo_pulsewidth(ESC, max_value)
        time.sleep(1)
        pi.set_servo_pulsewidth(ESC, min_value)
        time.sleep(1)
        control() 
        
def stop(): 
    pi.set_servo_pulsewidth(ESC, 0)
    pi.stop()

inp = input()
if inp == "manual":
    manual_drive()
elif inp == "calibrate":
    calibrate()
elif inp == "arm":
    arm()
elif inp == "control":
    control()
elif inp == "stop":
    stop()
else :
    print ("Stop")
