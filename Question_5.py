def dictionary_sort(str):
    n = len(str)
    
    for i in range(n - 1):
        min_idx = i
        
        for j in range(i + 1, n):
            if str[j].lower() < str[min_idx].lower():
                min_idx = j
        
        if min_idx != i:
            str[i], str[min_idx] = str[min_idx], str[i]


input_list = input("Enter a list of strings separated by spaces: ").split()
dictionary_sort(input_list)

print("Sorted list:", input_list)

