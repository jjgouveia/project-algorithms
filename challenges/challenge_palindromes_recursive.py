def is_palindrome_recursive(
    word: str, low_index: int = 0, high_index: int = None
):
    if not word:
        return False

    if high_index is None:
        high_index = len(word) - 1

    word = word.lower().replace(" ", "")

    if low_index >= len(word) - 1:
        return True

    if word[low_index] != word[high_index]:
        return False

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
