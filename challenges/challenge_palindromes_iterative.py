def is_palindrome_iterative(word):
    if not word:
        return False

    word = word.lower()
    word = word.replace(" ", "")

    reversed_word = word[::-1]

    if word != reversed_word:
        return False

    return True
