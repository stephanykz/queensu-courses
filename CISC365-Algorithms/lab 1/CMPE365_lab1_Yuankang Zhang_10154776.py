import matplotlib.pyplot as plt

checked_value = []
iteration_counts_set = []
sum_iteration_counts = []

# collatz program
def collatz_loop(n):
    nums = list(range(1, n+1))
    sum = 0
    for num in nums:
        num_looping = num
        num_iteration_count = 0
        while num_looping != 1:
            if num_looping in checked_value:
                #num_iteration_count += iteration_counts_set[checked_value.index(num_looping)]
                break
            if (num_looping % 2):
                num_looping = (3 * num_looping + 1)//2
                num_iteration_count += 2
                '''
                num_looping = 3 * num_looping + 1
                num_iteration_count += 1
                '''
            else:
                num_looping = num_looping//2
                num_iteration_count += 1
        checked_value.append(num)
        iteration_counts_set.append(num_iteration_count)
    #summation
    sum = 0
    for i in iteration_counts_set:
        sum = sum + i
    print(checked_value)
    print(iteration_counts_set)
    print("Sum of Iteration= ", str(sum))
    print("The highest times of iteration happen for ",checked_value[iteration_counts_set.index(max(iteration_counts_set))],", with iteration of", max(iteration_counts_set))

collatz_loop(1000)
plt.scatter(checked_value, iteration_counts_set)
plt.ylabel('Total number of iterations of the Collatz loop')
plt.xlabel('n')
plt.show()
