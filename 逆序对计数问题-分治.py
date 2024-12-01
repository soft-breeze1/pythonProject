def merge_sort_and_count(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, left_count = merge_sort_and_count(arr[:mid])
    right, right_count = merge_sort_and_count(arr[mid:])
    merged, cross_count = merge_and_count(left, right)
    return merged, left_count + right_count + cross_count

def merge_and_count(left, right):
    result = []
    count = 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            count += len(left) - i
    result.extend(left[i:])
    result.extend(right[j:])
    return result, count
input_str = input()
input_list = [int(item) for item in input_str.split(',')]
sorted_list, inversion_count = merge_sort_and_count(input_list)
print(inversion_count)