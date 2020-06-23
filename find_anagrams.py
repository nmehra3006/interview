from collections import Counter
def find_anagrams(string, pattern):
    anagrams = []

    n_string = len(string)
    n_pattern = len(pattern)

    p_counter = Counter(pattern)

    for i in range(n_string-n_pattern+1):

        window_counter = Counter(string[i:i+n_pattern])
        if window_counter == p_counter:
            anagrams.append(i)

    return anagrams


print find_anagrams("abcabcabc", "abc")