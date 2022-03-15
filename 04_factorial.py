# n = 3
# product = 1
# for i in range(n):
#     product = product * (i+1)
# print(product)    

# upar vale ke jaisa hi hum ab karege function me.
#_iter ka matlab iterative finction hota hai.
# def factorial_iter(n):
#     product = 1
#     for i in range(n):
#         product = product * (i+1)
#     return product

# print(factorial_iter(5))



def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    else:    
        return n * factorial_recursive(n-1)

p = factorial_recursive(5)
print(p)