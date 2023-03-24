
def merge_sort(numbers, start=0, end=None):
    if end is None:
        end = len(numbers)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(numbers, start, mid)
        merge_sort(numbers, mid, end)
        merge(numbers, start, mid, end)

    return ''.join(numbers)


def merge(numbers, start, mid, end):
    left = numbers[start:mid]
    right = numbers[mid:end]
    left_len = len(left)
    right_len = len(right)

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= left_len:
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= right_len:
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            numbers[general_index] = right[right_index]
            right_index = right_index + 1



def is_anagram(first_string: str, second_string: str):
    if not first_string and not second_string:
        return (first_string, second_string, False)

    first_string = first_string.lower()
    second_string = second_string.lower()

    str1_sorted = merge_sort(list(first_string))
    str2_sorted = merge_sort(list(second_string))

    if str1_sorted == str2_sorted:
        return (str1_sorted, str2_sorted, True)
    else:
        return (str1_sorted, str2_sorted, False)


    

print(is_anagram("Silent", "Listen"))


# print(len(''.join("Batata")))