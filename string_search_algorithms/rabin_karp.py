def rabin_karp(sentence: str, word: str):
    prime_number = 101
    d = 256
    M = len(word)
    N = len(sentence)
    p = 0  # initial hash value for pattern
    t = 0  # initial hash value for txt
    h = 1
    counter = 0

    # The value of h is "pow(d, M-1)% q"
    for i in range(M - 1):
        h = (h * d) % prime_number

    # Calculate the hash value of pattern and first window
    # of text
    for i in range(M):
        p = (d * p + ord(word[i])) % prime_number
        t = (d * t + ord(sentence[i])) % prime_number

    # Slide the pattern over text one by one
    for i in range(N - M + 1):
        # Check the hash values of current window of text and pattern
        # if the hash values match then only check for characters one by one
        if p == t:
            for j in range(M):
                if sentence[i + j] != word[j]:
                    break

            j += 1
            if j == M:
                counter += 1

        # Calculate hash value for next window of text: Remove leading digit, add trailing digit
        if i < N - M:
            t = (d * (t - ord(sentence[i]) * h) + ord(sentence[i + M])) % prime_number

            # We might get negative values of t, convert it to a positive number
            if t < 0:
                t = t + prime_number
    return counter
