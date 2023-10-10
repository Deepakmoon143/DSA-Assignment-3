def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    merge = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merge.append(left[left_index])
            left_index += 1
        else:
            merge.append(right[right_index])
            right_index += 1

    merge.extend(left[left_index:])
    merge.extend(right[right_index:])

    return merge


input_list = input("Enter a list of numbers separated by spaces: ").split()
input_list = [int(item) for item in input_list]

sorted_list = merge_sort(input_list)

print("Sorted list:", sorted_list)

