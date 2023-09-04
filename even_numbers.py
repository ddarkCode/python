
sum_of_all_even_numbers = 0

for even in range(1, 101):
    if even % 2 == 0:
        sum_of_all_even_numbers += even
print(sum_of_all_even_numbers)