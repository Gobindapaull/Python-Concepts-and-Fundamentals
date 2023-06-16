from datetime import datetime

now = datetime.now()
time_now = now.strftime("date: %m-%d-%Y (%H-%M-%S)")
print(time_now)
