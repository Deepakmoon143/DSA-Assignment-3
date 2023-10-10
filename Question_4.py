def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


input_list = input("Enter a list of numbers separated by spaces: ").split()
input_list = [int(item) for item in input_list]

insertion_sort(input_list)

print("Sorted list:", input_list)

