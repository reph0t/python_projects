def pos_neg(array):
    pos_list = []    # Postive List
    neg_list = []    # Negative List
    non_neg = []    # Nonnegative List

    for i in array:
        if i < 0:       # If the value less than 0 it is a negative number
            neg_list.append(i)

        elif i > 0:     # Checks the values if its greater than 0
            pos_list.append(i)

        else:
            non_neg.append(i)


    print(f"Positive Numbers: {pos_list}")
    print(f"Negative Numbers: {neg_list}")
    print(f"Non Negative: {non_neg}")

def list_sort(array):
    n = len(array)

    for i in range(n):
        already_sorted = True

        for j in range(n - i -1):
            if array[j] > array[j + 1]:
             array[j], array[j +1] = array[j + 1], array[j]

            already_sorted = False

        if already_sorted:
            break



def user():
    user_input = input("Enter a list numbers separated by a space: ").split()
    numbers = [int(num) for num in user_input]

    list_sort(numbers)
    pos_neg(numbers)

if __name__ == "__main__":
    user()
