def mathWork():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    total_sum = num1 + num2
    print(f"\nResult of {num1} + {num2} is {total_sum}")
    return total_sum

mathWork()

# Simple script I was easily able to put together, inclund f - function statements
# and the requested operation of providing the product of addition for 2 #'s

# list_of_numbers = [2, 4, 3, 8, 2, 55, 1, 33, 41]
# total_sum = 0
# for digit in list_of_numbers:
#     total_sum += digit    <<<-------
#     print(total_sum)

def sum_list(): 
    list_of_numbers = [2, 4, 3, 8, 2, 55, 1, 33, 41] 
    total = sum(list_of_numbers) 
    print(f"\n{total} is the sum of all list elements")
    print() 
    return(sum_list)
sum_list()