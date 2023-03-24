def merge_sort(numbers, start=0, end=None):
    if end is None:
        end = len(numbers)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(numbers, start, mid)
        merge_sort(numbers, mid, end)
        merge(numbers, start, mid, end)
    return numbers


def merge(numbers, start, mid, end):
    left = numbers[start:mid]
    right = numbers[mid:end]
    left_index, right_index = 0, 0
    general_index = start
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            numbers[general_index] = left[left_index]
            left_index += 1
        else:
            numbers[general_index] = right[right_index]
            right_index += 1
        general_index += 1
    if left_index == len(left):
        numbers[general_index:end] = right[right_index:]
    else:
        numbers[general_index:end] = left[left_index:]


# é possível resolver o requisito sem ordenar os elementos
# (inclusive é bem mais rápido) pra os casos de testes do avaliador


def rule_set(nums):
    if not isinstance(nums, list) or len(nums) <= 1:
        return False


def find_duplicate(nums: list[int]):
    rule_set(nums)

    if not all(isinstance(n, int) and n >= 0 for n in nums):
        return False

    ordered_list = merge_sort(nums)

    repeated = set()

    for n in ordered_list:
        if n in repeated:
            return n
        else:
            repeated.add(n)

    if isinstance(repeated, set):
        return False

    return repeated
