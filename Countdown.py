import time
import sys
from plyer import notification as nf

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
    nf.notify(
        title='Countdown was finished',
        message="Your burger is ready",
        timeout = 2 , 
        app_icon = "icon.ico"
       )

while True:
    try:
       input_time=int(input('time in sec? '))
       countdown(input_time)
    except:
        print('spmething went wrong')
        pass
    else:
        break
