import sys
import time


def swap_positions(list1, pos1, pos2):
    list1[pos1], list1[pos2] = list1[pos2], list1[pos1]
    return list1


def str_to_list(new_str):
    my_arr = []
    for char in new_str:
        my_arr.append(ord(char))
    return my_arr


def list_to_str(lst):
    empty_str = ''
    for nums in lst:
        empty_str += chr(nums)
    return empty_str


def next_permutation(word):
    arr = str_to_list(word)
    n = len(arr)
    i = 0
    j = 0

    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            break

    if i < 0:
        arr.reverse()

    else:
        for j in range(n - 1, i, -1):
            if arr[j] > arr[i]:
                break

        swap_positions(arr, i, j)

        str_t, end = i + 1, len(arr)

        arr[str_t:end] = arr[str_t:end][::-1]
    next_one = list_to_str(arr)
    return next_one


if __name__ == "__main__":
    test_cases = int(input("enter the number of cases..... "))
    if 1 > test_cases or test_cases > pow(10, 5):
        print("The number of cases must be in range 1 ≤ T ≤ 10^5")
        time.sleep(5)
        sys.exit(0)

    for num in range(test_cases):
        new_word = input("enter the word..... ")
        if 1 > len(new_word) or len(new_word) > 100:
            print("the length of word mus be less the  100 and more then 0")
            time.sleep(5)
            sys.exit(0)
        for letter in new_word:
            if ord(letter) < ord('a') or ord(letter) > ord('z'):
                print("string must contain only letters in range [a to z]")
                time.sleep(5)
                sys.exit(0)
        a = next_permutation(new_word)
        print(a)