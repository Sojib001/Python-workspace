import time
res = int(time.strftime('%H'))
if(res >= 18):
    print("Good evening, sir!")
elif(res >= 12):
    print("Good Noon, sir!")
else:
    print("Good Morning, sir!")
