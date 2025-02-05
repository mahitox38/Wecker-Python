from tkinter import *
import winsound
import datetime
import time
from threading import *

fenster = Tk()
fenster.geometry('400x200')


def Threading():
    t1 = Thread(target=alarm)
    t1.start()

def alarm():
    alarm_zeit_speichern = None
    while True:
        set_alarm_time = f'{int(hour.get()):02d}:{int(minute.get()):02d}:{int(second.get()):02d}'
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)
        if current_time == set_alarm_time:
           print('Aufwachen')
           winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
           alarm_zeit_speichern = datetime.datetime.now()

        if alarm_zeit_speichern:
            elapsed_time = (datetime.datetime.now() - alarm_zeit_speichern).total_seconds()
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            if elapsed_time > 60:
                print('Alarm stoppt jetzt.')
                winsound.PlaySound(None, winsound.SND_PURGE)
                break
Label(fenster, text='Alarm Generieren', font=("Helvetica 20 bold"), fg='Blue').pack(pady=10)
frame = Frame(fenster)
frame.pack(pady=20)

hour = StringVar(fenster)
hours = [x for x in range(24)]
hour.set(hours[0])
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(fenster)
minutes = [x for x in range(60)]
#('00', '01','02','03','04','05','06','07','08','09','10',
 #           '11', '12','13','14','15','16','17','18','19','20',
  #          '21','22','23','24','25', '26','27','28','29','30',
   #         '31','32','33','34','35','36','37','38','39','40',
    #        '41','42','43','44','45','46','47','48','49','50',
     #       '51','52','53','54','55','56','57','58','59')
minute.set(minutes[0])
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(fenster)
seconds = [x for x in range(60)]
#('00', '01','02','03','04','05','06','07','08','09','10',
 #           '11', '12','13','14','15','16','17','18','19','20',
  #          '21','22','23','24','25', '26','27','28','29','30',
   #         '31','32','33','34','35','36','37','38','39','40',
    #        '41','42','43','44','45','46','47','48','49','50',
     #       '51','52','53','54','55','56','57','58','59')
second.set(seconds[0])
secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(fenster, text='Jetzt Generieren', command=Threading).pack(pady=20)
fenster.mainloop()

