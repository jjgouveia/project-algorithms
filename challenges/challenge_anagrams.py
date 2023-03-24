
def counting_sort(word: str):
    count = {}

    for character in word:
        count[character] = count.get(character, 0) + 1

    result = ''
    for character in 'abcdefghijklmnopqrstuvwxyz':
        result += character * count.get(character, 0)

    return result


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
