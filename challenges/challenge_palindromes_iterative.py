def is_palindrome_iterative(word: str):

    if not word:
        return False
    
    word = word.lower().replace(" ", "")

    for index in range(len(word) // 2):
        if word[index] != word[- index - 1]:
            return False
        
    return True


print(is_palindrome_iterative("parap"))