seconds = int(input("Enter the elapsed time in seconds: "))
print("The elapsed time in seconds =", seconds)

seconds = seconds % (24 * 3600)
hour = seconds / 3600
seconds = seconds % 3600
minutes = seconds / 60
seconds = seconds % 60

print("The equivalent time in hours:minutes:seconds =", (int(hour)), ":", (int(minutes)), ":", (int(seconds)))
