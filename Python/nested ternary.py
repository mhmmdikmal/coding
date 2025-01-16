# Python program to demonstrate nested ternary operator
a, b = 10, 20
 
if a != b:
    if a > b:
        print("a is greater than b\n")
    else:
        print("b is greater than a\n")
else:
    print("a same as b\n")

a=5
b=7 
# [statement_on_True] if [condition] else [statement_on_false]
print(a,"is greater") if (a<b) else print(b,"is Greater")