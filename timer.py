import time

seconds=input('enter time in number of seconds')
def countDown(seconds):
    while seconds>0:
        mins=int(seconds/60)
        secs=int(seconds%60)
        timer=f'{mins}:{secs}'
        print(timer)
        seconds=seconds-1


countDown(int(seconds))