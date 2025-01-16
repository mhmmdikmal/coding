import random
list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))

# prints a random item from the string
string = "prakerja paideia"
print(random.choice(string))
  
# prints a random item from the tuple
tuple1 = (1, 2, 3, 4, 5)
print(random.choice(tuple1))

# import the random module
import random
# declare a list
sample_list = [1, 2, 3, 4, 5]
  
print("Original list : ")
print(sample_list)
  
# first shuffle
random.shuffle(sample_list)
print("\nAfter the first shuffle : ")
print(sample_list)
  
# second shuffle
random.shuffle(sample_list)
print("\nAfter the second shuffle : ")
print(sample_list)
