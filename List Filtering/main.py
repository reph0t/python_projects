def even_list(array):
    even_list = []      # a new list 

    for i in array:

        # if array[i] % 2 == 0:  
            
    # The line above was a mistake I made because I thought you should include the array in order to check if the value 
    # is even. If you were to run it would give you index error because you are comparing the indices 
    # not the value of the list.
        
        if i % 2 == 0: # this the correct way to check if the value is even    
            
            even_list.append(i)       

    print(f"Even Numbers: {even_list}")

def sorted(array):  #Using the bubble sort algorithm 
    n = len(array)  # grabs the size of the array

    for i in range(n): 
        already_sorted = True

        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

                already_sorted = False

        if already_sorted:
            break

def user():
    user_input = input("Enter a list of numbers separated by a space: ").split()
    numbers = [int(num) for num in user_input]

    sorted(numbers) # first organize the list 
    even_list(numbers) # print the even numbers 


if __name__ == "__main__":
    user()
