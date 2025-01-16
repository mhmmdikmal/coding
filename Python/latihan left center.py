# String alignment
String1 = "|{:<10}|{:^10}|{:>10}|".format('Pra', 'Kerja', 'Paideia')
print("\nLeft, center and right alignment with Formatting: ")
print(String1)

# To demonstrate aligning of spaces
String1 = "\n{0:^5} was founded in {1:>2}!".format("Paideia", 2021)
print(String1)