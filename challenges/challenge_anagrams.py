
def counting_sort(string):
    char_count = [0] * 256
    for char in string:
        char_count[ord(char)] += 1

    for i in range(1, 256):
        char_count[i] += char_count[i-1]

    result = [None] * len(string)
    for char in string:
        result[char_count[ord(char)] - 1] = char
        char_count[ord(char)] -= 1

    return ''.join(result)


def is_anagram(first_string: str, second_string: str):
    if not first_string and not second_string:
        return (first_string, second_string, False)

    first_string = first_string.lower().replace(" ", "")
    second_string = second_string.lower().replace(" ", "")

    str1_sorted = counting_sort(first_string)
    str2_sorted = counting_sort(second_string)

    if str1_sorted == str2_sorted:
        return (str1_sorted, str2_sorted, True)
    else:
        return (str1_sorted, str2_sorted, False)
