def linear_search(sentence: str, word):
    for i in range(len(sentence) - len(word) + 1):
        if sentence[i:i + len(word)] == word:
            return i

    return -1  # target substring not found
