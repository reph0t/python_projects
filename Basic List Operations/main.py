def total(numbers):
    print(f"Total: {sum(numbers)}")

def average(numbers):
    print(f"Average: {sum(numbers) / len(numbers)}")

def small_large(numbers):
    print(f"Smallest Number: {min(numbers)}")
    print(f"Largest Number: {max(numbers)}")

def main():
    user_input = input("Enter a list of numbers separated by spaces: ").split()
    numbers = [int(num) for num in user_input] # Convert each input to an integer

    new_list = []

    for i in numbers:
        if i not in new_list:
            new_list.append(i)

    print(new_list)

    total(new_list)
    average(new_list)
    small_large(new_list)

if __name__ == "__main__":
    main()
