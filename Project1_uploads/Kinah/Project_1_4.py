#Problem 4
import numpy as np

for i in range(1, 15, 2):
    numbers = [x if not x % i == 0 else 0 for x in range(101)]
    
def q5_func(i, numbers):
    print(str(i))
    mean_numbers = sum(numbers) / len(numbers)
    odd_numbers = sorted(numbers)
    median_numbers = (len(odd_numbers)) / 2
    odd_median = odd_numbers[int(median_numbers - 0.5)]
    print('Mean' + str(mean_numbers))
    print('Median' + str(odd_median))

q5_func(i, numbers)

print(np.mean(numbers))
print(np.median(numbers))
