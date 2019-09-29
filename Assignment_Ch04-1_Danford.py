# CIS012 Assignment 04_1
# Patrick Danford, 9/28/2019


# Function that takes hours and rate as input, returns calculated pay
def CalPay(hrs, rate):
    ot_rate = rate * 1.5
    dt_rate = rate * 2
    if hrs <= 40:
        pay = hrs * rate
    elif hrs <= 60:
        base_pay = 40 * rate
        ot_hours = hrs - 40
        pay = base_pay + (ot_hours * ot_rate)
    elif hrs > 60:
        base_pay = 40 * rate
        ot_pay = 20 * ot_rate
        dt_hours = hrs - 60
        pay = base_pay + ot_pay + (dt_hours * dt_rate)
    return print("Your total pay amount is: ", pay)


# User inputs required information
hr = input("Please enter number of hours worked for this week: ")
rt = input("What is hourly rate? ")

# Convert input string to float if numerals.  If other, indicate input is invalid
try:
    fhr = float(hr)
    frt = float(rt)
except:
    print("Invalid entry. Try again.")

# Invoke def CalPay
CalPay(fhr, frt)
