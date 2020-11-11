import time #Allows for the outputs to be readable
import math 

pi = math.pi

def Lever(): #Using functions to allow for repeatability and future expansions
    Le = float(input('What is the longer length from the pivot point? '))
    Lr = float(input('What is the shorter length from the pivot point? '))
    N = float(input('How much effort do you wish to obtain [in Newtons]? '))
    M = Le/Lr
    time.sleep(1)
    print(f'The Ideal Mechanical Advantage (IMA) of your lever is: {str(M)}')
    print(f'You will need to put in {str(N/M)}N of effort')

def WaA():
    R = float(input('What is the radius of the wheel? '))
    r = float(input('What is the radius of the axle? '))
    M = R/r
    time.sleep(1)
    print(f'The Ideal Mechanical Advantage (IMA) Wheel and Axle system is: {str(M)}')

def Incline():
    L = float(input('What is the hypotenouse of the ramp? '))
    h = float(input('What is the height of the ramp? '))
    M = L/h
    time.sleep(1)
    print(f'The Ideal Mechanical Advantage (IMA) of your incline is: {str(M)}')

def Wedge():
    L = float(input('What is the length of the wedge? '))
    t = float(input('What is the height of the wedge? '))
    M = L/t
    time.sleep(1)
    print(f'The Ideal Mechanical Advantage (IMA) of your wedge is: {str(M)}')

def Screw():
    L = float(input('What is the length of the handle? '))
    P = float(input('What is the height of each thread? '))
    M = (2*pi)*L/P
    time.sleep(1)
    print(f'The Ideal Mechanical Advantage (IMA) of your screw is: {str(M)}')

def Pulley():
    N = int(input('How many rope-segments are there? '))
    time.sleep(1)
    M = N
    print(f'The Ideal Mechanical Advantage (IMA) of your pulley system is: {str(M)}')

def inputs(): 
    print("Hello and Welcome to the mechanical advantage calculator!")
    while True:
        global Mch
        Mch=input("Which machine do you wish to calculate the mechanical advantage of? ")
        c=("Lever", "Wheel and Axel", "Pulley", "Incline", "Wedge", "Screw") #These lists are to ensure that a valid input has been made
        if Mch in c:
            break
        if Mch not in c:
            print("Please enter a valid Mechanism (Lever, Wheel and Axel, Pulley, Incline, Wedge or Screw)") #Printed if the input is incorrect
    if Mch == "Lever":
         Lever()
    if Mch == "Wheel and Axel":
         WaA()
    if Mch == "Pulley":
         Pulley()
    if Mch == "Incline":
         Incline()
    if Mch == "Wedge":
         Wedge()
    if Mch == "Screw":
         Screw()
    
inputs()
