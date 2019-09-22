# User inputs required information
hours = input("Please enter number of hours worked for this week: ")
rate = input("What is hourly rate? ")

# Convert input string to float if numerals.  If other, quit
try:
    fh = float(hours)
    fr = float(rate)
except:
    print("Invalid entry. Try again.")
    quit()


# Calculate overtime and double-time rates
ot_rate = fr * 1.5
#print("Overtime rate is:", ot_rate)
dt_rate = fr * 2
#print("Doubletime rate is:", dt_rate)

# Calculate pay based on hours input, display total
if fh <= 40:
    base_pay = fh * fr
    print("Your pay amount is: ", base_pay)
elif fh <= 60:
    base_pay = 40 * fr
    ot_hours = fh - 40
    #print("OT hours: ", ot_hours)
    pay = base_pay + (ot_hours * ot_rate)
    print("Your pay amount is: ", pay)
elif fh > 60:
    base_pay = 40 * fr
    ot_pay = 20 * ot_rate
    dt_hours = fh - 60
    #print("Base pay is: ", base_pay)
    #print("OT hours: 20, OT pay: ", ot_pay)
    #print("DT hours: ", dt_hours)
    pay = base_pay + ot_pay + (dt_hours * dt_rate)
    print("Your total pay amount is: ", pay)
