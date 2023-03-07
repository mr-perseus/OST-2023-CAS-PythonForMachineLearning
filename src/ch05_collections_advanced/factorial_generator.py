def fac_generator(n=0):
    iteration = 1
    result = 1
    while iteration <= n:
        yield result
        iteration += 1
        result *= iteration


numbers = fac_generator(5)
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))

for i in fac_generator(5):
    print(i)


#############################

def square(nums):
    for num in nums:
        yield num ** 2


for i in square(fac_generator(5)):
    print(i)