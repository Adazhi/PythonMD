
def compute_salary(hours, rate):
    return (hours * rate)

hours_worked =55
overtime_hours = 5

if hours_worked > 40 :
    overtime_hours = hours_worked - 40
    regular_hours = 40
else : regular_hours = hours_worked

total_salary = compute_salary (regular_hours, 10) + compute_salary (overtime_hours, 21.5)
print ('Total salary is ${:,.2f}'. format (total_salary))