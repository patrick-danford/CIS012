# CIS012 Assignment 04_1
# Patrick Danford, 9/28/2019


# Function that takes hours and rate as input, returns calculated pay
def CalPay(hrs, rte):
    ot_rte = rte * 1.5
    dt_rte = rte * 2
    if hrs <= 40:
        pay = hrs * rte
    elif hrs <= 60:
        base_pay = 40 * rte
        ot_hours = hrs - 40
        pay = base_pay + (ot_hours * ot_rte)
    elif hrs > 60:
        base_pay = 40 * rte
        ot_pay = 20 * ot_rte
        dt_hours = hrs - 60
        pay = base_pay + ot_pay + (dt_hours * dt_rte)
    return print("Your total pay amount is: ", pay)


# User inputs required information
hours = input("Please enter number of hours worked for this week: ")
rate = input("What is hourly rate? ")
try:
    # Convert input to float if valid entry
    fhr = float(hours)
    frt = float(rate)
    # Confirm entry is positive numbers, prompt user to try again if not
    if fhr > -1 and frt > -1:
        # Invoke def CalPay
        CalPay(fhr, frt)
    else:
        print("Invalid entry. Try again.")
except:
    print("Invalid entry. Try again.")


