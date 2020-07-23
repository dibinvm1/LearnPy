import webbrowser
import time

print ("This Program stared on " + time.ctime())
for n in range(3):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=KVLNz7rgRl8",2,True)