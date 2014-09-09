import time
import webbrowser
i = 0
print "this programme started on"+time.ctime()
while (i < 2):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=jU3P7qz3ZrM", new = 1)
    i = i+1
