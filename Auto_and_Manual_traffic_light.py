import time
def trafficlight():
    direction=input("Enter the Direction: ")
    signal=input("Enter the signal : ")
    if(signal not in ("RED","YELLOW","GREEN")):
        print("Enter valid signal in capitals")
    else:
        value=light(signal)
    if(value==0):
        print(direction,"side=> STOP!")
    elif(value==1):
        print(direction,"side=> GET READY TO GO")
    else:
        print(direction,"side=> GO!")

def light(signal):
    if(signal=="RED"):
        return(0)
    elif(signal=="YELLOW"):
        return(1)
    else:
        return(2)

def automatic_trafficlight():
    print("RED Light => STOP")
    time.sleep(5)
    print("YELLOW Light => GET READY TO GO")
    time.sleep(5)
    print("GREEN Light => GO!")
    time.sleep(5)

mode=input("Select Mode Auto or Manual : ")
if mode=="Auto":
    automatic_trafficlight()

elif mode=="Manual":
    trafficlight()
    
    
