# masukan kata kunci untuk mengakses dict
Dict = {1: 'Code', 2: 'its', 3: 'Real'} 
    
# contoh 1
print("\nAccessing a element using key:") 
print(Dict[1]) 
  
# accessing a element using get() 
# method 
print("\nAccessing a element using get:") 
print(Dict.get(3)) 


String1 = "Programmer"
print("\nInitial String: ")
print(String1)
 
# Printing First character
print("\nFirst character of String is: ")
print(String1[0])
 
# Printing Last character
print("\nLast character of String is: ")
print(String1[-1])


String1 = "The Beauty of Code"
print("\nInitial String: ")
print(String1)

String1 = "The Beauty of Code"
print("\nInitial String: ")
print(String1)
 
# use del for deleting obj (del String1)
print("\nDeleting entire String: ")
def string():
    del String1
    print(String1)

String1 = ("\nThe Beauty of Code")
print(String1[5:11])#menghitung kosa kata yang diinginkan

print(String1)

#Dict List
Dict = dict([(1, 'Coding'), (2, 'Python')]) 
print("\nDictionary : ") 
print(Dict) 

Dict = dict({1: 'Beauty', 2: 'Of', 3:'Code'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict) 