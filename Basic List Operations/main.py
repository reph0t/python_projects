def total(numbers):    # Calculates the sum  of the list 
    print(f"Total: {sum(numbers)}")

def average(numbers):    # Calculates the average of the list 
    print(f"Average: {sum(numbers) / len(numbers)}")

def small_large(numbers):    # Prints the smallest and largest number in the list 
    print(f"Smallest Number: {min(numbers)}")
    print(f"Largest Number: {max(numbers)}")

def main():
    user_input = input("Enter a list of numbers separated by spaces: ").split()    # Asks the user for input 
    numbers = [int(num) for num in user_input] # Convert each input to an integer

    # a new list is initiliazed 
    new_list = []

    for i in numbers: # iterates in the old list
        if i not in new_list: # if the number is not in the new_list
            new_list.append(i)     # add the number in that list 

    print(new_list) 
    
    total(new_list) 
    average(new_list)
    small_large(new_list)

if __name__ == "__main__":
    main()
