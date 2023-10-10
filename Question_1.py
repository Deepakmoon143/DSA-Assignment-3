def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

input_list = input("Enter a sorted list of numbers separated by spaces: ").split()
target = int(input("Enter the number you want to search for: "))
input_list = [int(item) for item in input_list]
    
result = binary_search(input_list, target)

if result != -1:
    print(f"Found {target} at index {result}.")
else:
    print(f"{target} not found in the list.")
