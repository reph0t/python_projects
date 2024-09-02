def alphabet_order(array):
    n = len(array)

    for i in range(n):
        assorted_list = True

        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                assorted_list = False
                print(f"{i} Iteration: {array}")


        if assorted_list:
            break

    print(f"Sorted alphabetically: {array}")


def main():

    user_input = input("Please enter a list of words separated by a space: ").split()
    alphabet_order(user_input)

if __name__ == "__main__":
    main()
