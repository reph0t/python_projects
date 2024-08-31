def ascend_sort(array):

    # loop to access each array element
    for i in range(len(array)):
        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[ j + 1]:

                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    print(f"Ascend Order: {array}")


def descend_sort(array):
    # loop to access each array element
    for i in range(len(array)):
        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            # change < to sort in descending order
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    print(f"Descend Order: {array}")

def main():
    user_input = input("Please enter a list a numbers separated by a space: ").split()
    numbers = [int(num) for num in user_input]

    ascend_sort(numbers)
    descend_sort(numbers)

if __name__ == "__main__":
    main()