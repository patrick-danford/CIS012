seconds = int(input("Please enter how much time has elapsed in seconds: "))

seconds = seconds % (24 * 3600)
hour = seconds / 3600
seconds = seconds % 3600
minutes = seconds / 60
seconds = seconds % 60


print("That is", int(hour), "hours", int(minutes), "minutes and", seconds, "seconds")
