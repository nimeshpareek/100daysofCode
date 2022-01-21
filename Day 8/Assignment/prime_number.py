# # Write your code below this line 👇
# def prime_checker(num):
#     if num == 2:
#         print("It's a prime number.")
#     if num == 0 or num == 1:
#         print("It's is not a prime number.")
#     for i in range(2, num):
#         if num % i == 0:  #at 87 it was failing don't know why
#             print("It's not a prime number.")
#             break
#         else:
#             print("It's a prime number.")
#             break
#
#
# # Write your code above this line 👆
# # Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(num = n)

# Write your code below this line 👇

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number = n)





