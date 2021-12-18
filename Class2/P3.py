time = int(input("Enter time in seconds: "))
hour = int(time / 3600)
time = time%3600
minutes = int(time / 60)
time = time%60
seconds = int(time)
print(hour,"Hours", minutes,"Minutes", seconds,"Seconds")