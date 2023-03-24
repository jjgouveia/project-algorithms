def is_palindrome_iterative(word: str):
    if not word:
        return False

    word = word.lower().replace(" ", "")

    reversed_word = word[::-1]

    if word != reversed_word:
        return False

    return True
