import webbrowser
import time

total_break = 3
break_count = 0

print("this program started on "+time.ctime())
while (break_count<total_break):
    time.sleep(2*60*60)
    webbrowser.open("http://www.google.com")
    break_count = break_count + 1
