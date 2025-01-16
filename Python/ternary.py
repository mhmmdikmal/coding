#[on_true] if [expression] else [on_false] 
# Tenary dapat ditulis sebagai if else bersarang (nested if's)
# Program to demonstrate conditional operator
a, b = 10, 20
 
# Copy value of a in min if a < b else copy b
min = a if a > b else b
print(min)