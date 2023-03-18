hours = int (input ("Enter Hours:"))
rate = int (input ("Enter Rate:"))
if hours <= 30:
    pay = str (hours*rate)
    print ("Pay:" + pay)
else:
    newHours = hours - 30
    newRate = rate * 2.50
    pay = str (30 * rate + newHours*newRate)
    print ("Pay:" + pay)