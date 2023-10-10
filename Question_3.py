def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array.pop()  
    left = []
    right = []

    for i in array:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)


input_list = input("Enter a list of numbers separated by spaces: ").split()
input_list = [int(item) for item in input_list]

sorted_list = quick_sort(input_list)

print("Sorted list:", sorted_list)

