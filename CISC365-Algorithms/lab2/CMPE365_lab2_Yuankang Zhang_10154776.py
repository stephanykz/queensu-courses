'''
Name: Yuankang Zhang
Student #: 10154776
NetID: 14yz28
'''

final_max_sum = 0
final_index = [0, 0]
#second_max = 0

def Sum(lst, start, mid, end):
    global final_max_sum
    global final_index
    global second_max
    global current_max_sum

    current_sum = 0
    left_sum = -9999
    for i in range(mid, start - 1, -1):
        current_sum = current_sum + lst[i]
        if (current_sum > left_sum):
            left_sum = current_sum
            final_index[0] = i

    current_sum = 0
    right_sum = -9999
    for i in range(mid + 1, end + 1):
        current_sum = current_sum + lst[i]
        if (current_sum > right_sum):
            right_sum = current_sum
            final_index[1] = i

    #second_max = final_max_sum
    current_max_sum = left_sum + right_sum
    if final_max_sum < current_max_sum:
        final_max_sum = current_max_sum

    return left_sum + right_sum


def Sub(list, start, end):
    if (start == end):
        return list[start]

    mid = (start + end) // 2

    return max(Sub(list, start, mid),
               Sub(list, mid + 1, end),
               Sum(list, start, mid, end))

# mss() for part 1
def mss1(list):

    if all(i <= 0 for i in list):
        print("Since all numbers in the list are negative, we assume the max segment sum is Zero.")

    else:
        Sub(list, 0, len(list) - 1)
        print("For list " + str(list) + ', the maximum segment sum is ' + str(final_max_sum) +
              ', and the elements of this segment are ' + str(list[final_index[0]:final_index[1]+1]))
        #for part 3
        #print("The second max was " + str(second_max))


# mss() and for part 2
def mss2(list):
    global final_max_sum
    global final_index

    if all(i <= 0 for i in list):
        print("Since all numbers in the list are negative, we assume the max segment sum is Zero.")
    else:
        Sub(list, 0, len(list) - 1)
        print("For list " + str(list) + ', the first maximum segment sum is ' + str(final_max_sum) +
              ', and the elements of this segment are ' + str(list[final_index[0]:final_index[1] + 1]))

        i = final_index[0]
        while i <= final_index[1]:
            list[i] = 0
            i = i + 1

        final_max_sum = 0
        final_index = [0,0]

        Sub(list, 0, len(list) - 1)
        print('The second maximum segment sum is ' + str(final_max_sum) +
              ', and the elements of this segment are ' + str(list[final_index[0]:final_index[1] + 1]))
        print(str(final_index))


def test(question_n):
    # test 1: blending pasitive numbers and negative numbers - a variation of list1 by switching the order
    list1 = [-7, 2, 4, 5, 3, -6, 1, 4]
    # test 2: the maximum segment is the entire list - a list with only positive number
    list2 = [1, 9, 2, 8, 3, 7, 4, 6, 5]
    # test 3: a list with only negative number - in this case, we assume the max sum is Zero
    list3 = [-1, -9, -2, -8, -3, -7, -4, -6, -5]

    if question_n == 1 :
        print ('\nCase 1:')
        mss1(list1)
        print ('\nCase 2:')
        mss1(list2)
        print ('\nCase 3:')
        mss1(list3)
    elif question_n == 2:
        print('\nCase 1:')
        mss2(list1)
        print('\nCase 2:')
        mss2(list2)
        print('\nCase 3:')
        mss2(list3)

test(1)

