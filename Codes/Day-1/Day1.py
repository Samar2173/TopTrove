# while True:
#     # Taking input from user
#     num_1 = int(input("Enter 1st number: "))
#     num_2 = int(input("Enter 2nd number: "))

#     # Splitting 2 digit number seperately
#     o1 = num_1//10 # 56 // 10 = 5
#     t1 = num_1%10   # 56 % 10 = 6

#     o2 = num_1//10
#     t2 = num_2%10

#     if(o1*t1 > o2*t2): print(f'Product of {num_1} is greater')
#     else: print(f'Product of {num_2} is greater')

#     check = input("Do you wan to contunue y/n: ")
#     if check == 'n': break

# while True:
#     # Taking input from user
#     num_1 = int(input("Enter 1st number: "))
#     num_2 = int(input("Enter 2nd number: "))

#     # Splitting 2 digit number seperately
#     o1 = num_1//10 # 56 // 10 = 5
#     t1 = num_1%10   # 56 % 10 = 6

#     o2 = num_1//10
#     t2 = num_2%10

#     if(o1*t1 > o2*t2): print(f'Product of {num_1} is greater')
#     else: print(f'Product of {num_2} is greater')

#     check = input("Do you wan to contunue y/n: ")
#     if check == 'y': continue
#     else:
#         check = input("Are you sure? y/n: ")
#         if check == 'y': break

while True:
    pass    
# Taking input from user
num_1 = int(input("Enter 1st number: "))
num_2 = int(input("Enter 2nd number: "))

# Splitting 2 digit number seperately
o1 = num_1//10 # 56 // 10 = 5
t1 = num_1%10   # 56 % 10 = 6

o2 = num_1//10
t2 = num_2%10

if(o1*t1 > o2*t2): print(f'Product of {num_1} is greater')
else: print(f'Product of {num_2} is greater')

check = input("Do you wan to contunue y/n: ")
if check == 'n': break