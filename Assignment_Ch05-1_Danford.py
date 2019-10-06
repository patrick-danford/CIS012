# CIS012 Assignment 05_1
# Patrick Danford, 10/06/2019

# Function that takes hours and rate as input, returns calculated pay
def CalPay(hrs, rte):
    ot_rte = rte * 1.5
    dt_rte = rte * 2
    if hrs <= 40:
        pay = hrs * rte
    elif hrs <= 60:
        base_pay = 40 * rte
        ot_hrs = hrs - 40
        pay = base_pay + (ot_hrs * ot_rte)
    elif hrs > 60:
        base_pay = 40 * rte
        ot_pay = 20 * ot_rte
        dt_hrs = hrs - 60
        pay = base_pay + ot_pay + (dt_hrs * dt_rte)
    return print("Your total pay amount is: ", pay)


# Loop that prompts user for required information
while True:
    hours = input("Please enter number of hours worked for this week: ")
    rate = input("What is hourly rate? ")
    try:
        # Convert input to float if valid entry
        fhr = float(hours)
        frt = float(rate)
        # Confirm entry is positive numbers
        if fhr > -1 and frt > -1:
            # Invoke def CalPay
            CalPay(fhr, frt)
            # Prompt user to go again
            again = input('Do you want another pay calculation? (y or n): ')
            if again == 'y':
                continue
            else:
                print('Goodbye!')
                break
        # Inform user of invalid entry, restart loop
        else:
            print("Invalid entry. Try again.")
            continue
    # Inform user of invalid entry, restart loop
    except:
        print("Invalid entry. Try again.")
        continue
