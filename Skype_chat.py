import Skype4Py
from playsound import playsound
import time
import psutil

def play_sound():
    playsound('alarmclock.mp3')
    playsound('beepclocka.mp3')
def Powercheck():
    battery = psutil.sensors_battery()
    print battery
    if battery.percent < 15:
        print "Battary percentage low"
        play_sound()


def func_check():
    skype = Skype4Py.Skype()
    skype.Attach()

    user_status = skype.CurrentUserStatus  # returns a string
    missed_messages = skype.MissedMessages  # object type=message collection
    missed_calls = skype.MissedCalls  # object type=call collection

    print 'user_status:', user_status
    if user_status != 'ONLINE':
        #playsound('beep-01a.mp3')
        pass

    for list in missed_messages:
        print 'missed_messages:', list
        play_sound()
    for list in missed_calls:
        print 'missed_calls:', list
        play_sound()

# Play sound

if __name__ == '__main__':
    while True:
        func_check()
        Powercheck()
        time.sleep(10)
