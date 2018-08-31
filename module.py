from datetime import date
from datetime import datetime
t=datetime.now()
d=date.weekday(t)
day= ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
print(day[d])
#Answer-2 Play a video Using Webbrowser module
import webbrowser
webbrowser.open_new_tab('https://www.youtube.com/watch?v=RcGQ6N0NIss')
#Answer-3
import os
c=os.listdir(Ranveer)#name of files
i = 1
for f in c:
    os.rename(f, str(i)+'.jpg')
    i = i+1
