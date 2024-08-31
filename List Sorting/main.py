def ascend_sort(array):
    n = len(array)

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

                already_sorted = False

        if already_sorted:
            break
    print(f"Ascending Order: {array}")

def descend_sort(array):
    n = len(array)

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

                already_sorted = False

        if already_sorted:
            break
    print(f"Descending Order: {array}")

def main():
    user_input = input("Please enter a list a numbers separated by a space: ").split()
    numbers = [int(num) for num in user_input]

    ascend_sort(numbers)
    descend_sort(numbers)

if __name__ == "__main__":
    main()
