def is_palindrome_iterative(word):
    word = word.lower().replace(" ", "")

    reversed_word = word[::-1]

    if word == reversed_word and not len(word) == 0:
        return True
    else:
        return False
