import time

minutes = int(input("Enter the mumber of minutes to focus: "))
second = minutes * 60

while second :
  mins, secs = divmod(second, 60)
  time = '{:02d}:{:02d}',format(mins, secs)
  print(timer,end="\r")
  time.sleep(1)
  secnod -= 1
  
  print("Time's up!")
  
