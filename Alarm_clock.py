from playsound import playsound 
import time 


CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def alarm(seconds):
    time_elapsed = 0
    

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60 
        
        
        print(f"{CLEAR_AND_RETURN}{minutes_left:02d}:{seconds_left:02d} ")
        #Change the Path in playsound or just put the name of the file EX: playsound("song.mp3")
    playsound("C:\\Users\\21623\\Documents\\python\\test\\Alarm\\song.mp3")


while True:
    x = input("set your alarm \n")
    if x.isdigit():
        if int(x) > 0:
            s = int(x)
            break
        else:
            print("time must be greater than 0 .")
    else:
        print("please enter a valid number .")


alarm(s)